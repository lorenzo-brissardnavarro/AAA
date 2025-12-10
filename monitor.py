import psutil
import datetime
import time
import socket


cores_count = psutil.cpu_count()

cores_freq = psutil.cpu_freq() 

cores_usage_percentage = psutil.cpu_percent(1)
# Infos mémoire
used_memory = (psutil.virtual_memory().used)/1000000000
total_memory = (psutil.virtual_memory().total)/1000000000
memory_usage_percentage = psutil.virtual_memory().percent

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
html = html.replace("{{ cores_usage_percentage}}", str(cores_usage_percentage))


html = html.replace("{{ used_memory }}", str(used_memory))
html = html.replace("{{ total_memory }}", str(total_memory))
html = html.replace("{{ memory_usage_percentage }}", str(memory_usage_percentage))


# Création du fichier contenant les variables remplacées
with open("index.html", "w") as fp:
    fp.write(html)