
#============================================
#
#mwin Grüße projekt für Ausbildung 🤍
# ich bin Abdallah und ich mache diesen programmcode für meine Ausbildung.
#Datum : 24/9/2026.
#
#============================================

import tkinter as tk
window = tk.Tk ()
window.title("mein projekt 🤍")
window.geometry("400x500")

# Abdallah'z main manu 📙

title = tk.Label (window ,text ="Main Manu" ,front =("Arial" ,18 ,"bold"))
title.pack(pady = 20)

#Buttons
def add_word():
  print("clicked")
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
