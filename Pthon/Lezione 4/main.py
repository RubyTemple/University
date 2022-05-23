# Esercizio: Disegnare il perimetro e l'area del rettangolo

def draw(perimetro):
    for i in range(altezza):
        for j in range(lunghezza):
            if perimetro:
                if i == 0 or i == altezza - 1:
                    print("*", end="")
                else:
                    if j == lunghezza - 1 or j == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
            else:
                print("*", end="")
        print()


altezza = int(input("Inserisci l'altezza del rettangolo: "))
lunghezza = int(input("Inserisci la lunghezza del rettangolo: "))
perimetro = int(input("Vuoi che ti venga mostrato il perimetro (0 false, 1 true): "))
perimetro = (perimetro == 1)
print("\nEcco il tuo rettangolo: \n")
draw(perimetro)
