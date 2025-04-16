#scrivere un programma che acquisisca tutte le righe di un file di testo il cui nome va richiesto all'utente. Il file si suppone contenere un numero per ogni riga (anche con decimali). Calcolare la media e indicare il valore massimo comprensivo della riga in cui è stato trovato nel file.

File_name=input("Inserisci il nome del file: ")
i=0
somma=0
max =None
riga_max = 0
daLeggere = open(File_name, "r")
righe = daLeggere.readlines()
for i, riga in enumerate(righe, start=1):
 valore= float(riga.strip())
 somma += valore

 if max is None or valore > max:
    max = valore
    riga_max=i

media = somma / len(righe)

print(f"Media: {media}")
print(f"valore massimo: {max} trovato alla riga {riga_max}")
