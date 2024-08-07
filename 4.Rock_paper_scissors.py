import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Wow, a tie! We both picked {user_choice}."
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return f"Nice one! You chose {user_choice} and I chose {computer_choice}. You win this round!"
    
    return f"Ouch! I picked {computer_choice} and you picked {user_choice}. I win this round!"

def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    messagebox.showinfo("Round Result", result)
    
    if "You win this round!" in result:
        global user_wins
        user_wins += 1
    elif "I win this round!" in result:
        global computer_wins
        computer_wins += 1

    update_score()

def update_score():
    score_label.config(text=f"Your score: {user_wins}\nMy score: {computer_wins}")

def reset_game():
    global user_wins, computer_wins
    user_wins = 0
    computer_wins = 0
    update_score()

user_wins = 0
computer_wins = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Showdown")

tk.Label(root, text="Rock-Paper-Scissors Showdown!", font=("Helvetica", 16)).pack(pady=15)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

score_label = tk.Label(root, text="Your score: 0\nMy score: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Restart", command=reset_game)
reset_button.pack(pady=15)

root.mainloop()
