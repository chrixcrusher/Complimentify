import random  # Import the random module for generating random choices
import cowsay  # Import the cowsay module for generating ASCII art of a cow saying the compliment
import textwrap  # Import the textwrap module for wrapping text
from PIL import Image, ImageDraw, ImageFont  # Import the necessary modules from the PIL library for image manipulation
import sqlite3  # Import the sqlite3 module for working with SQLite databases
import subprocess  # Import the subprocess module for executing shell commands
import sys  # Import the sys module for exiting the program

def main():
    greet = get_random_greeting()  # Get a random greeting from the greetings database
    name = input(f"{greet} What's your name? ")  # Prompt the user for their name

    response = prompt_user("Are you having a bad day? (yes/y or no/n): ", ["yes", "y", "no", "n"])  # Prompt the user if they are having a bad day

    if response in ["no", "n"]:
        no_response = get_random_no_response()  # Get a random response from the no_responses database
        print(no_response)  # Print the response
        sys.exit()  # Exit the program

    response = prompt_user("Do you mind me to share something with you? (yes/y or no/n): ", ["yes", "y", "no", "n"])  # Prompt the user if they want something shared with them

    if response in ["no", "n"]:
        print("Okay, I understand. Hope you'll feel fine soon.")
        sys.exit()  # Exit the program

    print("Great. Hope this helps you:")
    compliment = get_random_compliment()  # Get a random compliment from the compliments database
    compliment_name = f"{name}, {compliment}"  # Combine the name and compliment
    print(compliment_name)  # Print the compliment name (to be deleted)
    characters = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
                  'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
                  'turkey', 'turtle', 'tux']
    character = random.choice(characters)  # Choose a random character from the list
    cowsay_command = f'cowsay -c {character} -t "{compliment_name}"'  # Generate the cowsay ASCII art command
    cowsay_output = subprocess.check_output(cowsay_command, shell=True, text=True)  # Execute the cowsay command and capture the output
    print(cowsay_output)  # Print the generated cowsay output
    response = prompt_user("Do you want to output the compliment as a PNG? (yes/y or no/n): ", ["yes", "y", "no", "n"])  # Prompt the user if they want to output the compliment as a PNG

    if response in ["yes", "y"]:
        output_to_png(cowsay_output)  # Pass the generated cowsay output to the output_to_png function

def get_random_greeting():
    conn = sqlite3.connect('greetings.db')  # Connect to the greetings database
    cursor = conn.cursor()
    cursor.execute("SELECT greeting FROM greetings ORDER BY RANDOM() LIMIT 1;")  # Select a random greeting from the greetings database
    greeting = cursor.fetchone()[0]  # Fetch the greeting from the result
    conn.close()
    return greeting  # Return the greeting

def get_random_no_response():
    conn = sqlite3.connect('no_response.db')  # Connect to the no_response database
    cursor = conn.cursor()
    cursor.execute("SELECT response FROM no_responses ORDER BY RANDOM() LIMIT 1;")  # Select a random response from the no_responses database
    response = cursor.fetchone()[0]  # Fetch the response from the result
    conn.close()
    return response  # Return the response

def get_random_compliment():
    conn = sqlite3.connect('compliment.db')  # Connect to the compliment database
    cursor = conn.cursor()
    cursor.execute("SELECT compliment FROM compliments ORDER BY RANDOM() LIMIT 1;")  # Select a random compliment from the compliments database
    compliment = cursor.fetchone()[0]  # Fetch the compliment from the result
    conn.close()
    compliment = compliment.lower()  # Convert the compliment to lowercase
    return compliment  # Return the compliment

def prompt_user(prompt, valid_responses):
    while True:
        response = input(prompt).strip().lower()  # Prompt the user and convert the response to lowercase
        if response in valid_responses:
            return response  # Return the response if it is valid
        print("I don't understand what you said, kindly clarify.")

def output_to_png(text):
    # Use a monospaced font to maintain the alignment
    font = ImageFont.truetype("cour.ttf", 14)  # Load the monospaced font

    # Calculate the size of the image required to hold the text
    lines = text.split("\n")  # Split the text into lines
    max_line_width = max(font.getbbox(line)[2] for line in lines)  # Get the maximum line width
    max_line_height = max(font.getbbox(line)[3] for line in lines)  # Get the maximum line height
    image_width = max_line_width + 10  # Calculate the image width with padding
    image_height = max_line_height * len(lines) + 10  # Calculate the image height with padding

    img = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))  # Create a new image with white background
    d = ImageDraw.Draw(img)

    # Draw each line of text
    y_text = 0
    for line in lines:
        d.text((5, y_text), line, font=font, fill=(0, 0, 0))  # Draw the text with padding
        y_text += max_line_height
    
    img.save('compliment.png')  # Save the image as a PNG file

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
