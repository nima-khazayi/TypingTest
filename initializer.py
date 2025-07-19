import pyfiglet
import curses
from wpm import run

var = None
line = None
cursor = None
height = None
width = None
words = []
length = []

"""
    We fill this part with a summary
    of what init part will do
"""

def init(text, h, w):
    """Take the global variable text"""
    global var, line, cursor, height, width, words, length

    # Initialize global variables
    height = h
    width = w
    var = text
    line = 9
    cursor = 0

    # Split words in a list called words
    tmp = var.split(" ")
    for i in range(len(tmp)):
        tmp[i] = tmp[i].replace(" ", "")
        tmp[i] = tmp[i].replace("\n", "")
        words.append(tmp[i])

    # Save the length of each line in a list called length
    counter = 0
    for i in var:
        if i == "\n":
            length.append(counter)
            counter = 0

        else:
            counter += 1
    length.append(counter) # This is for the last line which does not have \n


def root(text, h, w):
    """This is called in other modules"""
    init(text, h, w)  # Call init with the provided parameters
    curses.wrapper(screen)

"""
    we fill this part with a summary
    of what running part will do
"""    

def screen(stdscr):
    global var, line, cursor, height, width, words, length

    try:
        """Main screen object"""
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.clear()
        stdscr.refresh()

        # Display initial content
        stdscr.addstr(height - 2, width // 2 - 12, "Press Space To Continue", curses.A_BOLD)
        while True:
            message = pyfiglet.figlet_format("TypingTest", font="slant")
            stdscr.addstr(0, 0, message)
            stdscr.addstr(7, 0, "     ________________________________________")
            stdscr.addstr(9, 0, var)
            boundary_controller(stdscr)
            stdscr.move(line, cursor)
            stdscr.refresh()  # Ensure screen updates

            key = stdscr.getch()
            run(stdscr, words, key)
            if handle_input(stdscr, key):
                break

    except Exception as e:
        print(f"Curses error: {e}")  # Debug output before exiting
        raise

    finally:
        # Cleanup to restore terminal on exit
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

def handle_input(stdscr, key):
    """Function for keys' handling"""
    global height

    if key == 27:
        return True
    
    elif key == 32:
        stdscr.move(height - 2, 0)
        stdscr.clrtoeol()
        movement(stdscr)
        stdscr.refresh()
    
def movement(stdscr):
    """Keep going infront"""
    global cursor
    cursor += 1

def boundary_controller(stdscr):
    """Always keeps us in the screen"""
    global length, cursor, line

    if cursor >= length[line - 9]:
        cursor = 1
        line += 1




