# Esercizio
# Implementazione del Merge Sort
from heapq import merge


def mergeSort(lista): #tot = o(n log n)
    if len(lista) <= 1:
        return lista
    else:
        primo = lista[:len(lista) // 2]
        secondo = lista[len(lista) // 2:]
        primo = mergeSort(primo)
        secondo = mergeSort(secondo)
        return list(merge(primo, secondo))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 6, 8, 9, 11, 1, 4]
print(mergeSort(a))
