print("""HEY TU, FACCIAMO UN BEL GIOCO!
Conosci SASSO, CARTA, FORBICI?
Sono sicuro di sì... """)

punteggio_utente =0
punteggio_computer =0
giri = 0
mossa_utente=''
mossa_segreta = ''


while giri < 3:
    giri += 1
    mossa_utente = int(input("Scegli una mossa: sasso = 1, carta = 2, forbici = 3".strip()))

    import random

    mossa_segreta = random.randint(1, 3)
    if mossa_segreta == 1:
        print("Io ho scelto sasso")
    if mossa_segreta == 2:
        print("Io ho scelto carta")
    if mossa_segreta == 3:
        print("Io ho scelto forbici")

    if ((mossa_segreta == 1 and mossa_utente == 3) or
        (mossa_segreta == 2 and mossa_utente == 1) or
        mossa_segreta == 3 and mossa_utente == 2):
        print("Ah-ah hai perso!")
        punteggio_computer +=1

    elif mossa_segreta == mossa_utente:
        print("Pareggio!")

    else:
        print("Wow hai vinto!")
        punteggio_utente += 1


print ("Fine del gioco!")
if punteggio_utente > punteggio_computer:
    print("Questa volta hai vinto tu... aspetto la rivincita!")
elif punteggio_computer > punteggio_utente:
    print("Hai persooooo!Ah-ah-ah!")
elif punteggio_computer == punteggio_utente:
    print("Wow abbiamo pareggiato!")
print("Alla prossima!")