import re
from function import *
from completion import *
from determinisation import *

#creer une nouvelle ligne dans le tableau et met letat i
def add_i(auto):
    nb_col = len(auto[0])
    nouvelle_ligne = [""] * nb_col
    auto.insert(0, nouvelle_ligne)
    auto[0][1] = 'i'
    return auto






#ajoute les etats a i

def add_state_i(auto, i):
    for j in range(2, len(auto[0])):
            if auto[0][j]:
                auto[0][j] = auto[0][j] + "," + auto[i][j]
            else:
                auto[0][j] = auto[0][j] + auto[i][j]




#enleve toute les entrer et le met a i:
def remove_enter(auto):
    for i in range(1, len(auto)):
        if auto[i][0] == "E/S":
            add_state_i(auto, i)
            auto[i][0] = 'S'
        elif (auto[i][0] == "E"):
            add_state_i(auto, i)
            auto[i][0] = ' '
    auto[0][0] = "E"



    #appelle a toute les fonctions necessaire pour standardiser
def standardiser (auto):
    add_i(auto)
    remove_enter(auto)