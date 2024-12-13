def tab(file_path):
    """
    Fonction pour lire un fichier ICS ligne par ligne et stocker chaque ligne dans un tableau.
    
    :param file_path: Le chemin du fichier .ics
    :return: Liste contenant les lignes du fichier.
    """
    lines = []  # Initialisation de la liste pour stocker les lignes
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Lire le fichier ligne par ligne et ajouter chaque ligne à la liste
            for line in file:
                lines.append(line.strip())  # Ajouter la ligne après suppression des espaces et retours à la ligne
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{file_path}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur: Impossible d'ouvrir le fichier '{file_path}'.")
    
    return lines

def rechercheFlag(mot, lignes):
    """
    Recherche un mot dans chaque ligne d'un tableau et affiche les lignes contenant ce mot.
    
    :param mot: Le mot à rechercher.
    :param lignes: La liste des lignes dans lesquelles chercher.
    """
    print(f"\nRecherche du mot '{mot}' dans les lignes :")
    found = False  # Variable pour savoir si on a trouvé au moins une ligne
    for i, ligne in enumerate(lignes, 1):
        if mot.lower() in ligne.lower():  # Recherche insensible à la casse
            print(f"Ligne {i}: {ligne}")
            found = True
    
    if not found:
        print(f"Aucune ligne ne contient le mot '{mot}'.")

def main():
    # Définir le chemin du fichier .ics
    file_path = "testEv.ics"
    
    # Appeler la fonction tab pour lire le fichier et obtenir les lignes dans un tableau
    lignes = tab(file_path)
    
    # Afficher les lignes récupérées (facultatif)
    if lignes:
        print("Les lignes du fichier .ics sont :")
        for i, ligne in enumerate(lignes, 1):
            print(f"Ligne {i}: {ligne}")
    else:
        print("Aucune ligne lue du fichier.")
    
    # Recherche d'un mot spécifique dans les lignes
    mot_a_rechercher = "LACAN"  # Exemple de mot à rechercher
    rechercheFlag(mot_a_rechercher, lignes)

# Point d'entrée du programme
if __name__ == "__main__":
    main()
