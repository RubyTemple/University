# Esercizio
# Una tupla numerica annidata o tna è un numero (int o float) oppure una tupla tale che ogni suo elemento è una tna.
#
# Esempio:
#
# t = ( 3.14, (2,3), (2.71, (7, 5)), 9, (12, ( 4, )) )
#
# è una tna in quanto t è una tupla contenente 3.14 che è un numero, (2,3) che è una tna in quanto la tupla (2,3) a sua volta contiene due numeri che sono tna...
#
# Scrivere una funzione, chiamata conta_elem_tna(), che prende in input una tna e restituisce il numero totale di float ed int dentro la tna.
#
# Ad esempio se t è la tna definita sopra
#
# conta_elem_tna(t)
#
# deve ritornare 9

# global
conta = 0

def contatuple(tupla):
    global conta
    for i in tupla:
        if type(i) == tuple:
            contatuple(i) # recursive call
        else:
            conta += 1
    return conta


tupla = (3.14, (2, 3), (2.71, (7, 5)), 9, (12, (4,)))
# print(t[1])
print("Gli elementi della tupla sono: ", contatuple(tupla))
