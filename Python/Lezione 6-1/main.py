# Esercizio 1: Identificare con tre simboli diversi le lettere maiuscole, minuscole ed i caratteri numerici
# * Minuscole
# + Maiuscole
# - Numerie e simboli

stringa = input("Inserisci la tua stringa: ")
soluzione = ""
min,mai,altro = 0,0,0
for i in stringa:
    if "a" <= i <= "z":
        soluzione += "*"
        min += 1
    elif "A" <= i <= "Z":
        soluzione += "+"
        mai += 1
    else:
        soluzione += "-"
        altro += 1
print()
print(stringa)
print(soluzione)
print()
print("Maiuscole totali: " + str(mai) + "\n" +
      "Minuscole totali: " + str(min) + "\n" +
      "Numeri e simboli: " + str(altro))