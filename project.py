from rich.console import Console    # For colored output
from rich.text import Text          # For styled text
import curses
import pyfiglet                     # For ASCII art
import os
import shutil
import time

console = Console()

def clear():
    """Clear the screen before running."""
    os.system("cls" if os.name == "nt" else "clear")

def enterance():
    """Display entrance text in slanted ASCII art."""
    message = pyfiglet.figlet_format("TypingTest", font="slant")
    console.print(message)
    print("________________________________________")
    

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

def main():
    clear()
    enterance()
    """Main function."""
    try:
        print("")
        colorized_message("Welcome to My Project!\n", "green")
        colorized_message("Press Enter to continue...", "orange")
        input()  # Wait for user input
        clear()


    except ModuleNotFoundError:
        colorized_message("\nModule not found", "red")
        colorized_message("\nInstall requirements from requirements.txt", "red")
    except EOFError:
        colorized_message("\nAn unexpected error occurred", "red")
    except KeyboardInterrupt:
        colorized_message("\nAn unexpected error occurred", "red")

if __name__ == "__main__":
    main()