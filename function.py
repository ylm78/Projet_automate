import re

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

def get_next_line(f):
    fichier = f.readlines()
    return fichier

def remove_n(fichier):
    count = 0
    while (count < len(fichier)):
        fichier[count] = fichier[count].replace('\n', '')
        count += 1

def add_transition(tab, s):
    row = int(s[0])
    col = ord(s[1]) - ord('a') + 2
    val = s[2]
    tab[row][col] = val