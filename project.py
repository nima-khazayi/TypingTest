from rich.console import Console    # For colored output
from rich.text import Text          # For styled text
import curses
import pyfiglet                     # For ASCII art
import os
import shutil
import time
from textcreator import dict
from initializer import init, screen

console = Console()

def clear():
    """Clear the screen before running."""
    os.system("cls" if os.name == "nt" else "clear")

def enterance():
    """Display entrance text in slanted ASCII art."""
    message = pyfiglet.figlet_format("TypingTest", font="slant")
    console.print(message)
    print("     ________________________________________")
    
def colorized_message(message, color="cyan"):
    """Print a colorized message."""
    if color == "white":
        text = Text(message, style=color)
        console.print(text)
    else:
        for i in message:
            i = Text(i, style=color)
            console.print(i, end="")
            time.sleep(0.04)

def sample_words(num):
    """Appears the TypingText"""
    dictionary = dict(num)
    clear()
    enterance()
    print("")
    text = " ".join(dictionary)
    better_print(text)
    

def better_print(text):
    """Take the terminal length, Hints, More user friendly"""
    # Initialize the screen size
    terminal_size = shutil.get_terminal_size()
    height = terminal_size.lines
    width = terminal_size.columns

    # Make the text of the words, screen dynamic
    words_length = 0
    text_tmp = text.split(" ")
    for i in range(len(text_tmp)):
        words_length += len(text_tmp[i]) + 1
        if words_length >= width:
            text_tmp[i - 1] += "\n"
            words_length = len(text_tmp[i])

    text_tmp[0] = " " + text_tmp[0]
    text = " ".join(text_tmp) 
    print(text)
    init(text, height, width)
    curses.wrapper(screen)


def get_valid_input():
    """Length taker"""
    while True:
        try:
            clear()
            enterance()
            print("")
            colorized_message("Choose the number of your typing test words: ", "green")
            num = int(input())
            if num < 30:
                colorized_message("Choose 30 or more words!", "red")
                time.sleep(3)        
            else:
                sample_words(num)
                break

        except ValueError:
            colorized_message("Your input number was not in a valid integer form", "red")

def main():
    clear()
    enterance()
    """Main function."""
    print("")
    colorized_message("Welcome to My Project!\n", "green")
    colorized_message("Press Enter to continue...", "orange")
    input()  # Wait for user input
    try:
        get_valid_input()

    except ModuleNotFoundError:
        colorized_message("\nModule not found", "red")
        colorized_message("\nInstall requirements from requirements.txt", "red")
    except EOFError:
        colorized_message("\nAn unexpected error occurred", "red")
    except KeyboardInterrupt:
        colorized_message("\nAn unexpected error occurred", "red")
    

if __name__ == "__main__":
    main()