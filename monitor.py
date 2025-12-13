import psutil
import platform
import socket
import os
import datetime
import time


def get_timestamp():
    return datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")


def get_cpu_infos():
    cores_count = psutil.cpu_count()
    cores_freq = psutil.cpu_freq().current
    cores_usage_percentage = psutil.cpu_percent(1)
    return cores_count, cores_freq, cores_usage_percentage


def get_memory_infos():
    used_memory = round((psutil.virtual_memory().used) / (1024.0 ** 3), 2)
    total_memory = round((psutil.virtual_memory().total) / (1024.0 ** 3), 2)
    memory_usage_percentage = psutil.virtual_memory().percent
    return used_memory, total_memory, memory_usage_percentage


def get_system_infos():
    machine_name = socket.gethostname()
    os_name = platform.system()
    os_version = platform.release()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%Y à %H:%M:%S")

    uptime_seconds = time.time() - psutil.boot_time()
    uptime = str(datetime.timedelta(seconds=int(uptime_seconds)))

    ip_adress = ""
    for iface_name, iface_info in psutil.net_if_addrs().items():
        for addr in iface_info:
            if addr.family == socket.AF_INET and addr.address != "127.0.0.1":
                ip_adress = addr.address
                break

    users = len(psutil.users())

    return machine_name, os_name, os_version, boot_time, uptime, ip_adress, users


def analyze_files(folder, extensions):
    counts = {}
    for ext in extensions:
        counts[ext] = 0

    total_files = 0

    for root, dirs, files in os.walk(folder):
        for name in files:
            total_files += 1
            for ext in extensions:
                if name.lower().endswith(ext):
                    counts[ext] += 1

    percentage_txt = round((counts[".txt"] / total_files) * 100, 2)
    percentage_py = round((counts[".py"] / total_files) * 100, 2)
    percentage_pdf = round((counts[".pdf"] / total_files) * 100, 2)
    percentage_jpg = round((counts[".jpg"] / total_files) * 100, 2)
    percentage_html = round((counts[".html"] / total_files) * 100, 2)
    percentage_css = round((counts[".css"] / total_files) * 100, 2)
    percentage_js = round((counts[".js"] / total_files) * 100, 2)
    percentage_png = round((counts[".png"] / total_files) * 100, 2)

    return total_files, counts, percentage_txt, percentage_py, percentage_pdf, percentage_jpg, percentage_html, percentage_css, percentage_js, percentage_png


def get_process_infos():
    cpu_processus = []
    for processus in psutil.process_iter(['pid', 'name']):
        consumption_cpu = processus.cpu_percent(interval=None)

    time.sleep(1)

    for processus in psutil.process_iter(['pid', 'name']):
        consumption_cpu = processus.cpu_percent(interval=None)
        if consumption_cpu > 0.0:
            cpu_processus.append((processus.info['pid'], processus.info['name'], consumption_cpu))

    memory_processus = []
    for processus in psutil.process_iter(['pid', 'name']):
        consumption_memory = processus.memory_percent()
        if consumption_memory > 0.0:
            memory_processus.append((processus.info['pid'], processus.info['name'], consumption_memory))

    return cpu_processus, memory_processus


def format_process_lists(cpu_processus, memory_processus):
    cpu_processus_list = ""
    for p in cpu_processus:
        cpu_processus_list += "PID " + str(p[0]) + " — " + str(p[1]) + " : " + str(p[2]) + "%   |   "

    memory_processus_list = ""
    for p in memory_processus:
        memory_processus_list += "PID " + str(p[0]) + " — " + str(p[1]) + " : " + str(round(p[2], 1)) + "%   |   "

    return cpu_processus_list, memory_processus_list


def get_top_cpu_processes(cpu_processus):
    def cpu_value(processus):
        return processus[2]

    resource_intensive_processus = sorted(cpu_processus, key=cpu_value, reverse=True)[:3]

    process_1 = ""
    process_2 = ""
    process_3 = ""

    if len(resource_intensive_processus) > 0:
        process_1 = "PID " + str(resource_intensive_processus[0][0]) + " — " + str(resource_intensive_processus[0][1]) + " : " + str(round(resource_intensive_processus[0][2], 1)) + "%"
    if len(resource_intensive_processus) > 1:
        process_2 = "PID " + str(resource_intensive_processus[1][0]) + " — " + str(resource_intensive_processus[1][1]) + " : " + str(round(resource_intensive_processus[1][2], 1)) + "%"
    if len(resource_intensive_processus) > 2:
        process_3 = "PID " + str(resource_intensive_processus[2][0]) + " — " + str(resource_intensive_processus[2][1]) + " : " + str(round(resource_intensive_processus[2][2], 1)) + "%"

    return process_1, process_2, process_3


def collect_replacements():
    timestamp = get_timestamp()

    cores_count, cores_freq, cores_usage_percentage = get_cpu_infos()
    used_memory, total_memory, memory_usage_percentage = get_memory_infos()
    machine_name, os_name, os_version, boot_time, uptime, ip_adress, users = get_system_infos()

    folder = "/home/projetubuntu/Documents"
    extensions = [".txt", ".py", ".pdf", ".jpg", ".html", ".css", ".js", ".png"]

    total_files, counts, percentage_txt, percentage_py, percentage_pdf, percentage_jpg, percentage_html, percentage_css, percentage_js, percentage_png = analyze_files(folder, extensions)

    cpu_processus, memory_processus = get_process_infos()
    cpu_processus_list, memory_processus_list = format_process_lists(cpu_processus, memory_processus)

    process_1, process_2, process_3 = get_top_cpu_processes(cpu_processus)

    replacements = {
        "{{ timestamp }}": timestamp,
        "{{ cores_count }}": cores_count,
        "{{ cores_freq }}": cores_freq,
        "{{ cores_usage_percentage }}": cores_usage_percentage,
        "{{ used_memory }}": used_memory,
        "{{ total_memory }}": total_memory,
        "{{ memory_usage_percentage }}": memory_usage_percentage,
        "{{ machine_name }}": machine_name,
        "{{ os_name }}": os_name,
        "{{ os_version }}": os_version,
        "{{ boot_time }}": boot_time,
        "{{ uptime }}": uptime,
        "{{ users }}": users,
        "{{ ip_adress }}": ip_adress,
        "{{ cpu_processus_list }}": cpu_processus_list,
        "{{ memory_processus_list }}": memory_processus_list,
        "{{ process_1 }}": process_1,
        "{{ process_2 }}": process_2,
        "{{ process_3 }}": process_3,
        "{{ folder }}": folder,
        "{{ total_files }}": total_files,
        "{{ count_txt }}": counts[".txt"],
        "{{ count_py }}": counts[".py"],
        "{{ count_pdf }}": counts[".pdf"],
        "{{ count_jpg }}": counts[".jpg"],
        "{{ count_html }}": counts[".html"],
        "{{ count_css }}": counts[".css"],
        "{{ count_js }}": counts[".js"],
        "{{ count_png }}": counts[".png"],
        "{{ percentage_txt }}": percentage_txt,
        "{{ percentage_py }}": percentage_py,
        "{{ percentage_pdf }}": percentage_pdf,
        "{{ percentage_jpg }}": percentage_jpg,
        "{{ percentage_html }}": percentage_html,
        "{{ percentage_css }}": percentage_css,
        "{{ percentage_js }}": percentage_js,
        "{{ percentage_png }}": percentage_png
    }

    return replacements


def generate_html(replacements):
    html = open("template.html").read()

    for key, value in replacements.items():
        html = html.replace(key, str(value))

    with open("index.html", "w") as fp:
        fp.write(html)


def main():
    running = True
    while running:
        replacements = collect_replacements()
        generate_html(replacements)
        time.sleep(30)


main()
