import tkinter as tk #Importerer ulike bibliotheker
import random
from turtle import*
import time
from tkinter import *

def riktig_svar (nytotale_poeng): #Definerer koden når du svarer riktig
    print("gratulerer, neste oppgave")
    totale_poeng = nytotale_poeng+1 #Gir deg poeng
    print ("totale poeng: ", totale_poeng)
    return totale_poeng #Gir ny poengverdi videre
    

def feil_svar(poeng, highscore, navn, oldhighscorenavn): #Definerer koden når du svarer feil
    print ("Svaret ditt er feil. Kanskje du skrev feil,eller tenkte feil;)")
    if highscore < poeng: #Bestemmer om det blir ny highscore
        print("New highscore!")
        print("New Highscore: ",poeng) #Viser highscoren
        newhighscore = poeng #Setter highscore
        newhighscorenavn = navn #Setter navnet ditt til highscore
        print("Highscoren tilhører: ", newhighscorenavn) #Viser hvem highscoren tilhører
        
    else: #Dette skjer vis det ikke ble ny highscore
        newhighscore = highscore
        print("No new highscore")
        print("Old Highscore: ",highscore) #Viser hvor mye den gamle highscoren er.
        newhighscorenavn = oldhighscorenavn 
        print("Highscoren tilhører" , oldhighscorenavn)
    return newhighscore, newhighscorenavn #Return "gir tilbake" noe


def pause(): #En enkel pausefunskjon
    time.sleep (0.1)

    
def restart(poeng,highscore,highscorenavn): #Selve oppgaven. Alt ligger i en funskjon slik at man kan restarte
    print ("Hei, nå skal vi ha et lite mattespill, lykke til, først. Hva heter du?")
    navn= input() #Lagrer det du skrev inn under variabelen "navn"
    totale_poeng = poeng
    while 1==1: #Denne finnes for at oppgaven skal repetere seg selv helt til du gjør feil.
        tall_a= random.randint(10,20) #Her lager du oppgaven 
        tall_b= random.randint(10,20)
        svar= tall_a + tall_b #programmet lagrer svaret
        oppgave_2=0 #Variabel som bestemmer om oppgave 2 blir riktig eller feil
            

               
        print ("oppgave 1")

        print ("oppgaven din", navn, ":", tall_a, "+", tall_b) #Her for spilleren se oppgaven 

        print ("Hva er svaret?(skriv tall)")

        sammenlign_svar= input() #gir deg et felt der du kan skrive svaret


        try: #Programmet prøver å kjøre denne koden
            sammenlign_svar = int(sammenlign_svar) #forvandler svaret til heltall
        except ValueError: #Om det kræsjer, fortsett med dette istedet (feilsvar())
            highscore, highscorenavn = feil_svar(totale_poeng, highscore, navn, highscorenavn)#En annen funskjon
            totale_poeng = 0
            print ("svaret hadde vært", svar)
            Button(totale_poeng, highscore, highscorenavn) #Funskjonskall

        if sammenlign_svar == svar: #her kommer en klamme som bestemmer om du kommer videre eller ikke 
            totale_poeng = riktig_svar(totale_poeng) #Svarte du riktig hopper maskinen inn i en funskjon lengre oppe

        else: #svarer du feil skjer dette. 
            highscore, highscorenavn = feil_svar(totale_poeng, highscore, navn, highscorenavn)#En annen funskjon
            totale_poeng = 0
            print ("svaret hadde vært", svar)
            Button(totale_poeng, highscore, highscorenavn)
        pause()#Pausefunskjon
            
        print ("oppgave 2")
        pause()    
      

        print ("Er det riktige tallet fra forrige oppgave her? (skriv y/Y eller n/N)") #spørsmålsetning
        pause()

        for i in range (10): #Dette er en løkke som viser forskjellige tall 10 ganger. 
            random_tall = random.randint(20, 40) 
            
            print(random_tall)

            pause()
            
            if random_tall==svar: #Dette er en klamme som angir svaret som må bli funnet i neste avsnitt
                oppgave_2= 1

        riktig_eller_feil=input()


        if (riktig_eller_feil== ("y") or riktig_eller_feil==("Y")) and oppgave_2==1: #Dette er keypoint, vis svaret er ja og oppgaven sier at det er riktig, sier programmet at oppgaven er riktig.
           
            
            totale_poeng = riktig_svar (totale_poeng)
            
        elif (riktig_eller_feil== ("n") or riktig_eller_feil==("N")) and oppgave_2==0: #Litt av det samme her, er svaret nei og oppgaven sier at svaret er feil, svarte du riktig.
            
            
            totale_poeng = riktig_svar (totale_poeng) 

        else: #I alle andre tilfeller så blir det du svarer feil. 
            highscore, highscorenavn = feil_svar(totale_poeng, highscore, navn, highscorenavn)
            totale_poeng = 0
            Button(totale_poeng, highscore, highscorenavn)


  
def Button(poeng,highscore,highscorenavn): #Definerer vinduet somm kommer opp når du skal restarte hele spillet
    print("Dette er desverre ganske komplisert, det vil ha kommet opp en ny fane")
    def restart2():
        root.destroy() #Gjør at vinduet lukker seg
        restart(poeng,highscore,highscorenavn)
    root = tk.Tk() #Innbygget funksjon av tkinter, starter knappen. Resten av funskjonen er kopiert fra internett(https://www.python-course.eu/tkinter_buttons.php)
    frame = tk.Frame(root)#Bygger vinduet
    frame.pack()
    button = tk.Button(frame, 
                       text="QUIT", 
                       fg="blue", #det bestemmer fargen på knappen
                       command=quit) #quit er en kommando som gjør at du går ut 
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="restart",
                        fg="green",
                        command=restart2)
    slogan.pack(side=tk.LEFT)
    pause()
    root.mainloop()
    pause()

restart(0,0,"") #Starter scriptet og setter startverdier til 0 (Poeng, Highscore, higscorenavn) 
