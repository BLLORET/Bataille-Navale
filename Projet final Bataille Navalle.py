# -*- coding: utf-8 -*-

"""
Bienvenue sur le jeu de la bataille navale en Python.
Les règles sont simples. Vous et l'ordinateur tirez chacun votre tour dans la
grille de l'adversaire pour essayer de toucher un bateau afin de le couler.
Quand un de vous deux arrive à couler la totalité des bateaux adverse, la
victoire est attribué.
Les bateaux de 2 cases sont codées par des 2, ceux de 3 cases par des 3 et
ainsi de suite. Les cases vides sont codées par des 0, une case vide où l'on a
tiré est codée par 0 et les cases touchés sont codées par des multiples de 10
comme 20, 30 ou encore 40 selon la taille du bateau.
Bon jeu
"""
import random


def taille_grille() -> int:
    """
    Cette fonction demande à l'utilisateur la taille voulue pour la grille de
    jeu où se déroulera la partie. Elle n'a pas besoin de recevoir d'argument
    mais retourne la valeur d'un entier correspondant à la longueur d'un coté
    du carré délimitant l'aire de jeu.

    Paramètre
    ---------
    None

    Retour
    ------
    n : int
        Valeur correspondant à la longueur d'un coté du carré du plateau de jeu
    """

    reponse_ok = False
    while not reponse_ok:   # Tant que la réponse n'est pas vrai

        # L'utilisateur entre les dimensions du plateau de jeu
        taille = input(" La taille du plateau de jeu sera de '5x5', '6x6', \
'7x7','8x8' ou '9x9' ? : ")

        # On retient la taille de la grille dans la variable n

        reponse_ok = True   # On pense que la réponse sera correcte
        if taille == "5x5":
            n = 5
        elif taille == "6x6":
            n = 6
        elif taille == "7x7":
            n = 7
        elif taille == "8x8":
            n = 8
        elif taille == "9x9":
            n = 9
        else:
            reponse_ok = False   # Finalement la réponse est fausse

    return n


def verif_dims_bat_hor(liste: list, taille: int) -> bool:
    """
    Cette fonction reçoit comme arguments une liste correspondante aux indices
    des colonnes où vont être placés les bateaux et la dimension du plateau de
    jeu. Si les indices des colonnes sont situés dans le plateaux la fonction
    retourne True, sinon elle retourne False.

    Paramètres
    ----------
    liste : list
        Liste des indices des colonnes
    taille : int
        Dimension du plateau de jeu

    Retour
    ------
    ok : bool
        Booléen qui donne une condition
    """
    ok = True  # On supose que la fonction renvoie True
    # On parcours les indices des colonnes
    for colonne in liste:
        # Si l'indice n'est pas dans le plateau de jeu ...
        if colonne > taille - 1 or colonne < 0:
            ok = False  # ... La fonction renvoie finalement False ...
            break  # ... Et stop la boucle

    return ok


def verif_dims_bat_vert(liste: list, taille: int) -> bool:
    """
    Cette fonction reçoit comme arguments une liste correspondante aux indices
    des lignes où vont être placés les bateaux et la dimension du plateau de
    jeu. Si les indices des lignes sont situés dans le plateaux la fonction
    retourne True, sinon elle retourne False.

    Paramètres
    ----------
    liste : list
        Liste des indices des lignes
    taille : int
        Dimension du plateau de jeu

    Retour
    ------
    ok : bool
        Booléen qui donne une condition
    """
    ok = True  # On suppose que la fonction renvoie True
    # On parcours les indices des lignes
    for ligne in liste:
        # Si l'indice n'est pas dans le plateau de jeu ...
        if ligne > taille - 1 or ligne < 0:
            ok = False  # ... La fonction renvoie finalement False ...
            break  # ... Et stop la boucle

    return ok


def case_dispo(tab: list, ligne: int, colonne: int) -> bool:
    """
    Cette fonction a pour rôle de tester si la case visée est vide ou déjà
    attribuée dans la zone du plateau de jeu en fonction de sa colonne et de sa
    ligne. La fonction reçoit comme argument la liste du plateau de jeu, la
    ligne et la colonne où vont être effectué le test. la fonction retourne un
    booléen. Si la case n'a jamais été visé la fonction retourne True. Si elle
    a déjà été visé la fonction retourne False.

    Paramètres
    ----------
    tab : list
        Liste qui correspond au plateau de jeu où sera effectué le test
    ligne : int
        Cela correspond à la position de la ligne où est effectué le test
    colonne: int
        Cela correspond à la position de la colonne où est effectué le test

    Retour
    ------
    True or False : bool
        La fonction retourne soit True soit False selon la disponibilité de la
    case
    """

    # On regarde si la case visé est codée par 0
    if tab[ligne][colonne] == 0:
        return True   # L'affirmation est vraie
    else:
        return False   # L'affirmation est fausse


def cases_dispo_horizontales(tab: list, l: list, ligne: int) -> bool:
    """
    Cette fonction reçoit en argument le plateau de jeu noté tab, une liste
    correspondante aux indices des positions probables du bateau et de la ligne
    correspondante à laquelle le placement horizontal est supposé être. Dans le
    cas où une case est déjà occupée, la fonction s'arête et renvoit False. Si
    elle a parcourru toute la liste et que toutes les cases visées étaient
    disponibles, la fonction renvoit True.

    Paramètres
    ----------
    tab : list
        Liste du plateau de jeu
    l : list
        Liste des indices à tester
    ligne : int
        Ligne où se situe le bateau horizontal

    Retour
    ------
    ok = bool
        Booléen qui donne une condition
    """
    ok = True  # On suppose que le placement est bon
    # On parcours les indices des colonnes de la liste l
    for colonne in l:
        # Si la position n'est pas codée par 0 ...
        if tab[ligne][colonne] != 0:
            ok = False  # ... La fonction renvoie finalement False ...
            break  # ... Et stop la boucle

    return ok


def cases_dispo_verticales(tab: list, l: list, colonne: int) -> bool:
    """
    Cette fonction reçoit en argument le plateau de jeu noté tab, une liste
    correspondante aux indices des positions probables du bateau, de la colonne
    correspondante à laquelle le placement horizontal est supposé être. Dans le
    cas où une case est déjà occupée, la fonction s'arête et renvoit False. Si
    elle a parcourru toute la liste et que toutes les cases visées étaient
    disponibles, la fonction renvoit True.

    Paramètres
    ----------
    tab : list
        Liste du plateau de jeu
    l : list
        Liste des indices à tester
    colonne : int
        Colonne où se situe le bateau horizontal

    Retour
    ------
    ok = bool
        Booléen qui donne une condition
    """
    ok = True  # On suppose que le placement est bon
    # On parcours les indices des ligne de la liste l
    for ligne in l:
        # Si la position n'est pas codée par 0 ...
        if tab[ligne][colonne] != 0:
            ok = False  # ... La fonction renvoie finalement False ...
            break  # ... Et stop la boucle

    return ok


def place_bateau_auto(tab: list, taille: int, n: int) -> list:
    """
    Cette fonction a pour rôle de placer automatiquement un bateaux de taille n
    dans la grille de l'adversaire. Elle prend comme arguments le plateau de
    jeu noté tab, la dimension du plateau taille et la taille n du bateau.
    Cette fonction réagit sous forme d'une boucle. Elle va tirer aléatoirement
    les coordonnées de la première case et son orientation afin de décider de
    son placement. Dans chaque cas d'orientation, la fonction va vérifier à
    l'aide de fonctions intermédiaires si les indices sont situés dans le
    plateau de jeu et si les cases du bateau sont disponibles. Si c'est bon, le
    bateau est plaçé sinon les coordonnées sont à nouveau tiré aléatoirement
    jusqu'à avoir placé le bateau. La fonction retourne ensuite la liste avec
    le bateau placé.

    Paramètres
    ----------
    tab : list
        Liste du plateau de jeu
    taille : int
        Dimension du plateau de jeu
    n : int
        Taille du bateau à placer

    Retour
    ------
    tab : list
        Plateau de jeu avec le bateau placé
    """
    i = 0  # Initialisation du compteur
    while i < 1:  # Tant que le bateau n'est pas placé
        # On génère aléatoirement la ligne, la colonne et l'orientation
        ligne = random.randint(0, taille - 1)
        colonne = random.randint(0, taille - 1)
        orientation = random.randint(0, 3)
        # On place le bateau vers le haut
        if orientation == 0:
            # On retient les indices de position dans plh
            plh = place_haut(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_vert(plh, taille) and cases_dispo_verticales(tab, plh, colonne):
                i += 1  # Incrémentation du compteur
                for ligne in plh:  # On parcours les indices des postions...
                    tab[ligne][colonne] = n  # ... Et on code par n
        # On place le bateau vers la droite
        elif orientation == 1:
            # On retient les indices de position dans pld
            pld = place_droite(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_hor(pld, taille) and cases_dispo_horizontales(tab, pld, ligne):
                i += 1  # Incrémentation du compteur
                for colonne in pld:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n
        # On place le bateau vers le bas
        elif orientation == 2:
            # On retient les indices de position dans plb
            plb = place_bas(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_vert(plb, taille) and cases_dispo_verticales(tab, plb, colonne):
                i += 1  # Incrémentation du compteur
                for ligne in plb:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n
        # On place le bateau vers la gauche
        else:
            # On retient les indices de position dans plg
            plg = place_gauche(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_hor(plg, taille) and cases_dispo_horizontales(tab, plg, ligne):
                i += 1  # Incrémentation du compteur
                for colonne in plg:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n

    return tab


def place_bateau_manuel(tab, taille, n):
    """
    Cette fonction a pour rôle de placer manuellement un bateaux de taille n
    dans notre grille. Elle prend comme arguments le plateau de jeu noté tab,
    la dimension du plateau taille et la taille n du bateau.
    Cette fonction réagit sous forme d'une boucle. Elle va nous demander les
    coordonnées de la première case et son orientation afin de décider de son
    placement. Dans chaque cas d'orientation, la fonction va vérifier à l'aide
    de fonctions intermédiaires si les indices sont situés dans le plateau de
    jeu et si les cases du bateau sont disponibles. Si c'est bon, le bateau est
    plaçé sinon les coordonnées sont à nouveau demandé jusqu'à avoir placé le
    bateau. La fonction retourne ensuite la liste avec le bateau placé.

    Paramètres
    ----------
    tab : list
        Liste du plateau de jeu
    taille : int
        Dimension du plateau de jeu
    n : int
        Taille du bateau à placer

    Retour
    ------
    tab : list
        Plateau de jeu avec le bateau placé
    """
    i = 0  # Initialisation du compteur
    while i < 1:  # Tant que le bateau n'est pas placé
        # On demande à l'utilisateur de placer son bateau
        ligne = int(input("Veuillez entrer la valeur de la ligne : ")) - 1
        colonne = int(input("Veuillez entrer la valeur de la colonne : ")) - 1
        orientation = input('Entrez "haut", "droite", "bas" ou "gauche" : ')
        # On place le bateau vers le haut
        if orientation == "haut":
            # On retient les indices de position dans plh
            plh = place_haut(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_vert(plh, taille) and cases_dispo_verticales(tab, plh, colonne):
                i += 1  # Incrémentation du compteur
                for ligne in plh:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n
                    # On place le bateau vers la droite
        elif orientation == "droite":
            # On retient les indices de position dans pld
            pld = place_droite(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_hor(pld, taille) and cases_dispo_horizontales(tab, pld, ligne):
                i += 1  # Incrémentation du compteur
                for colonne in pld:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n
            # On place le bateau vers le bas
        elif orientation == "bas":
            # On retient les indices de position dans plb
            plb = place_bas(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_vert(plb, taille) and cases_dispo_verticales(tab, plb, colonne):
                i += 1  # Incrémentation du compteur
                for ligne in plb:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n
        # On place le bateau vers la gauche
        else:
            # On retient les indices de position dans plg
            plg = place_gauche(tab, ligne, colonne, n)
            # Verification des conditions
            if verif_dims_bat_hor(plg, taille) and cases_dispo_horizontales(tab, plg, ligne):
                i += 1  # Incrémentation du compteur
                for colonne in plg:  # On parcours les indices des postions ...
                    tab[ligne][colonne] = n  # ... Et on code par n

    return tab


def creation_tableau(taille: int) -> list:
    """
    Cette fonction à pour rôle de créer un tableau de taille n choisie
    préalablement par l'utilisateur et de le garder en mémoire sous forme de
    liste de liste.

    Paramètre
    ---------
    taille : int
        Entier correspondant à une longueur du tableau carré

    Retour
    ------
    tab : list
        Tableau remplie de 0
    """
    tab = []  # Création d'une liste vide
    # On répète la 1ere boucle le nombre de fois la valeur de taille
    for i in range(taille):
        l_inter = []  # Création d'une seconde liste vide
        # On répète la 2nde boucle le nombre de fois la valeur de taille
        for j in range(taille):
            l_inter.append(0)  # On remplie la 2nde liste de 0
        tab.append(l_inter)  # On remplie la 1ere liste avec la 2nde liste

    return tab


def place_droite(tab: list, ligne: int, colonne: int, n: int) -> list:
    """
    Cette fonction a pour rôle de placer le bateau vers la droite case par case
    à partir d'une position déjà connue auparavant. Elle prend en argument la
    liste correspondant au plateau de jeu, la ligne correspondant à la ligne
    de plaçage, la colonne a partir de laquelle est fixé le plaçage et la
    taille n du bateau à placer.

    Paramètres
    ----------
    tab : list
        Tableau qui correspond au plateau de jeu
    ligne : int
        Position de la ligne où est effectué le plaçage
    colonne : int
        Position de la première colonne d'où part le plaçage
    n : int
        Taille du bateau

    Retours
    -------
    l : list
        Liste contenant les indices des colonnes
    """
    l = []  # Création d'une liste vide
    for i in range(n):  # On répète l'élément n fois
        l.append(colonne)  # On ajoute l'indice de la colonne à la liste ...
        colonne += 1  # ... et on augmente de 1 l'indice de la colonne

    return l


def place_gauche(tab: list, ligne: int, colonne: int, n: int) -> list:
    """
    Cette fonction a pour rôle de placer le bateau vers la gauche case par case
    à partir d'une position déjà connue auparavant. Elle prend en argument la
    liste correspondant au plateau de jeu, la ligne correspondant à la ligne
    de plaçage, la colonne a partir de laquelle est fixé le plaçage et la
    taille n du bateau à placer.

    Paramètres
    ----------
    tab : list
        Tableau qui correspond au plateau de jeu
    ligne : int
        Position de la ligne où est effectué le plaçage
    colonne : int
        Position de la première colonne d'où part le plaçage
    n : int
        Taille du bateau

    Retours
    -------
    l : list
        Liste contenant les indices des colonnes
    """

    l = []  # Création d'une liste vide
    for i in range(n):  # On répète l'élément n fois
        l.append(colonne)  # On ajoute l'indice de la colonne à la liste ...
        colonne -= 1  # ... et on réduit de 1 l'indice de la colonne

    return l


def place_haut(tab: list, ligne: int, colonne: int, n: int) -> list:
    """
    Cette fonction a pour rôle de placer le bateau vers le haut case par case à
    partir d'une position déjà connue auparavant. Elle prend en argument la
    liste correspondant au plateau de jeu, la ligne a partir de laquelle est
    fixé le plaçage, la colonne correspondant à la colonne de plaçage et la
    taille n du bateau à placer.

    Paramètres
    ----------
    tab : list
        Tableau qui correspond au plateau de jeu
    ligne : int
        Position de la première ligne d'où part le plaçage
    colonne : int
        Position de la colonne où est effectué le plaçage
    n : int
        Taille du bateau

    Retours
    -------
    l : list
        Liste contenant les indices des lignes
    """

    l = []  # Création d'une liste vide
    for i in range(n):  # On répète l'élément n fois
        l.append(ligne)  # On ajoute l'indice de la ligne à la liste ...
        ligne -= 1  # ... et on réduit de 1 l'indice de la ligne

    return l


def place_bas(tab: list, ligne: int, colonne: int, n: int) -> list:
    """
    Cette fonction a pour rôle de placer le bateau vers le bas case par case à
    partir d'une position déjà connue auparavant. Elle prend en argument la
    liste correspondant au plateau de jeu, la ligne a partir de laquelle est
    fixé le plaçage, la colonne correspondant à la colonne de plaçage et la
    taille n du bateau à placer.

    Paramètres
    ----------
    tab : list
        Tableau qui correspond au plateau de jeu
    ligne : int
        Position de la première ligne d'où part le plaçage
    colonne : int
        Position de la colonne où est effectué le plaçage
    n : int
        Taille du bateau

    Retours
    -------
    l : list
        Liste contenant les indices des lignes
    """

    l = []  # Création d'une liste vide
    for i in range(n):  # On répète l'élément n fois
        l.append(ligne)  # On ajoute l'indice de la ligne à la liste ...
        ligne += 1  # ... et on augmente de 1 l'indice de la ligne

    return l


def tir_com(liste: list, taille: int):
    """
    Cette fonction permet à l'ordinateur de tirer au hasard dans notre grille
    de jeu en prenant comme arguments la liste correspondante au plateau de jeu
    et la largeur de la grille appelé taille.

    Paramètres
    ----------
    liste : list
        Plateau de jeu
    taille : int
        Largeur de la grille
    """
    # On génère aléatoirement le point de tir
    colonne = random.randint(0, taille - 1)
    ligne = random.randint(0, taille - 1)
    # Vérification de la disponibilité de la case
    if case_dispo(liste, ligne, colonne):
        # La case est libre donc pas de bateau,
        # on la code 1 pour ne pas retirer dessus
        liste[ligne][colonne] = 1
        print("L'ordinateur à tiré à l'eau !")
    # La case n'est pas libre
    else:
        ok = False
        while not ok:  # Tant que la réponse n'est pas vraie

            # Case différente de 1 et inférieure à 10
            if liste[ligne][colonne] != 1 and liste[ligne][colonne] < 10:
                ok = True  # La  réponse devient vrai
                liste[ligne][colonne] *= 10  # On mutltiplie par 10 la valeur
                print(" L'ordinateur vous a touché !")
            # La case a déjà été visée donc on relance le point de tir
            else:
                colonne = random.randint(0, taille - 1)
                ligne = random.randint(0, taille - 1)

    return liste


def tir_nous(liste: list):
    """
    Cette fonction nous permettre de tirer dans la grille de l'adversaire en
    prenant comme argument le plateau de jeu.

    Paramètre
    ---------
    liste : list
        Plateau de jeu

    Retour
    ------
    None
    """
    ok = False
    while not ok:  # Tant que la réponse n'est pas vrai
        ok = True  # On suppose que la réponse sera vrai
        # On demande à l'utilisateur où il souhaite tirer
        ligne = int(input("Dans quelle ligne souhaitez vous tirer?:")) - 1
        colonne = int(input("Dans quelle colonne souhaitez vous tirer?:")) - 1
        # Si l'utilisateur rentre une case impossible ...
        if colonne not in range(0, len(liste)) or ligne not in range(0, len(liste)):
            ok = False  # ... La reponse devient fausse
        # La case est vide donc on la code en 1 pour ne pas y retirer plus tard
        elif case_dispo(liste, ligne, colonne):
            liste[ligne][colonne] = 1
            print("A l'eau !")
        else:
            if liste[ligne][colonne] == 1:  # Case déja ciblée
                ok = False  # La reponse devient fausse
            elif liste[ligne][colonne] > 10:  # Case déjà ciblée
                ok = False  # La reponse devient fausse
            # La case est occupée par un bateau.
            else:  # On l'a touché donc on code par x10
                liste[ligne][colonne] *= 10
                print("Touché !")

    return liste


def liste_bateau(taille: int) -> list:
    """
    Cette fonction a pour rôle de garder en mémoire dans une liste le nombre de
    bateaux présent dans la grille en fonction de la taille de celle-ci.
    Elle commence par créer une liste vide puis ajoute la valeur de chaque
    bateau dedans.

    Paramètre
    ---------
    taille : int
        Dimension du plateau de jeu

    Retour
    ------
    l : list
        Liste contenant la taille des bateaux présent dans la grille.
    """
    l = []  # Création d'une liste vide
    n = taille - 1  # Affectation de la taille du premier bateau à n
    while n > 1:
        l.append(n)  # Ajout de la taille dans la liste l
        n -= 1  # On diminue de 1 la grille jusqu'à atteindre un bateau de 2

    return l


def coulé(tab: list, taille: int, coulé: int, Liste_bateau: list) -> tuple:
    """
    Cette fonction a pour but de compté le nombre de bateaux coulé

    Paramètres
    ----------
    tab : liste
        Plateau de jeu
    taille : int
        Dimension du plateau
    coulé : int
        Nombre de bateau déjà coulé
    liste_bateau : list
        Liste contenant le nombre de bateau de plateau de jeu

    Retour
    ------
    (coulé, liste_bateau) : tuple
        Tuple composé d'un entié coulé et de la liste des bateaux restant
    """
    # Si on ne connait pas la liste
    if Liste_bateau == None:
        # On appelle la fonction liste_bateau qui crée la liste
        Liste_bateau = liste_bateau(taille)
        # On parcourt la liste des bateaux
        for n in Liste_bateau:
            # On vérifie si le bateau a été coulé ...
            if comptage_touché(tab, n, coulé) == coulé + 1:
                coulé += 1  # ... et on incrémente la variable coulé
                # On retire le bateau coulé de la liste des bateaux
                Liste_bateau.remove(n)
    # Si on connait déjà la liste
    else:
        # On parcourt la liste des bateaux
        for n in Liste_bateau:
            # On verifie que le bateau a été coulé ...
            if comptage_touché(tab, n, coulé) == coulé + 1:
                coulé += 1   # ... et on incrémente la variable coulé
                # On retire le bateau coulé de la liste des bateaux
                Liste_bateau.remove(n)

    return (coulé, Liste_bateau)  # On retourne un tuple contenant


def comptage_touché(tab: list, n: int, coulé: int):
    """
    Cette fonction a pour but de compter le nombre de case touché pour chaque
    bateau et d'affiché coulé quand un bateau est coulé. Elle prend en argument
    la liste dans laquelle elle va compter le nombre de cases touché pour un
    bateau de taille n choisi et retourner le nombre de bateaux coulés.

    Paramètres
    ----------
    tab : list
        Liste correspondant au plateau de jeu dans lequel est compté le nombre
        de bateaux coulés
    n : int
        Entier correspondant à la taille du bateau
    coulé : int
        Nombre de bateaux déjà coulés avant le comptage

    Retour
    ------
    coulé : int
        Nombre de bateaux coulés après le comptage
    """
    nb_touché = 0  # On crée une variable du nombre de bateau touché égale à 1
    # On parcour chaque ligne et chaque colonne du tableau grâce à deux boucles
    for ligne in range(len(tab)):
        for colonne in range(len(tab[ligne])):
            # Dans le case où la case est un mutliple de 10 ...
            if tab[ligne][colonne] == n * 10:
                nb_touché += 1  # ... on incrémente la variable nb_touché
    # S'il y a autant de bateau touché que le nombre de case du bateau ...
    if nb_touché == n:
        print("Coulé !")
        coulé += 1  # On affiche coulé et on incrémente la variable coulé

    return coulé


def placement_auto(tab: list, taille: int, n: int) -> list:
    """
    Cette fonction a pour de placer tous les bateaux de l'adversaire dans sa
    grille en faisant appel à la fonction place_bateau_auto. Elle prend comme
    arguments le plateau de jeu, la dimension du plateau et la taille du
    premier bateau à placer. La fonction renvoit ensuite le plateau de jeu avec
    tous les bateaux placés.

    Paramètres
    ----------
    tab : list
        Plateau de jeu
    taille : int
        Dimension du plateau de jeu
    n : int
        Taille du premier bateau à placer

    Retour
    ------
    tab : liste
        Plateau de jeu avec les bateaux placés
    """
    # On place tous les bateaux du plus grand au plus petit jusqu'au bateau de
    while n > 1:  # taille 2 cases
        # On appelle la fonction place_bateau_auto pour placer chaque bateau
        place_bateau_auto(tab, taille, n)
        n -= 1  # On réduit n de 1 pour placer le bateau de taille inférieur
    return tab


def placement_manuel(tab: list, taille: int, n: int):
    """
    Cette fonction a pour de placer tous nos bateaux dans notre grille en
    faisant appel à la fonction place_bateau_manuel. Elle prend comme arguments
    le plateau de jeu, la dimension du plateau et la taille du premier bateau à
    placer. La fonction renvoit ensuite le plateau de jeu avec tous les bateaux
    placés.

    Paramètres
    ----------
    tab : list
        Plateau de jeu
    taille : int
        Dimension du plateau de jeu
    n : int
        Taille du premier bateau à placer

    Retour
    ------
    tab : liste
        Plateau de jeu avec les bateaux placés
    """
    # On place tous les bateaux du plus grand au plus petit jusqu'au bateau de
    while n > 1:  # taille 2 cases
        print("Placement du bateau de taille ", n)
        # On appelle la fonction place_bateau_auto pour placer chaque bateau
        place_bateau_manuel(tab, taille, n)
        n -= 1  # On réduit n de 1 pour placer le bateau de taille inférieur
    return tab


def remplissage_nous(taille: int, tab: list) -> list:
    """
    Cette fonction a pour but de remplir notre grille de façon choisi selon
    la taille donnée en argument précédemment en faisant appel à la fonction
    placement_manuel. Elle renvoit une liste avec les bateaux placés en
    fonction de la dimension du plateau de jeu.

    Paramètres
    ----------
    taille : int
        Dimension du plateau de jeu
    tab : list
        Plateau de jeu vide

    Retour
    ------
    tab : list
        Plateau de jeu avec les bateaux placés selon la taille de la grille
    """
    # La largeur et la longeur du plateau sont de 5 par 5
    if taille == 5:
        # On appelle la fonction placement_manuelle pour placer les bateaux
        tab = placement_manuel(tab, taille, 4)
    # La largeur et la longeur du plateau sont de 6 par 6
    elif taille == 6:
        # On appelle la fonction placement_manuelle pour placer les bateaux
        tab = placement_manuel(tab, taille, 5)
    # La largeur et la longeur du plateau sont de 7 par 7
    elif taille == 7:
        # On appelle la fonction placement_manuelle pour placer les bateaux
        tab = placement_manuel(tab, taille, 6)
    # La largeur et la longeur du plateau sont de 8 par 8
    elif taille == 8:
        # On appelle la fonction placement_manuelle pour placer les bateaux
        tab = placement_manuel(tab, taille, 7)
    # La largeur et la longeur du plateau sont de 9 par 9
    else:
        # On appelle la fonction placement_manuelle pour placer les bateaux
        tab = placement_manuel(tab, taille, 8)

    return tab


def remplissage_com(taille: int, tab: list) -> list:
    """
    Cette fonction a pour but de remplir la grille de l'adversaire selon
    la taille du plateau donnée en argument précédemment en faisant appel à la
    fonction placement_auto. Elle renvoit une liste avec les bateaux placés en
    fonction de la dimension du plateau de jeu.

    Paramètres
    ----------
    taille : int
        Dimension du plateau de jeu
    tab : list
        Plateau de jeu vide

    Retour
    ------
    tab : list
        Plateau de jeu avec les bateaux placés selon la taille de la grille
    """
    # La largeur et la longeur du plateau sont de 5 par 5
    if taille == 5:
        # On appelle la fonction placement_auto pour placer les bateaux
        tab = placement_auto(tab, taille, 4)
    # La largeur et la longeur du plateau sont de 6 par 6
    elif taille == 6:
        # On appelle la fonction placement_auto pour placer les bateaux
        tab = placement_auto(tab, taille, 5)
    # La largeur et la longeur du plateau sont de 7 par 7
    elif taille == 7:
        # On appelle la fonction placement_auto pour placer les bateaux
        tab = placement_auto(tab, taille, 6)
    # La largeur et la longeur du plateau sont de 8 par 8
    elif taille == 8:
        # On appelle la fonction placement_auto pour placer les bateaux
        tab = placement_auto(tab, taille, 7)
    # La largeur et la longeur du plateau sont de 9 par 9
    else:
        # On appelle la fonction placement_auto pour placer les bateaux
        tab = placement_auto(tab, taille, 8)

    return tab


def affichage_tableau(tab: list):
    """
    Cette fonction a pour but d'afficher le plateau de jeu, donné sous forme de
    liste de liste, ligne par ligne les unes en dessous des autres.

    Paramètre
    ---------
    tab : list
        Plateau de jeu

    Retour
    ------
    None
    """
    for ligne in tab:  # On parcourt les lignes du tableau ...
        print(ligne)  # ... et on les affiche.


def affichage(tab: list, taille: int) -> list:
    """

    Cette fonction nous permet de remplacer les cases touchées par un "X" et
    les à l'eau par des "-". Les cases non visées sont affichés par "0". Elle
    fonctionne avec l'aide d'un cache qui dévoile "X" ou "-" dès que l'on vise
    la case.

    Paramètres
    ---------
    tab : list
        Plateau de jeu de l'ordinateur
    taille : int
        Dimension du plateau

    Retour
    ------
    cache : list
        Plateau de jeu codé
    """
    # On parcourt la table case par case pour détecter les bateaux touchés
    cache = []  # On crée une liste vide dans la variable cache
    # On parcours taille fois la boucle
    for ligne in range(taille):
        cache_ligne = []  # On crée une liste vide dans la variable cache_ligne
        # On parcours taille fois la boucle
        for colonne in range(taille):
            # Dans la case on met la valeur du codage de la grille de l'ordi
            case = tab[ligne][colonne]
            # Si la case est codée supérieur à 9 ...
            if case > 9:
                cache_ligne.append("X")  # On ajoute à la liste cache_ligne "X"
            # Si la case est codée 1
            elif case == 1:
                cache_ligne.append("-")  # On ajoute à la liste cache_ligne "-"
            # Si la case est codée autrement ...
            else:
                cache_ligne.append("0")  # On ajoute à la liste cache_ligne "0"
        # On ajoute à la liste principale les lignes de cache_ligne
        cache.append(cache_ligne)

    return cache


def main():
    """ Fonction principale """
    start = "start"  # On affecte la chaine de caractère "start" à la variable
    while start == "start":  # start pour faire tourner la boucle de jeu

        nom = input("Veuillez entrer votre pseudo: ")
        # On appelle la fonction taille_grille pour coisir la taille du plateau
        taille = taille_grille()
        # On crée les grilles des adversaires
        grille_joueur = creation_tableau(taille)
        grille_com = creation_tableau(taille)
        # Remplissage grille adversaire
        grille_com = remplissage_com(taille, grille_com)
        # Remplissage de notre grille
        grille_joueur = remplissage_nous(taille, grille_joueur)

        # Initialisation des lancés
        coup_1 = 0
        coup_com = 0
        # Initialisation des bateaux coulés
        coulé_1 = 0
        coulé_2 = 0

        # On ne met rien dans les liste_bateau car elles doivent être vide
        # Avant de débuter
        liste_bateau1 = None
        liste_bateau2 = None
        # Tant que ni l'ordinateur ni nous n'ont coulé tous les bateaux
        while (coulé_1 != taille - 2) and (coulé_2 != taille - 2):
            # Affichage des grilles
            print("Grille Joueur")
            affichage_tableau(grille_joueur)
            print("Grille Ordinateur")
            affichage_tableau(affichage(grille_com, taille))

            # On tire dans la grille de l'ordinateur en appelant tir_nous
            grille_com = tir_nous(grille_com)
            # On retiens la valeur de coulé_1 en retenant la valeur coulé de la
            # fonction coulé
            coulé_1 = coulé(grille_com, taille, coulé_1, liste_bateau1)[0]
            # On retiens la liste des bateaux en retenant la valeur
            # liste_bateau de la fonction coulé
            liste_bateau1 = coulé(grille_com, taille, coulé_1, liste_bateau1)[1]
            coup_1 += 1  # On incrémente la variable coup_1
            # L'adversaire tir dans notre grille en appelant tir_com
            grille_joueur = tir_com(grille_joueur, taille)
            # On retiens la valeur de coulé_1 en retenant la valeur coulé de la
            # fonction coulé
            coulé_2 = coulé(grille_joueur, taille, coulé_2, liste_bateau2)[0]
            # On retiens la liste des bateaux en retenant la valeur
            # liste_bateau de la fonction coulé
            liste_bateau2 = coulé(grille_joueur, taille, coulé_2, liste_bateau2)[1]
            coup_com += 1  # On incrémente la variable coup_2

        # On affiche le résultat de la partie
        if coulé_1 > coulé_2:
            print("BRAVO ", nom, ", vous avez gagné en ", coup_1, "coups!")
        elif coulé_1 < coulé_2:
            print("l'adversaire a gagné en ", coup_com, "coups!")
        else:
            print("EGALITE")

        # On décide de rejouer une partie ou d'arêter
        start = input("Entrez 'start' pour rejouer ou 'Entrée' pour quitter")

main()  # Lancement du programme
