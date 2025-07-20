from rich.console import Console    # For colored output
from rich.text import Text          # For styled text
import pyfiglet                     # For ASCII art
import os
import shutil
import time
from textcreator import dict
from initializer import root

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

def sample_words(num, n):
    """Appears the TypingText"""
    dictionary = dict(num, n)
    clear()
    enterance()
    print("")
    text = " ".join(dictionary)

    # Initialize the screen size
    terminal_size = shutil.get_terminal_size()
    height = terminal_size.lines
    width = terminal_size.columns

    root(text, height, width)


def get_valid_input():
    """Length taker"""
    try:
        # Taking the number of words
        clear()
        enterance()
        print("")
        colorized_message("Choose the number of your typing test words: ", "green")
        num = int(input())
        
        if num < 30:
            colorized_message("Choose 30 or more words!", "red")
            time.sleep(3)
            return get_valid_input()  # Call again if num is invalid

        # Taking the words length upper bound
        while True:
            clear()
            enterance()
            print("")
            colorized_message("The length of the words are less equal to: ", "green")
            n = int(input())

            if n < 4:
                colorized_message("Choose words with 4 or more letters", "red")
                time.sleep(3)
            else:
                break  # Exit the loop if n is valid

        sample_words(num, n)  # Call sample_words with valid inputs

    except ValueError:
        colorized_message("Your input number was not in a valid integer form", "red")
        time.sleep(3)
        return get_valid_input()  # Call again if input is invalid

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