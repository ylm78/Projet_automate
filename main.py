from function import *
import pandas as pd
import string
import matplotlib.pyplot as plt

f = open('file.txt')
fichier = get_next_line(f)
remove_n(fichier)
f.close()

fichier[0] = int(fichier[0])
fichier[1] = int(fichier[1])
fichier[2] = int(fichier[2])
if (len(fichier[3]) == 1 ):
    fichier[3] = int(fichier[3])
else :
    fichier[3] = extract_numbers(fichier[3])
fichier[4] = int(fichier[4])
if (len(fichier[5]) == 1 ):
    fichier[5] = int(fichier[5])
else :
    fichier[5] = extract_numbers(fichier[5])




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



for i in range(6, len(fichier)):
    add_transition(auto, fichier[i])



df = pd.DataFrame(auto)
letters = [' ']+ list(string.ascii_lowercase)[:len(df.columns) - 3]


df = df.set_axis(['']+['']+letters, axis='columns')
print(df.to_string(index=False))

import wx
import wx.grid
import pandas as pd


import wx
import wx.grid
import pandas as pd

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Automate : " + str(fichier[0]) + " états", size=(500, 300))
        panel = wx.Panel(self)
        grid = wx.grid.Grid(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Importer votre tableau avec Pandas
        df = pd.DataFrame(auto)
        # Ajouter les données à la grille
        grid.CreateGrid(df.shape[0], df.shape[1]-2)
        # Ajouter les en-têtes de colonnes
        grid.SetColLabelValue(0, "États")
        for i in range(0, df.shape[1]):
            grid.SetColLabelValue(i + 1, string.ascii_lowercase[i])
        for i in range(0, df.shape[0]):
            grid.SetRowLabelValue(i, str(auto[i][0]))


        for col in range(1, df.shape[1] - 1):
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



