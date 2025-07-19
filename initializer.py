import pyfiglet
import curses
from wpm import TypingSession
import time

var = None
line = None
cursor = None
height = None
width = None
session = None
start_time = None
end_time = None
words = []
length = []

"""
    We fill this part with a summary
    of what init part will do
"""

def init(text, h, w):
    """Take the global variable text"""
    global var, line, cursor, height, width, words, length, session

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

    # Make session Typingsession Class Type
    session = TypingSession(words)


def root(text, h, w):
    """This is called in other modules"""
    init(text, h, w)  # Call init with the provided parameters
    curses.wrapper(screen)

"""
    we fill this part with a summary
    of what running part will do
"""    

def screen(stdscr):
    global var, line, cursor, height, width, words, length, session, start_time, end_time

    try:
        """Main screen object"""
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.clear()
        stdscr.refresh()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

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
            session.run(stdscr, key)
            if handle_input(stdscr, key):
                # When the script is going to an end
                global end_time

                end_time = time.time()
                duration = end_time - start_time

                words_per_minute = len(words) / (duration / 60)
                accuracy_score = session.get_accuracy()
                stdscr.addstr(height - 1, 0, f"Time: {duration:.2f}s | Accuracy: {accuracy_score:.2f}% | WPM: {words_per_minute:.2f}")
                stdscr.refresh()
                time.sleep(3)
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

    elif key == 127:
        remove(stdscr)

    else:
        alphabet_handling(stdscr, key)


def alphabet_handling(stdscr, key):
    """Handle input || Color the value"""
    global words
    

def remove(stdscr):
    pass


def movement(stdscr):
    """Keep going infront"""
    global cursor, start_time

    if start_time is None:
        start_time = time.time()

    cursor += 1

def boundary_controller(stdscr):
    """Always keeps us in the screen"""
    global length, cursor, line

    if cursor >= length[line - 9]:
        cursor = 1
        line += 1




