
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
import random 

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
            
        Workout.append(workout1)
        
        with open("Workout.txt" ,"a" ,encoding ="utf-8") as file :
            
            file.write(f"{workout1}\n")   
        
        add_window2.destroy()
        
    tk.Button(add_window2 ,text="Save" ,width=15 ,command =save_workout).pack(pady=5)
    tk.Button(add_window2 ,text="Cancel" ,width=15 ,command=add_window2.destroy).pack(pady=5)

#================================================================

def word_test():
    if not word_book:
        error_window = tk.Toplevel(window)
        error_window.title("ERROR")
        error_window.geometry("300x100")
        tk.Label(error_window, text="There are no words yet!",
                 fg="red").pack(pady=20)
        tk.Button(error_window, text="OK",
                  command=error_window.destroy).pack(pady=5)
        return
    
    test_window = tk.Toplevel(window)
    test_window.title("German Words Test")
    test_window.geometry("400x400")
    
    random_key = ""
    correct_answer = ""
    score_correct = 0
    score_wrong = 0
    
    tk.Label(test_window, text="Translate this word:",
             font=("Arial", 12)).pack(pady=10)
    
    
    question_label = tk.Label(test_window, text="",
                              font=("Arial", 20, "bold"), fg="blue")
    question_label.pack(pady=10)
    
    
    tk.Label(test_window, text="Your answer:").pack(pady=5)
    entry_answer = tk.Entry(test_window, width=30)
    entry_answer.pack(pady=5)
    
    
    result_label = tk.Label(test_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)
    
    
    score_label = tk.Label(test_window, text="✅ 0  |  ❌ 0",
                           font=("Arial", 11))
    score_label.pack(pady=5)
    
    
    def load_new_question():
        nonlocal random_key, correct_answer
        
        random_key = random.choice(list(word_book.keys()))
        correct_answer = word_book[random_key]
        
        question_label.config(text=random_key)
        entry_answer.delete(0, tk.END)
        result_label.config(text="")
    
    
    def check_answer():
        nonlocal score_correct, score_wrong
        
        user_answer = entry_answer.get().strip()
        
        if not user_answer:
            result_label.config(text="⚠ Please write an answer!",
                                fg="red")
            return
        
        if user_answer == correct_answer:
            score_correct += 1
            result_label.config(text="✅ Correct! 😸", fg="green")
        else:
            score_wrong += 1
            result_label.config(
                text=f"❌ Wrong! The answer is: {correct_answer}",
                fg="red")
        

        score_label.config(text=f"✅ {score_correct}  |  ❌ {score_wrong}")
    
    
    load_new_question()
    
    
    tk.Button(test_window, text="Check", width=15,
              command=check_answer).pack(pady=5)
    tk.Button(test_window, text="Next", width=15,
              command=load_new_question).pack(pady=5)
    tk.Button(test_window, text="Close", width=15,
              command=test_window.destroy).pack(pady=5)

#================================================================
# Buttons ✅️
#================================================================
but1 = tk.Button(window, text="1 - Add new German word.",
                 width=30, command=add_word)
but1.pack(pady=5)

but2 = tk.Button(window, text="2 - Add new Workout.", width=30 ,command=add_workout)
but2.pack(pady=5)

but3 = tk.Button(window, text="3 - German words test.", width=30 ,command=word_test)
but3.pack(pady=5)

but4 = tk.Button(window, text="4 - Show all data.", width=30)
but4.pack(pady=5)

but5 = tk.Button(window, text="5 - Close App.",
                 width=30, command=window.destroy)
but5.pack(pady=5)



window.mainloop()
