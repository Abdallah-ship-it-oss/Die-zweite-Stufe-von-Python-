#===========================
#
#Digetaler-Haushalt. 
#
#===========================


while True :
	geheimzahl = input("geheimzahl : ")
	if geheimzahl == "1":
		print("Wilkommen Abdallah")
		break
	else :
		print("falsche geheimzahl")
		

# 1 - Hauptmenü ..
vokablen = {}
i = 0

def hauptmenü () :
	while True :
		print("1 - wöterbuch & vokabel_trainer.")
		print("2 - kalorienrichner")
		print("3 - To_Do_liste")
		print("4 - programschleißen")
		
	
		auswahl = input("wahl eine nummer : ")
		
		#1 - wöterbuch & vokabel_trainer.
		while True :
			if auswahl == "1" :
				print("1 - wöterbuch.")
				print("2 - neue vokabel")
				print("3 - Vokabel trainer.")
							
				auswahl2 = input("wahl eine nummer : ")
			if auswahl2 == "1" :
				print(vokablen)
				print("0 - schleißen.")
				i = input("")
				break
					
			elif auswahl2 == "2" :
				wort = 												input("Das wort mit Deutsch : ")
				bedeutung = input("Das wort mit Arabisch : ")
				vokablen[wort] = bedeutung
				print("Das wort wurde gespeichert")
			else :
				break
			
						

hauptmenü () 						
								



