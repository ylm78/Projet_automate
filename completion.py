from standardisation import *

#Ajoute letat poubelle
def add_P(auto):
    nb_col = len(auto[0])
    nouvelle_ligne = [""] * nb_col
    auto.insert(0, nouvelle_ligne)
    auto[0][1] = 'P'
    auto[0][2] = 'P'
    auto[0][3] = 'P'
    auto[0][0] = 'S'
    return auto


#Remplis les case vide de l'etats poubelle
def fill_empty_cases(auto):
    for i in range(len(auto)):
        for j in range(2, len(auto[i])):
            if not auto[i][j] or str(auto[i][j]) == "..":
                auto[i][j] = 'P'

def completer(auto):
    add_P(auto)
    fill_empty_cases(auto)

