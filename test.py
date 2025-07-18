from initializer import root
import shutil

if __name__ == "__main__":
    terminal_size = shutil.get_terminal_size()
    height = terminal_size.lines
    width = terminal_size.columns
    root("Your text here", height, width)  # Example dimensions