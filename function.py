#Fonction qui vérifie si un état est une entrée ou une sortie
def es_or_not(val, nb_init, nb_term, init, term):
    result = []
    for i in range(0, nb_init):
        if val == init[i]:
            result.append("E")
    for j in range(0, nb_term):
        if val == term[j]:
            result.append("S")
    return result

def es_or_not(val,nb_init_term,init_term):
    for i in range(0, nb_init_term):
        if val == init_term[i]:
            return 1
    return 0


def get_next_line(f):
    fichier = f.readlines()
    return fichier

def remove_n(fichier):
    count = 0
    while (count < len(fichier)):
        fichier[count] = fichier[count].replace('\n', '')
        count += 1

