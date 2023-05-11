import tkinter as tk
from tkinter import filedialog

to_be_found = 'Through Number'
to_be_found_bytes = to_be_found.encode()

# Fonction pour traiter chaque fichier sélectionné
def process_file(name):
	with open(name, "rb") as f:
		i = 1
		line = f.readline()
		while line:
			if to_be_found_bytes in line:
				filename = name[:-4] + ' ' + str(i) + name[-4:]
				print('Création de ' + filename)
				i += 1
				with open(filename, 'wb') as output:
					output.write(line)
					line = f.readline()
					while line and to_be_found_bytes not in line:
						output.write(line)
						line = f.readline()
			else:
				line = f.readline()

# Création de la fenêtre de sélection de fichiers
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilenames(title="Sélectionner les fichiers à traiter", filetypes=[("Fichiers ntb", "*.ntb")])

# Traitement des fichiers sélectionnés
if file_path:
	for file in file_path:
		process_file(file)
else:
	print("Aucun fichier sélectionné.")
