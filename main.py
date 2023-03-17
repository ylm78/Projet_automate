from function import *

f = open('R7-4.txt')
fichier = get_next_line(f)
remove_n(fichier)
print(fichier)
f.close()

auto=[[]]

for i in range(0, int(fichier[1])):
     for j in range(0,int(fichier[0]) + 2):
          if es_or_not(j,fichier[2],fichier[3] and es_or_not(j,fichier[4],fichier[5])):
               fichier[i].append("ES")
          elif (es_or_not(j,fichier[2],fichier[3])):
               fichier[i].append("E")
          elif (es_or_not(j,fichier[4],fichier[5])):
               fichier[i].append("S")
          else:
               fichier[i] = -1