import re
import pandas as pd
import string

#Va regarder sil ny a que un seul etat terminaux ou initial
def manage_file(fichier):
    fichier[0] = int(fichier[0])
    fichier[1] = int(fichier[1])
    fichier[2] = int(fichier[2])
    if (len(fichier[3]) == 1):
        fichier[3] = int(fichier[3])
    else:
        fichier[3] = extract_numbers(fichier[3])
    fichier[4] = int(fichier[4])
    if (len(fichier[5]) == 1):
        fichier[5] = int(fichier[5])
    else:
        fichier[5] = extract_numbers(fichier[5])

#remplis un tableau automate avec les informations du fichiers (sans les transitions)
def fill_file(fichier):
    auto = [[".."] * (fichier[0] + 2) for i in range(fichier[1])]

    for i in range(0, fichier[1]):
        auto[i][1] = i
        if es_or_not(i, fichier[2], fichier[3]) and es_or_not(i, fichier[4], fichier[5]):
            auto[i][0] = "E/S"
        elif es_or_not(i, fichier[2], fichier[3]):
            auto[i][0] = "E"
        elif es_or_not(i, fichier[4], fichier[5]):
            auto[i][0] = "S"
        else:
            auto[i][0] = " "
    return auto



    #Determine si un etat est initiaux ou terminal
def es_or_not(val, nb_init_term, init_term):
    if (nb_init_term == 1):
         return val == init_term
    if isinstance(init_term, list):
        return val in init_term
    init_term_list = [int(x) for x in init_term.split()]
    return val in init_term_list


def extract_numbers(s):
    pattern = r'\d+'
    numbers = re.findall(pattern, s)
    numbers = [int(n) for n in numbers]
    return numbers




    #recupere le fichier
def get_next_line(f):
    fichier = f.readlines()
    return fichier




    #Enleve les "\n" du fichier
def remove_n(fichier):
    count = 0
    while (count < len(fichier)):
        fichier[count] = fichier[count].replace('\n', '')
        count += 1




    #rajoute les transtions au tableau (exemple : 0a1)
def add_transition(tab, s):
    row = int(s[0])
    col = ord(s[1]) - ord('a') + 2
    val = s[2]
    if tab[row][col] != "..":
        tab[row][col] = tab[row][col] + val
    else :
        tab[row][col] = val





#Ajoute toutes les transitions du fichiers au tableau de lautomate

def add_all_transition(auto, fichier):
    for i in range(6, len(fichier)):
        add_transition(auto, fichier[i])




    #Check si il ny a pas de transition vide
def check_transition_vide(tab):
    for i in range(2, len(tab[0])):
        for j in range(0, len(tab)):
            if (tab[j][i] == ".."):
                return False
    return True




    #Check s'il y a bien une entre et une sortie
def check_exit_and_entry(tab):
    check_entrance = 0
    check_exit = 0
    for j in range(0,len(tab)):
        if (tab[j][0] == "E/S"):
            check_entrance = 1
            check_exit = 1
        elif  (tab[j][0] == "S"):
            check_exit = 1
        elif  (tab[j][0] == "E"):
            check_entrance = 1
    if check_exit * check_entrance == 0:
        return False
    return True




# Vérifier que toutes les transitions sont valides (i.e. un état valide vers un état valide)
def check_each_transition(tab):
    etats = [row[1] for row in tab[0:]]
    for i in range(0, len(tab)):
        for j in range(1, len(tab[i])):
            transition = str(tab[0][j]) + str(tab[i][1]) + str(tab[i][j])
            if len(transition) > 2:
                for k in range(0, len(transition) - 1):
                    if not (transition[k:k + 2].isdigit() and int(transition[k]) in etats and int(
                            transition[k + 1]) in etats):
                        return False
            elif transition.isdigit() and int(transition[0]) in etats and int(transition[1]) in etats:
                continue
            else:
                return False
    return True






    #Check si l'automate est complet (pas d'etats vide, une entre, une sortie, toutes les transitions sont valide)
def check_complet(tab):
    return (check_each_transition(tab) and check_transition_vide(tab) and check_exit_and_entry(tab)) == 1




    #Check s'il y a une seule entree dans lautomate
def check_unique_entry(tab):
    nb_entry = 0
    for i in range(0, len(tab)):
        if (tab[i][0] == "E/S"):
            nb_entry += 1
        if (tab[i][0] == "E"):
            nb_entry += 1
    if (nb_entry != 1):
        return (False)
    return (True)





#Trouver la valeur de la premiere entree
def find_value_entry(tab):
        for i in range(0, len(tab)):
            if (tab[i][0] == "E/S" or tab[i][0] == "E"):
                return tab[i][1]



#vérifie que chaque caractère d'une chaîne de caractères est différent d'une valeur donnée
def check_characters(string, value):
    for char in string:
        if char == value:
            return True
    return False


    #Check si lautomate a une transition pour revenir a lentre
def check_returnto_entry(tab):
    value_entry = find_value_entry(tab)
    for i in range(0, len(tab)):
        for j in range(2, len(tab[0])):
            if (check_characters(tab[i][j], str(value_entry))) == 1:
                return False
    return True



    #Check si lautomate est standard (une seule entree et aucune transition qui reviens a lentree)
def check_standard(tab):
    val = 1
    if check_each_transition(tab) == 0:
        print("Lautomate a des transitions qui n'hesite pas")
        val = 0
    if check_unique_entry(tab) == 0:
         print("Lautomate n'a pas que une seule entree")
         val = 0
    if check_returnto_entry(tab) == 0:
         print("Lautomate a une transition qui retourne a lentree")
         val = 0
    return val

#check si lautomate a une transition possible sur deux etats differents
def check_double_arrow(tab):
    for i in range(0, len(tab)):
        for j in range(2, len(tab[0])):
            if (len(tab[i][j]) > 1):
                return False
    return True

#Check si lautomate est deterministe (chaque transition est possible, une seule entree, pas de transition possible sur deux etats)
def check_deterministe(tab):
    val = 1
    if check_each_transition(tab) == 0:
        print("Lautomate a des transitions qui n'hesite pas")
        val = 0
    if check_unique_entry(tab) == 0:
         print("Lautomate n'a pas que une seule entree")
         val = 0
    if check_double_arrow(tab) == 0:
         print("Lautomate a un etats d'ou sort plus d'une fleche libelle par un meme caractere")
         val = 0
    return val



#Affiche toute les informations sur lautomates (standard, complet, deterministe)
def print_info(auto):
    if (check_standard(auto)):
        print("L'affichage est standard")
    else:
        print("L'affichage n'est pas standard")
    if (check_complet(auto)):
        print("L'affichage est complet")
    else:
        print("L'affichage n'est pas complet")
    if (check_deterministe(auto)):
        print("L'affichage est deterministe")
    else:
        print("L'affichage n'est pas deterministe")


#Affiche lautomate proprement dans le terminal grace a pandas
def print_pandas(auto):
    df = pd.DataFrame(auto)
    letters = [' '] + list(string.ascii_lowercase)[:len(df.columns) - 2]
    df = df.set_axis([''] + letters, axis='columns')
    print(df.to_string(index=False))








