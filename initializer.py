import pyfiglet
import curses

var = None

def init(text):
    """Take the global variable text"""
    global var
    var = text

def screen(stdscr):
    """Main screen object"""
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.clear()
        stdscr.refresh()

        while True:
            message = pyfiglet.figlet_format("TypingTest", font="slant")
            stdscr.addstr(0, 0, message)
            stdscr.addstr(7, 0, "     ________________________________________")

            # Take characters
            key = stdscr.getch()
            if handle_input(key):
                break

    finally:
        # Cleanup to restore terminal on exit
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        

def handle_input(key):
    """Function for keys' handling"""
    if key == 27:
        return True
