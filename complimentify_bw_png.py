import random
import cowsay
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sqlite3
import subprocess
import sys

def main():
    greet = get_random_greeting()
    name = input(f"{greet} What's your name? ")

    response = prompt_user("Are you having a bad day? (yes/y or no/n): ", ["yes", "y", "no", "n"])

    if response in ["no", "n"]:
        no_response = get_random_no_response()
        print(no_response)
        sys.exit()

    response = prompt_user("Do you mind me to share something with you? (yes/y or no/n): ", ["yes", "y", "no", "n"])

    if response in ["no", "n"]:
        print("Okay, I understand. Hope you'll feel fine soon.")
        sys.exit()

    print("Great. Hope this helps you:")
    compliment = get_random_compliment()
    compliment_name = f"{name}, {compliment}"
    print(compliment_name)  # to be deleted
    characters = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
                  'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
                  'turkey', 'turtle', 'tux']
    character = random.choice(characters)
    cowsay_command = f'cowsay -c {character} -t "{compliment_name}"'  # Generate the cowsay ASCII art
    cowsay_output = subprocess.check_output(cowsay_command, shell=True, text=True)
    print(cowsay_output)  # Print the generated cowsay output
    response = prompt_user("Do you want to output the compliment as a PNG? (yes/y or no/n): ", ["yes", "y", "no", "n"])

    if response in ["yes", "y"]:
        output_to_png(cowsay_output)  # Pass the generated cowsay output to the output_to_png function

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

def output_to_png(text):
    # Use a monospaced font to maintain the alignment
    font = ImageFont.truetype("cour.ttf", 14)  # cour.ttf is a monospaced font. Ensure this file is available.

    # Calculate the size of the image required to hold the text
    lines = text.split("\n")
    max_line_width = max(font.getbbox(line)[2] for line in lines)
    max_line_height = max(font.getbbox(line)[3] for line in lines)
    image_width = max_line_width + 10  # Add some padding
    image_height = max_line_height * len(lines) + 10  # Add some padding

    img = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Draw each line of text
    y_text = 0
    for line in lines:
        d.text((5, y_text), line, font=font, fill=(0, 0, 0))  # Add some padding
        y_text += max_line_height

    # Make the text bold
    img = img.filter(ImageFilter.FIND_EDGES)
    
    img.save('compliment.png')


if __name__ == "__main__":
    main()
