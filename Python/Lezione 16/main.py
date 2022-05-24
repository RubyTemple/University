# Esercizio
# 1: Il bubble-sort, così come lo abbiamo implementato a lezione a partire
# dalla seconda scansione in poi esegue un numero crescente di confronti
# inutili in quanto gli elementi più grandi hanno già raggiunto la loro
# posizione finale nella lista. Modificare l'implementazione evitando
# questi confronti inutili.

count = 0


def bubblesort(a):
    global count
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            print(count, ") ", a)
            count += 1
            bubblesort(a)


a = [1, 2, 9, 5, 17, 1, 9, 10]
print("Passaggi eseguiti dal Bubblesort: ")
bubblesort(a)
print()
print("Ordinato: ",a)
