def bubblesort(a):
    for i in range(len(a) - 1):
        if type(a[i]) == float or type(a[i]) == int:
            if type(a[i + 1]) == str:
                a[i], a[i + 1] = a[i + 1], a[i]
                bubblesort(a)
            elif a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                bubblesort(a)
        elif type(a[i + 1]) == str and len(a[i]) < len(a[i+1]):
            a[i], a[i + 1] = a[i + 1], a[i]
            bubblesort(a)


a = ["ciao", 1, "al", "caa", 3.5, "ciaoo", 3.26, "aldovino", "cia"]
bubblesort(a)
print(a[::-1])
