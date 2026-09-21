


#=================================================
#
# digitaler Halthaus 
#
#==========≈=======================================

#veriablen 
wöterbuch = {}



#gehimezahl 
while True :
    gehimezahl = input("was ist deine gehimezahl : ")
    if gehimezahl == "1" :
        print("welkommen Abdallah")
        break
    else :
       print("falsche nummer ")
       
    #Main Menue:
def main_manue () :
    while True :
        print("|__Main Menue__|")     
        print("1 - wöterbuch ")
        print("2 - Neue woter ")
        print("3 - Aufgaben ")
        print("0 - schleißen ")
        auswahl = input("wahl eine Nummer: ")
        if auswahl == "1" :
            print(wöterbuch)
            print("0 - |__Main Menue__|" )
            auswahl2 = input("wahl eine Nummer : ")
            if auswahl2 == "0" :
                print("Ok")
        elif auswahl == "2" :
            wort = input("schreib das woter : ")
            bedeutung = input("schrieb das bedeutung  : ")
            wöterbuch[wort] = bedeutung 
            print("du hast ein neue wort geschrieben✅️ ")
            print("0 - |__Main Menue__|")
            auswahl3 = input("wahl eine Nummer : ")
            if auswahl3 == "0" :
                print("Ok")
        elif auswahl == "3" :
            print("Deutsch lernen ")
            print("Programmieren ")
            print("gesundes Essen ")
            print("0 - |__Main Menue__|" )
            auswahl4 = input("wahl eine Nummer : " )
            if auswahl4 == "0" :
                print("Ok")
        else :
            print("Tschüss")
            break
main_manue()

#===================================================
#
#Namme : Abdallah mohamed 🐱
#von : 20/9/2026
#bis : 21/9/2026
#
#===================================================
         
           
        
