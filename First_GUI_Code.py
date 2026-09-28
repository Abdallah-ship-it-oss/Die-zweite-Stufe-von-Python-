
#============================================
#
#Das ist mein Grüße projekt für Ausbildung 🤍
# ich bin Abdallah und ich mache diesen programmcode für meine Ausbildung.
#Datum :-
#Von : 24/9/2026.
#bis : 
#Autor: Abdallah mohamed 🐱
#
#============================================

import tkinter as tk

#===================
word_book = {}
Workout = []
#===================

window = tk.Tk()
window.title("mein projekt 🤍")
window.geometry("400x500")

#===========================================
# Abdallah'z main menu ➿️
#===========================================

title = tk.Label(window, text="Main Menu", font=("Arial", 18, "bold"))
title.pack(pady=20)
#=====================================================================
# Codes ✅️
#=====================================================================

def add_word():
    add_window = tk.Toplevel(window)
    add_window.title("Add new German word")
    add_window.geometry("350x280")
    
    tk.Label(add_window, text="German word:").pack(pady=5)
    entry_de = tk.Entry(add_window, width=30)
    entry_de.pack(pady=5)
    
    tk.Label(add_window, text="Arabic word:").pack(pady=5)
    entry_ar = tk.Entry(add_window, width=30)
    entry_ar.pack(pady=5)
    
    message_label = tk.Label(add_window, text="", fg="red")
    message_label.pack(pady=5)
    
    def save_word():
        german = entry_de.get().strip()
        arabic = entry_ar.get().strip()
        
        if not german or not arabic:
            message_label.config(text="⚠ Please fill both fields!")
            return
        
        word_book[german] = arabic
        
        with open("word_book.txt", "a", encoding="utf-8") as file:
            file.write(f"{german}:{arabic}\n")
        
        add_window.destroy()
    
    tk.Button(add_window, text="Save", width=15,
              command=save_word).pack(pady=10)
    tk.Button(add_window, text="Cancel", width=15,
              command=add_window.destroy).pack(pady=5)
    
#================================================================

def add_workout():
    add_window2 = tk.Toplevel(window)
    add_window2.title("Add new Workout")
    add_window2.geometry("350x280")

    tk.Label(add_window2 ,text="Put your new Workout : ").pack(pady=5)
    entry_wo = tk.Entry(add_window2 ,width=30)
    entry_wo.pack(pady=5)
    
    message_label = tk.Label(add_window2, text="", fg="red")
    message_label.pack(pady=5)   
    
    def save_workout():
        workout1 = entry_wo.get().strip()

        if not workout1 :
            message_label.config(text="⚠ Please fill the field!") 
            return 
        with open("workout.txt" ,"a" ,encoding ="utf-8") as file :
            workout.append(workout1)
            file.write(f"{Workout1}\n")   
            
        add_window2.destroy()
        
    tk.Button(add_window2 ,text="Save" ,width=15 ,command =save_workout).pack(pady=5)
    tk.Button(add_window2 ,text="Cancel" ,width=15 ,command=add_window2.destroy).pack(pady=5)

#================================================================
# Buttons ✅️
#================================================================
but1 = tk.Button(window, text="1 - Add new German word.",
                 width=30, command=add_word)
but1.pack(pady=5)

but2 = tk.Button(window, text="2 - Add new Workout.", width=30 ,command=add_workout)
but2.pack(pady=5)

but3 = tk.Button(window, text="3 - German words test.", width=30)
but3.pack(pady=5)

but4 = tk.Button(window, text="4 - Show all data.", width=30)
but4.pack(pady=5)

but5 = tk.Button(window, text="5 - Close App.",
                 width=30, command=window.destroy)
but5.pack(pady=5)

window.mainloop()

        add_window.destroy()  
    
tk.Button(add_window ,text = "save" ,width = 15 ,command = save_word).pack(pady = 10)
tk.Button(add_window ,text = "Cancel" ,width = 15 ,command = add_window.destroy).pack(pady = 5)

  
  
but1 = tk.Button(window ,text ="1 - Add new German word. " ,width = 30 ,command = add_word)
but1.pack(pady = 5)


but2 = tk.Button(window ,text ="2 - Add new Workout. " ,width = 30 )
but2.pack(pady = 5)


but3 = tk.Button(window ,text ="3 - German words test. " ,width = 30 )
but3.pack(pady = 5)


but4 = tk.Button(window ,text ="4 - show all data. " ,width = 30 )
but4.pack(pady = 5)


but5 = tk.Button(window, text ="5 - Close App . " ,width = 30 ,command = window.destroy)
but5.pack(pady = 5)







window.mainloop()
