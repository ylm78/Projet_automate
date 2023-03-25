from standardisation import *
from completion import *
from completion import completer




#Fais une liste de toute les entree de lautomates
def get_input_symbols(auto):
    entrer = []
    for i in range(0, len(auto)):
        if auto[i][0] == "E" or auto[i][0] == "E/S":
            entrer.append(auto[i][1])
    return entrer

#creer un nouveau tableau deter pour pouvoir commencencer lalgorithme de determinisation ensuite.
def new_tab(auto):
    if check_complet(auto, "noprint") == 0:
        completer(auto)
    deter = [[".."] * len(auto[0])]
    deter[0][0] = "E"
    inputs = get_input_symbols(auto)
    print(inputs)
    deter[0][1] = ",".join([str(x) for x in inputs])
    print(deter)
    return deter




#Pour lancer la premiere etape de la determinisation
def add_outputs_first_line(auto, deter):
    etats = deter[0][1].split(",")
    for i in range(len(etats)):
        for j in range(0, len(auto)):
            if str(auto[j][1]) == etats[i]:
                for n in range(2, len(auto[0])):
                    if  deter[0][n] == "..":
                        deter[0][n] = auto[j][n]
                    elif deter[0][n]:
                        deter[0][n] = deter[0][n] + "," + auto[j][n]
                    else:
                        deter[0][n] = deter[0][n] + auto[j][n]
                    deter[0][n] = remove_duplicates(deter[0][n])
    if check_numbers_in_string(recup_all_exit(auto), str(deter[0][1])) == 1:
        deter[len(deter) - 1][0] = "E/S"
    return add_outputs_other_line(auto, deter)





#Test si deux case on une combinaison identique pour eviter les doublons dans les etats du tableau
def test_combinaison_identique(case1, case2):
    liste1 = case1.split(",")
    liste2 = case2.split(",")
    liste1 = sorted(liste1)
    liste2 = sorted(liste2)
    return liste1 == liste2




#Test si une combinaison detat existe deja dans le tableau (pour eviter les doublons)
def test_combinaison_identique_col(case1, deter):
    for i in range(1, len(deter)):
        if (test_combinaison_identique(case1, deter[i][1]) == 1):
                return 0
    return 1





#Enlever les doublons d'une chaine de caractere (par exemple 0,0,P,P = 0,P)
def remove_duplicates(string):
    # On transforme la chaîne de caractères en liste de nombres
    lst = list(map(str, string.split(",")))
    # On supprime les doublons en utilisant un ensemble
    unique_lst = list(set(lst))
    # On trie la liste pour avoir un ordre croissant
    unique_lst.sort()
    # On transforme la liste en chaîne de caractères
    unique_str = ",".join(map(str, unique_lst))
    return unique_str





#recuper toute les sortie de lautomate
def recup_all_exit(auto):
    exit = ""
    for i in range(len(auto)):
        if auto[i][0] == "S" or auto[i][0] == "E/S":
            if exit:
                exit = exit + "," + str(auto[i][1])
            else:
                exit = exit + str(auto[i][1])
    return exit


#Regarder si lun des etats que lon a est une sortie ou pas
def check_numbers_in_string(string, numbers):
    # Convertir la chaîne de caractères en liste de nombres entiers
    lst = list(map(str, string.split(",")))

    # Vérifier si chaque nombre est présent dans la liste
    for num in numbers:
        if str (num) in lst and str(num) != ",":
            return True

    # Si aucun des nombres n'est présent dans la liste, retourner False
    return False


#Determinisation
def add_outputs_other_line(auto, deter):
    # Pour chaque ligne de deter
    t = 0
    while t < len(deter):
        # Pour chaque colonne (sauf la première qui contient les états) de deter
        for i in range(2, len(deter[0])):
            # Si la combinaison de sorties de la colonne courante n'est pas déjà présente dans deter
            if (test_combinaison_identique_col(deter[t][i], deter) == 1):
                # Ajouter une nouvelle ligne à deter avec la combinaison de sorties de la colonne courante
                deter.insert(len(deter),  [".."] * len(deter[0]))
                deter[len(deter) - 1][1] = str(deter[t][i])
                deter[len(deter) - 1][0] = " "
                # Si la combinaison de sorties de la colonne courante correspond à une sortie finale de l'automate
                if check_numbers_in_string(recup_all_exit(auto), str(deter[t][i])) == 1:
                    deter[len(deter) - 1][0] = "S"

                # Pour chaque transition de la colonne courante
                for j in range(2, len(deter[0])):
                    transition = deter[t][j].split(",")

                    # Pour chaque état de la transition courante
                    for y in range(len(transition)):
                        # Pour chaque ligne de l'automate
                        for l in range(len(auto)):
                            # Si l'état de la transition courante correspond à un état de l'automate
                            if transition[y] == str(auto[l][1]):
                                # Ajouter les transitions de l'état correspondant à la nouvelle ligne de deter
                                for n in range(2, len(auto[0])):
                                    if deter[len(deter) - 1][j] == "..":
                                        deter[len(deter) - 1][j] = str(auto[l][n])
                                    elif deter[len(deter) - 1][j]:
                                        deter[len(deter) - 1][j] = deter[len(deter) - 1][j] + "," + str(auto[l][n])
                                    else:
                                        deter[len(deter) - 1][j] = deter[len(deter) - 1][j] + str(auto[l][n])
                                    # Supprimer les doublons dans les transitions de la nouvelle ligne
                                    deter[len(deter) - 1][j] = remove_duplicates(deter[len(deter) - 1][j])
    # Retourner le tableau déterministe avec les nouvelles sorties ajoutées
        t += 1
    return deter



def determiniser(auto):
    deter = new_tab(auto)
    deter = add_outputs_first_line(auto, deter)
    return deter


