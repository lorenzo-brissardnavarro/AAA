import psutil
import platform
import socket
import os
import datetime
import time

# Infos processeur
cores_count = psutil.cpu_count()
cores_freq = psutil.cpu_freq().current 
cores_usage_percentage = psutil.cpu_percent(1)

# Infos mémoire
used_memory = (psutil.virtual_memory().used) / (1024.0 ** 3)
total_memory = (psutil.virtual_memory().total) / (1024.0 ** 3)
memory_usage_percentage = psutil.virtual_memory().percent

# Infos système
machine_name = socket.gethostname()
os_name = platform.system()
os_version = platform.release()

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
print(boot_time)

uptime_seconds = time.time() - psutil.boot_time()
uptime = datetime.timedelta(seconds=int(uptime_seconds))
print(uptime)

for iface_name, iface_info in psutil.net_if_addrs().items():
    for addr in iface_info:
        if addr.family == socket.AF_INET and addr.address != "127.0.0.1":
            print(addr.address)
            break

users = len(psutil.users())



folder = "/home/projetubuntu/Documents"
extensions = [".txt", ".py", ".pdf", ".jpg"]

counts = {}
for ext in extensions:
    counts[ext] = 0

total_files = 0

for racine, dossiers, fichiers in os.walk(folder):
    for nom in fichiers:
        total_files += 1
        for ext in extensions:
            if nom.lower().endswith(ext):
                counts[ext] += 1


for ext in extensions: 
    if total_files > 0:
        percentage = (counts[ext] / total_files) * 100
    else:
        percentage = 0
    print(f"{ext} : {counts[ext]} fichiers ({percentage:.2f}%)")

print("Total de fichiers analysés :", total_files)
#Infos processus
cpu_processus = []
for processus in psutil.process_iter(['pid', 'name']):
    consumption_cpu = processus.cpu_percent(interval=None)
time.sleep(1)
for processus in psutil.process_iter(['pid', 'name']):
    consumption_cpu = processus.cpu_percent(interval=None)
    if consumption_cpu > 0.0:
        cpu_processus.append((processus.info['pid'], processus.info['name'], consumption_cpu))
print(cpu_processus)

memory_processus = []
for processus in psutil.process_iter(['pid', 'name']):
    consumption_memory = processus.memory_percent()
    if consumption_memory > 0.0:
        memory_processus.append((processus.info['pid'], processus.info['name'], consumption_memory))
print(memory_processus)


def cpu_value(processus):
    return processus[2]

resource_intensive_processus = sorted(cpu_processus, key=cpu_value, reverse=True)[:3]
print(resource_intensive_processus)


# Lecture du fichier HTML pour remplacer les variables
html = open("template.html").read()


# Remplacement des variables par les valeurs
html = html.replace("{{ cores_count }}", str(cores_count))
html = html.replace("{{ cores_freq }}", str(cores_freq))
html = html.replace("{{ cores_usage_percentage }}", str(cores_usage_percentage))


html = html.replace("{{ used_memory }}", str(used_memory))
html = html.replace("{{ total_memory }}", str(total_memory))
html = html.replace("{{ memory_usage_percentage }}", str(memory_usage_percentage))

html = html.replace("{{ machine_name }}", str(machine_name))
html = html.replace("{{ os_name }}", str(os_name))
html = html.replace("{{ os_version }}", str(os_version))
html = html.replace("{{ users }}", str(users))



# Création du fichier contenant les variables remplacées
with open("index.html", "w") as fp:
    fp.write(html)