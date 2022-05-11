import PySimpleGUI as sg
import random
import time


spelare=[ ]
dealer=[ ]
kortsiffra=(11,2,3,4,5,6,7,8,9,10)
kortfarg=("♥","♦","♣","♠")
vardtio=("J","Q","K",10)
raknare=0
bet=int(0)
spelarepoang=int(0)
dealerpoang=int(0)
kort=int(0)
pengar=int(100)
raknare2=1

def blackjack():
    def dealergiv():
        global dealerpoang
        kort=randomkort()
        tiorand=randomtio()
        for x in kortsiffra:
            if x == kort:
                if x == 11:
                    dealer.append("A")
                elif x == 10:
                    dealer.append(tiorand)
                else:
                    dealer.append(kort)
                dealerpoang+=kort

    def spelargiv():
        global spelarepoang
        kort=randomkort()
        tiorand=randomtio()
        for x in kortsiffra:
            if x == kort:
                if x == 11:
                    spelare.append("A")
                elif x == 10:
                    spelare.append(tiorand)
                else:
                    spelare.append(kort)
                spelarepoang+=kort

    def randomkort():
        kort=random.choice(kortsiffra)
        return kort
        
    def randomtio():
        tiorand=random.choice(vardtio)
        return tiorand


    layout = [[sg.Text("", key=("-KORT-"), visible=False)], [sg.Text("", key="-KORT2-", visible=False)], [sg.Text("", key="-KORT3-", visible=False)], 
            [sg.Text("", key="-TOTAL-", visible=False),sg.Button("Betta", key="-BETKNAPP-", visible=False), sg.Slider(range=(1, pengar), key="-BETSLIDER-", visible=False)],
            [sg.Text("Vill du spela?", key="-SPELA-")],
            [sg.Button("ja", key="-JA-"), sg.Button("nej", key="-NEJ-")],
            [sg.Button("hit", key="-HIT-", visible=False), sg.Button("stand", key="-STAND-", visible=False)], [sg.Button("Avsluta", key="-AVSLUTA-", visible=False)]]

    window = sg.Window("Mitt lilla fönster", layout) 


    while True:
        event, values = window.read()
        print(event, values)
        if event =="-NEJ-":
            break
        if event == "-JA-":
            window.Element("-SPELA-").Update(visible=False)
            window.Element("-JA-").Update(visible=False)
            window.Element("-NEJ-").Update(visible=False)
            window.Element("-BETSLIDER-").Update(range=(1, pengar), visible=True)
            window.Element("-BETKNAPP-").Update(visible=True)
        if event == "-BETKNAPP-":
            bet=values["-BETSLIDER-"]
            pengar=pengar-bet
            while raknare !=2:
                spelargiv()
                dealergiv()
                raknare+=1 
            window.Element("-BETSLIDER-").Update(visible=False)
            window.Element("-BETKNAPP-").Update(visible=False)
            window.Element("-KORT-").Update(value=spelare[0], visible=True)
            window.Element("-KORT2-").Update(value=spelare[1], visible=True)
            window.Element("-HIT-").Update(visible=True)
            window.Element("-STAND-").Update(visible=True)
            window.Element("-AVSLUTA-").Update(visible=True)
            window.Element("-TOTAL-").Update(visible=True, value=(f"du har just nu {spelarepoang} totalt"))
        if event == "-HIT-":
            spelargiv()
            window.Element("-KORT3-").Update(visible=True)
            window.extend_layout(window["-KORT3-"], [[sg.Text(spelare[-1])]])
            window.Element("-TOTAL-").Update(value=(f"du har just nu {spelarepoang} totalt"))
        if spelarepoang > 21:
            print("Du förlora!")
            spelarepoang=0
            raknare=0
            spelare.clear()
            window.Element("-TOTAL-").Update(value=f"du har just nu {spelarepoang} totalt")
            window.Element("-KORT-").Update(value="", visible=False)
            window.Element("-KORT2-").Update(value="", visible=False)
            window.Element("-KORT3-").Update(value="", visible=False)
            window.close()
            blackjack()
            window.Element("-HIT-").Update(visible=False)
            window.Element("-STAND-").Update(visible=False)
            window.Element("-AVSLUTA-").Update(visible=False)
            window.Element("-TOTAL-").Update(visible=False)
            window.Element("-BETSLIDER-").Update(range=(1, pengar), visible=True)
            window.Element("-BETKNAPP-").Update(visible=True)
            continue
        if event == "-AVSLUTA-":
            break
        
    window.close()

blackjack()
