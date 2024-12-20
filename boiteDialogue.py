import tkinter as tk
from tkinter import filedialog

def choisir_fichier():
    # Ouvre une boîte de dialogue pour sélectionner un fichier
    chemin_fichier = filedialog.askopenfilename(title="Sélectionner un fichier")
    
    # Affiche le chemin du fichier sélectionné
    if chemin_fichier:
        label_chemin.config(text=f"Fichier sélectionné : {chemin_fichier}")
    else:
        label_chemin.config(text="Aucun fichier sélectionné")

def quitter():
    # Ferme la fenêtre principale proprement
    fenetre.destroy()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sélectionner un fichier")
fenetre.geometry("400x200")

# Ajout d'un bouton pour ouvrir le dialogue de sélection de fichier
btn_choisir_fichier = tk.Button(fenetre, text="Choisir un fichier", command=choisir_fichier)
btn_choisir_fichier.pack(pady=20)

# Label pour afficher le chemin du fichier
label_chemin = tk.Label(fenetre, text="Aucun fichier sélectionné")
label_chemin.pack(pady=20)

# Ajout du bouton "Quitter"
btn_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
btn_quitter.pack(pady=20)

# Lancer l'interface graphique
fenetre.mainloop()
