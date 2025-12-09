import psutil


cores_count = psutil.cpu_count()

# Infos mémoire
used_memory = (psutil.virtual_memory().used)/1000000000
total_memory = (psutil.virtual_memory().total)/1000000000
memory_usage_percentage = psutil.virtual_memory().percent


# Lecture du fichier HTML pour remplacer les variables
html = open("template.html").read()


# Remplacement des variables par les valeurs
html = html.replace("{{ cores_count }}", str(cores_count))


html = html.replace("{{ used_memory }}", str(used_memory))
html = html.replace("{{ total_memory }}", str(total_memory))
html = html.replace("{{ memory_usage_percentage }}", str(memory_usage_percentage))


# Création du fichier contenant les variables remplacées
with open("index.html", "w") as fp:
    fp.write(html)