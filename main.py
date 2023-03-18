from function import *
import pandas as pd
import string
import wx
import wx.grid

f = open('file.txt')
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












# Affiche proprement lautomate dans une fenetre graphique grace a wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Automate : " + str(fichier[0]) + " états", size=(500, 300))
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


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()



