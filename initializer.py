import pyfiglet
import curses

var = None
line = None
cursor = None
height = None
width = None

def init(text, h, w):
    """Take the global variable text"""
    global var
    global line
    global cursor
    global height
    global width

    # Initialize global variables
    height = h
    width = w
    var = text
    line = 9
    cursor = 0

def screen(stdscr):
    """Main screen object"""
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(height - 2, width // 2 - 12, "Press Space To Continue", curses.A_BOLD)
        while True:
            message = pyfiglet.figlet_format("TypingTest", font="slant")
            stdscr.addstr(0, 0, message)
            stdscr.addstr(7, 0, "     ________________________________________")
            stdscr.addstr(9, 0, var)
            stdscr.move(line, cursor)

            # Take characters
            key = stdscr.getch()
            if handle_input(stdscr, key):
                break

    finally:
        # Cleanup to restore terminal on exit
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        

def handle_input(stdscr, key):
    """Function for keys' handling"""
    if key == 27:
        return True
    
    elif key == 32:
        stdscr.move(height - 2, 0)
        stdscr.clrtoeol()
        movement(stdscr)
    

def movement(stdscr):
    stdscr.move(line, cursor + 1)
