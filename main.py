from function import *
from standardisation import *
from completion import *
from determinisation import *
import pandas as pd
import string
import wx
import wx.grid


filename = input("Entrez le nom du fichier à ouvrir : ")
try:
    file_number = int(filename.split(".")[0])
except ValueError:
    print("Le nom de fichier n'est pas valide.")
    exit()
if file_number < 1 or file_number > 46:
    print("Le nom de fichier n'est pas valide.")
    exit()

f = open("Automate_test/" + filename + ".txt")

fichier = get_next_line(f)
#Enleve les retours a ligne dans la liste "Fichier"
remove_n(fichier)
f.close()

#Va regarder sil ny a que un seul etat terminaux/ initial (car implique different changement dans la lecture du fichier)
manage_file(fichier)

#remplis un tableau automate avec les informations du fichiers (sans les transitions)
auto = fill_file(fichier)

#Ajoute toutes les transitions du fichiers au tableau de lautomate
add_all_transition(auto, fichier)

#Affiche lautomate proprement dans le terminal grace a pandas
print_pandas(auto)

#Affiche toute les informations sur lautomates (standard, complet, deterministe)
print_info(auto)

import wx

# Définir la classe MyFrame pour l'affichage de la grille
class MyFrame(wx.Frame):
    def __init__(self, auto, fichier):
        wx.Frame.__init__(self, None, title="Automate : " + str(len(auto)) + " états", size=(500, 300))
        panel = wx.Panel(self)
        grid = wx.grid.Grid(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Importer votre tableau avec Pandas
        df = pd.DataFrame(auto)
        # Ajouter les données à la grille
        grid.CreateGrid(df.shape[0], df.shape[1]-1)
        # Ajouter les en-têtes de colonnes
        grid.SetColLabelValue(0, "États")
        for i in range(0, df.shape[1]):
            grid.SetColLabelValue(i + 1, string.ascii_lowercase[i])
        for i in range(0, df.shape[0]):
            grid.SetRowLabelValue(i, str(auto[i][0]))


        for col in range(1, df.shape[1]):
            for row in range(df.shape[0]):
                grid.SetCellValue(row, col-1, str(df.iloc[row, col]))
                # Verrouiller la cellule pour éviter l'édition
                grid.SetReadOnly(row, col-1)

        # Ajouter la grille au sizer
        sizer.Add(grid, 1, wx.EXPAND)
        panel.SetSizer(sizer)


# Créer l'objet wx.App avant la boucle while
app = wx.App()
frame = None
default = 0
while(1):
    print("\n\nQue faire avec l'automate ?")
    if check_standard(auto, "noprint") == 0:
        print("1 : Standardiser")
    if check_complet(auto, "noprint") == 0 :
        print("2 : Completer")
    if check_deterministe(auto, "noprint") == 0:
        print("3 : Determiner")
    if default == 0:
        print("4 : Afficher par defaut")
    print("5 : Information sur automate")
    print("STOP : Met fin au programme")

    do = input("\nSaisir votre choix : ")

    if do == '1' or do == '2' or do == '3' or do == '4' or do == '5' or do == "STOP":
        if do == '1' and check_standard(auto, "noprint") == 0:
            standardiser(auto)
        elif do == '2' and check_complet(auto, "noprint") == 0:
            completer(auto)
        elif do == '3' and  check_deterministe(auto, "noprint") == 0:
            auto = determiniser(auto)
        elif do == "4" :
            print("\n")
        elif do == "STOP":
            exit()
        elif do == "5":
            print_info(auto)
            default = 1
            continue
    else :
        print("Le choix n'est pas valide")

    default = 1
    # Afficher la grille dans une fenêtre wx.Frame
    if not frame:
        frame = MyFrame(auto, fichier)
    else:
        frame.Refresh()
    frame.Show()
    frame.Raise()
    app.MainLoop()
