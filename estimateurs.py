# Author : Ulrich COUDIN

def mediane(nombres):
    """ calcul de la médiane des valeurs d'une liste"""
    N=len(nombres)
    nombres.sort()
    # Trouve la médiane 
    if N%2==0:
        # Si N est pair
        ml=N/2
        m2=(N/2)+1
        # Convertir en entiers, faire correspondre la position dans la liste
        ml=int(ml)-1
        m2=int(m2)-1
        mediane=(nombres[ml]+nombres[m2])/2
    else:
        m=(N+1)/2
        # Convertir en entiers, faire correspondre 1a positiondans la liste
        m=int(m)-1
        mediane=nombres[m]
    return mediane

def moyenne(nombres):
    """ calcul de la moyenne des valeurs d'une liste"""
    N = len(nombres)
    s = 0
    for i in range(N):
        s += nombres[i]
    return s/N


def estimateur1(liste):
    """estimation de grand N d'un échantillon n prélevé à l'aide de la 1ère formule"""
    return 2*(mediane(liste))-1

def estimateur2(liste):
    """estimation de grand N d'un échantillon n prélevé à l'aide de la 2nd formule"""
    return 2*(moyenne(liste))-1

def estimateur3(liste):
    """estimation de grand N d'un échantillon n prélevé à l'aide de la 3ème formule"""
    return (max(liste)+min(liste))-1

def estimateur4(liste,n):
    """estimation de grand N d'un échantillon n prélevé à l'aide de la 4ème formule"""
    return (max(liste)*(n+1)/(n))-1

def estimateur5(liste,n):
    """estimation de grand N d'un échantillon n prélevé à l'aide de la 5ème formule"""
    return (((max(liste)-min(liste))*(n+1)/(n-1)))-1