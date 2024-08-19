import tkinter as tk
import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "developer"]

def choose_word():
    return random.choice(word_list)

def update_display():
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    display_label.config(text=" ".join(display_word))

def guess_letter():
    global attempts
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Please enter a single letter.", fg="red")
        return
    
    if guess in guessed_letters:
        result_label.config(text="You already guessed that letter.", fg="orange")
        return
    
    guessed_letters.append(guess)
    
    if guess in word:
        result_label.config(text="Good guess!", fg="green")
        update_display()
        if all(letter in guessed_letters for letter in word):
            result_label.config(text="Congratulations! You guessed the word!", fg="blue")
            guess_button.config(state=tk.DISABLED)
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        result_label.config(text="Incorrect!", fg="red")
        if attempts == 0:
            result_label.config(text=f"Game over! The word was: {word}", fg="purple")
            guess_button.config(state=tk.DISABLED)

# Initialize the game
word = choose_word()
guessed_letters = []
attempts = 6

# Create the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x600")
root.config(bg="#282c34")

# Create and place the widgets
title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 24, "bold"), bg="#61afef", fg="#282c34")
title_label.pack(pady=20)

display_label = tk.Label(root, text="_ " * len(word), font=("Helvetica", 18), bg="#282c34", fg="#abb2bf")
display_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 18), justify="center", fg="#282c34", bg="#abb2bf")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 18, "bold"), bg="#61afef", fg="#282c34")
guess_button.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Helvetica", 18), bg="#282c34", fg="#d19a66")
attempts_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#282c34")
result_label.pack(pady=10)

# Run the game loop
update_display()
root.mainloop()