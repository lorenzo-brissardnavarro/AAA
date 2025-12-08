import psutil


cores_count = psutil.cpu_count()




# Lecture du fichier HTML pour remplacer les variables
html = open("template.html").read()


# Remplacement des variables par les valeurs
html = html.replace("{{ cores_count }}", str(cores_count))


# Création du fichier contenant les variables remplacées
with open("index.html", "w") as fp:
    fp.write(html)