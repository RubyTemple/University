# Esercizio
# Si progetti ed implementi in Python una funzione denominata intersezione
# che prende in input due liste a e b e restituisce una terza lista,
# diciamo c, contenente tutti gli elementi che sono sia in a che in b.
# La lista c non deve avere elementi ripetuti. Dopo aver implementato
# la funzione se ne calcoli il costo computazionale.

# Utilizzando le liste il costo computazionale avrà una complessità di O(n^3)


def intersezione(a, b):  # tot: O(n^3)
    c = []  # O(1)
    for i in a:  # O(n)
        if i in b and i not in c:  # O(n^2)
            c.append(i)  # O(1)
    return c  # O(1)


# Utilizzando i set il costo computazionale avrà una complessità minore poiché
# indicizza utilizzando l'hashing quindi O(n)
def intersezione_2(a, b):  # tot: O(n)
    a = set(a)  # O(n)
    b = set(b)  # O(n)
    c = []  # O(1)
    for i in a:  # O(1)
        if i in b:  # O(1)
            c.append(i)  # O(1)
    return c  # O(1)


a = [1, "ciao", "ciao", 4, 7, "bella"]  # O(1)
b = ["ciao", "niaho", 1, "bella", "ciao"]  # O(1)

print("Intersezione: ", intersezione_2(a, b))  # O(1)
