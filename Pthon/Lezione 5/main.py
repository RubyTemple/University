# Esercizio: Scrivere un programma che chiede in input una stringa e stampa Vero se questa è palindroma, Falso altrimenti.

parola = input("Inserisci la tua stringa: ")
print("La parola è palindroma") if parola[:len(parola)//2] == parola[len(parola)//2 if len(parola)%2==0 else len(parola)//2+1:][::-1] else print("La parola non è palindroma")

