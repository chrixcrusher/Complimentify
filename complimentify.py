import sqlite3
import random
import cowsay
import sys

def main():
    # Greeting the user and ask for its name
    greet = get_random_greeting()
    name = input(f"{greet} What's your name? ")
    
    # Asking about the day
    response = prompt_user("Are you having a bad day? (yes/y or no/n): ", ["yes", "y", "no", "n"])
    
    if response in ["no", "n"]:
        no_response = get_random_no_response()
        print(no_response)
        sys.exit()
    
    # Asking if they want a compliment
    response = prompt_user("Do you mind me to share something with you? (yes/y or no/n): ", ["yes", "y", "no", "n"])
    
    if response in ["no", "n"]:
        print("Okay, I understand. Hope you'll feel fine soon.")
        sys.exit()
    
    # Giving a compliment
    print("Great. Hope this helps you:")
    compliment = get_random_compliment()
    characters = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
                  'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
                  'turkey', 'turtle', 'tux']
    character = random.choice(characters)
    getattr(cowsay, character)(f"{name}, {compliment}")

def get_random_greeting():
    conn = sqlite3.connect('greetings.db')
    cursor = conn.cursor()
    cursor.execute("SELECT greeting FROM greetings ORDER BY RANDOM() LIMIT 1;")
    greeting = cursor.fetchone()[0]
    conn.close()
    return greeting

def get_random_no_response():
    conn = sqlite3.connect('no_response.db')
    cursor = conn.cursor()
    cursor.execute("SELECT response FROM no_responses ORDER BY RANDOM() LIMIT 1;")
    response = cursor.fetchone()[0]
    conn.close()
    return response

def get_random_compliment():
    conn = sqlite3.connect('compliment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT compliment FROM compliments ORDER BY RANDOM() LIMIT 1;")
    compliment = cursor.fetchone()[0]
    conn.close()
    compliment = compliment.lower()
    return compliment

def prompt_user(prompt, valid_responses):
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        print("I don't understand what you said, kindly clarify.")

if __name__ == "__main__":
    main()



