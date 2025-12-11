import psutil
import platform
import socket
import os
import datetime
import time

timestamp = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")

# Infos processeur

cores_count = psutil.cpu_count()

cores_freq = psutil.cpu_freq().current 

cores_usage_percentage = psutil.cpu_percent(1)

# Infos mémoire

used_memory = round((psutil.virtual_memory().used) / (1024.0 ** 3), 2)

total_memory = round((psutil.virtual_memory().total) / (1024.0 ** 3), 2)

memory_usage_percentage = psutil.virtual_memory().percent

# Infos système

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


# Analyse des fichiers
folder = "/home/projetubuntu/Documents"
extensions = [".txt", ".py", ".pdf", ".jpg"]

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

count_txt = counts[".txt"]
count_py = counts[".py"]
count_pdf = counts[".pdf"]
count_jpg = counts[".jpg"]


#Infos processus

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

cpu_processus_list = ""
for p in cpu_processus:
    cpu_processus_list += "PID " + str(p[0]) + " — " + str(p[1]) + " : " + str(p[2]) + "%   |   "

memory_processus_list = ""
for p in memory_processus:
    memory_processus_list += "PID " + str(p[0]) + " — " + str(p[1]) + " : " + str(round(p[2], 1)) + "%   |   "

def cpu_value(processus):
    return processus[2]

resource_intensive_processus = sorted(cpu_processus, key=cpu_value, reverse=True)[:3]
process_1 = "PID " + str(resource_intensive_processus[0][0]) + " — " + str(resource_intensive_processus[0][1]) + " : " + str(round(resource_intensive_processus[0][2], 1)) + "%"
process_2 = "PID " + str(resource_intensive_processus[1][0]) + " — " + str(resource_intensive_processus[1][1]) + " : " + str(round(resource_intensive_processus[1][2], 1)) + "%"
process_3 = "PID " + str(resource_intensive_processus[2][0]) + " — " + str(resource_intensive_processus[2][1]) + " : " + str(round(resource_intensive_processus[2][2], 1)) + "%"


# Lecture du fichier HTML pour remplacer les variables
html = open("template.html").read()


# Remplacement des variables par les valeurs
html = html.replace("{{ timestamp }}", timestamp)
html = html.replace("{{ cores_count }}", str(cores_count))
html = html.replace("{{ cores_freq }}", str(cores_freq))
html = html.replace("{{ cores_usage_percentage }}", str(cores_usage_percentage))


html = html.replace("{{ used_memory }}", str(used_memory))
html = html.replace("{{ total_memory }}", str(total_memory))
html = html.replace("{{ memory_usage_percentage }}", str(memory_usage_percentage))

html = html.replace("{{ machine_name }}", machine_name)
html = html.replace("{{ os_name }}", os_name)
html = html.replace("{{ os_version }}", os_version)
html = html.replace("{{ boot_time }}", boot_time)
html = html.replace("{{ uptime }}", uptime)
html = html.replace("{{ users }}", str(users))
html = html.replace("{{ ip_adress }}", ip_adress)

html = html.replace("{{ cpu_processus_list }}", str(cpu_processus_list))
html = html.replace("{{ memory_processus_list }}", str(memory_processus_list))

html = html.replace("{{ process_1 }}", str(process_1))
html = html.replace("{{ process_2 }}", str(process_2))
html = html.replace("{{ process_3 }}", str(process_3))

html = html.replace("{{ folder }}", folder)
html = html.replace("{{ total_files }}", str(total_files))
html = html.replace("{{ count_txt }}", str(count_txt))
html = html.replace("{{ count_py }}", str(count_py))
html = html.replace("{{ count_pdf }}", str(count_pdf))
html = html.replace("{{ count_jpg }}", str(count_jpg))

html = html.replace("{{ percentage_txt }}", str(percentage_txt))
html = html.replace("{{ percentage_py }}", str(percentage_py))
html = html.replace("{{ percentage_pdf }}", str(percentage_pdf))
html = html.replace("{{ percentage_jpg }}", str(percentage_jpg))



# Création du fichier contenant les variables remplacées
with open("index.html", "w") as fp:
    fp.write(html)