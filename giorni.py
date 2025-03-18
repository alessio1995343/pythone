giorni="lunedì   "+"martedì  "+"mercoledì"+"giovedì  "+"venerdì  "+"sabato   "+"domenica "
giorno = int(input("Indica giorno: "))
p =(giorno - 1) * 9
print (giorni[p],giorni[p+1],giorni[p+2],giorni[p+3],giorni[p+4],giorni[p+5],giorni[p+6],giorni[p+7],giorni[p+8])