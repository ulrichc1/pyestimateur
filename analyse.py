from estimateurs import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analyse(N:int,n:int):
    """
    @post -> list,list,list,list,list

    Test des différents estimateurs sur des jeux de données aléatoires

    """
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []

    for _ in range(1000):

        data = [i for i in range(1,N+1)]
        np.random.shuffle(data)
        ech = data[:n]

        t1.append(estimateur1(ech))
        t2.append(estimateur2(ech))
        t3.append(estimateur3(ech))
        t4.append(estimateur4(ech,n))
        t5.append(estimateur5(ech,n))
    return [t1,t2,t3,t4,t5]


def graph(t1,t2,t3,t4,t5,N,v):
    """Traçage d'un graphique à nuage de points des différents tableaux correspondant aux résultats des estimateurs"""
    # Création d'un DataFrame à partir des tableaux
    df = pd.DataFrame({'Estimateur 1': t1, 'Estimateur 2': t2, 'Estimateur 3': t3, 'Estimateur 4': t4, 'Estimateur 5': t5})

    # Affichage des graphiques
    if v==1: # Graphique linéaire
        plt.plot(df["Estimateur 1"], color="green")
        plt.plot(df["Estimateur 2"], color="violet")
        plt.plot(df["Estimateur 3"], color="cyan")
        plt.plot(df["Estimateur 4"], color="blue")
        plt.plot(df["Estimateur 5"], color="gold")

    elif v==2: # Graphique à nuage de points
        plt.plot(df["Estimateur 1"], '.', color="green")
        plt.plot(df["Estimateur 2"], '.', color="violet")
        plt.plot(df["Estimateur 3"], '.', color="cyan")
        plt.plot(df["Estimateur 4"], '.', color="blue")
        plt.plot(df["Estimateur 5"], '.', color="gold")

    plt.axhline(y=N, color='red', linestyle='-')

    plt.title("Graphique linéaire de la mesure des estimateurs")
    plt.legend(["Estimateur 1","Estimateur 2","Estimateur 3","Estimateur 4","Estimateur 5"])
    plt.xlabel("Échantillons")
    plt.ylabel("Estimation")
    plt.show()


def ecart_quad(N:int,n:int,val:int)->str:
    """
    @pre -> N,n,val sont des entiers
    @post -> str

    Retourne l'estimateur avec l'écart quadratique le plus faible.

    """
    t1,t2,t3,t4,t5 = analyse(N,n)[0],analyse(N,n)[1],analyse(N,n)[2],analyse(N,n)[3],analyse(N,n)[4]
    graph(t1,t2,t3,t4,t5,N,val)
    eq1 = np.mean(np.square(np.array(t1) - N))
    eq2 = np.mean(np.square(np.array(t2) - N))
    eq3 = np.mean(np.square(np.array(t3) - N))
    eq4 = np.mean(np.square(np.array(t4) - N))
    eq5 = np.mean(np.square(np.array(t5) - N))
    eqs = [eq1, eq2, eq3, eq4, eq5]
    print(eqs)
    index = eqs.index(min(eqs))+1 
    
    return f"estimateur n°{index}"