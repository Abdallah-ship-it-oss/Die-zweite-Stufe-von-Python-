
#============================================
#
#mwin Grüße projekt für Ausbildung 🤍
# ich bin Abdallah und ich mache diesen programmcode für meine Ausbildung.
#Datum : 24/9/2026.
#
#============================================

import random


word_book = {}
Workout = []

def main_menu () : 
    while True :
        print("="* 35 )
        print("|_____Main_Menu_____|")
        print("="* 35 )
        print("1 - add new german word")
        print("2 - add new Workout")
        print("3 - German words test ")
        print("4 - show all data ")
        print("5 - close ")
        print("="* 35 )
    
        
        choice = input("chose a Number : ")
        if choice =="1" :
            german_word = input("the word with German :")
            arabic_word = input("the word with Arabic :")
            word_book[german_word] = arabic_word
            with open ("word_book.txt" ,"a" ,encoding = "utf-8") as file :
                file.write(f"{german_word}:{arabic_word}")
                
            print("the word has been saved . " )
            
            
            
        elif choice == "2" :
            new_Workout = input("what's your new Workout : ")
            Workout.append(new_Workout)
            with open ("Workout.txt" , "a" , encoding = "utf-8") as file :
                file.write(f"{new_Workout}")
            print("the Workout has been saved ! ")
            
            
        elif choice == "3" :
            print("we will ad this soon ")
            
            
        elif choice == "4" :
            print("=" * 35 )
            if not word_book :
                print("there's no words yet ! ")
            else :   
                print(word_book)
            print("=" * 35 )
            print("☆" * 35 )
            print("=" * 35 )
            if not Workout :
                print ("there's no Workout yet! ")
            else :
                print(Workout)
            print("=" * 35 )
            
            
        elif choice == "5" :
            print("good bye .")
            break
            
            
        else :
            print("wrong choice !")
 
            
main_menu()           
                    
    