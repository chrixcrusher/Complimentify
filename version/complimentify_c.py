import sqlite3  # Importing the sqlite3 module to interact with SQLite databases
import random  # Importing the random module to make random selections
import cowsay  # Importing the cowsay module to display messages with various characters
import sys  # Importing the sys module to use the sys.exit function

def main():
    # Greeting the user and ask for their name
    greet = get_random_greeting()  # Getting a random greeting from the database
    name = input(f"{greet} What's your name? ")  # Asking the user for their name
    
    # Asking about the day
    response = prompt_user("Are you having a bad day? (yes/y or no/n): ", ["yes", "y", "no", "n"])  # Prompting the user to ask about their day
    
    if response in ["no", "n"]:  # If the user is not having a bad day
        no_response = get_random_no_response()  # Get a random positive response
        print(no_response)  # Print the positive response
        sys.exit()  # Exit the program
    
    # Asking if they want a compliment
    response = prompt_user("Do you mind me to share something with you? (yes/y or no/n): ", ["yes", "y", "no", "n"])  # Asking if the user wants to hear a compliment
    
    if response in ["no", "n"]:  # If the user does not want a compliment
        print("Okay, I understand. Hope you'll feel fine soon.")  # Print an understanding message
        sys.exit()  # Exit the program
    
    # Giving a compliment
    print("Great. Hope this helps you:")  # Inform the user that a compliment is coming
    compliment = get_random_compliment()  # Get a random compliment from the database
    characters = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
                  'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
                  'turkey', 'turtle', 'tux']  # List of characters available in cowsay
    character = random.choice(characters)  # Randomly select one character from the list
    getattr(cowsay, character)(f"{name}, {compliment}")  # Use the selected character to say the compliment

def get_random_greeting():
    conn = sqlite3.connect('greetings.db')  # Connecting to the greetings database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL commands
    cursor.execute("SELECT greeting FROM greetings ORDER BY RANDOM() LIMIT 1;")  # Executing a query to get a random greeting
    greeting = cursor.fetchone()[0]  # Fetching the result of the query
    conn.close()  # Closing the database connection
    return greeting  # Returning the greeting

def get_random_no_response():
    conn = sqlite3.connect('no_response.db')  # Connecting to the no_response database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL commands
    cursor.execute("SELECT response FROM no_responses ORDER BY RANDOM() LIMIT 1;")  # Executing a query to get a random no-response
    response = cursor.fetchone()[0]  # Fetching the result of the query
    conn.close()  # Closing the database connection
    return response  # Returning the response

def get_random_compliment():
    conn = sqlite3.connect('compliment.db')  # Connecting to the compliment database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL commands
    cursor.execute("SELECT compliment FROM compliments ORDER BY RANDOM() LIMIT 1;")  # Executing a query to get a random compliment
    compliment = cursor.fetchone()[0]  # Fetching the result of the query
    conn.close()  # Closing the database connection
    compliment = compliment.lower()  # Converting the compliment to lowercase
    return compliment  # Returning the compliment

def prompt_user(prompt, valid_responses):
    while True:  # Start an infinite loop
        response = input(prompt).strip().lower()  # Prompt the user and get their response, stripped of leading/trailing whitespace and converted to lowercase
        if response in valid_responses:  # Check if the response is valid
            return response  # Return the valid response
        print("I don't understand what you said, kindly clarify.")  # Inform the user that their input was not understood

if __name__ == "__main__":
    main()  # Call the main function if this script is run directly
