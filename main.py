# Author : Ulrich COUDIN

from analyse import *
from tkinter import *
import sys
import subprocess

try:
    from customtkinter import *
except ImportError:
    print("CustomTkinter n'est pas installé.")
    install = input("Voulez-vous l'installer maintenant ? (O/N) ")
    if install.lower() == "o":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter'])
    else:
        print("Installation annulée.")

### GUI : Interface graphique pour l'exécution des modules

# Exécution des modules
def execute_meilleure_estimateur():
    """Execute la fonction ecart_quad"""
    # Vérification des entrées utilisateur
    if not (N_entry.get()).isdigit() or not (n_entry.get()).isdigit():
        resultat_label.configure(text="Les entrées doivent être des entiers.")
        return
    elif v.get()== 0:
        resultat_label.configure(text="Veuillez sélectionner une option d'affichage.")
        return
    else:
        N = int(N_entry.get())
        n = int(n_entry.get())
        val = int(v.get())
        resultat = ecart_quad(N, n, val)
        resultat_label.configure(text=f"Le meilleur estimateur pour un échantillon de {n} individus prélevé dans une série de {N} individus serait l'{resultat}.")
        
root = CTk()
root.title("Logiciel d'analyse d'estimateurs (échantillonage)")
root.geometry("800x600")

# Création des widgets
N_label = CTkLabel(master=root, text="Population (N):")
N_entry = CTkEntry(master=root)
n_label = CTkLabel(master=root, text="Échantillon (n):")
n_entry = CTkEntry(master=root)
execute_button = CTkButton(master=root, text="Exécuter", command=execute_meilleure_estimateur)
resultat_label = CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("white", "gray45"),
                               corner_radius=8,
                               text="")

v = IntVar()

radioTitle = CTkLabel(master=root, 
        text="Type de représentation graphique:",
        )

radio1 = CTkRadioButton(master=root,  
               text="Graphique linéaire",
               variable= v, 
               value=1)

radio2 = CTkRadioButton(master=root,
               text="Graphique en nuage de points",
               variable= v, 
               value=2)

radio3 = CTkRadioButton(master=root,
               text="Diagramme à dispersions",
               variable= v, 
               value=3)

radio4 = CTkRadioButton(master=root,
               text="Diagrammes en boîtes",
               variable= v, 
               value=4)

# Placement des widgets dans la fenêtre
N_label.pack(pady=10)
N_entry.pack(pady=5)
n_label.pack(pady=10)
n_entry.pack(pady=5)
radioTitle.pack(pady=10)
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)
radio4.pack(pady=5)
execute_button.pack(pady=30)
resultat_label.pack(pady=50)

# Boucle principale
root.mainloop()