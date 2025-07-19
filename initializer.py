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
counter = None
flag = None 
words = []
length = []

"""
    We fill this part with a summary
    of what init part will do
"""

def init(text, h, w):
    """Take the global variable text"""
    global var, line, cursor, height, width, words, length, session, counter, flag

    # Initialize global variables
    height = h
    width = w
    var = text
    line = 9
    cursor = 0
    counter = -1
    flag = False

    # Split words in a list called words
    tmp = var.split(" ")
    for i in range(len(tmp)):
        tmp[i] = tmp[i].replace(" ", "")
        tmp[i] = tmp[i].replace("\n", "")
        words.append(tmp[i])

    # Save the length of each line in a list called length
    c = 0
    for i in var:
        if i == "\n":
            length.append(c)
            c = 0

        else:
            c += 1
    length.append(c) # This is for the last line which does not have \n

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
    global var, line, cursor, height, width, words, length, session, start_time, end_time, counter, flag

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
        key = stdscr.getch() # Pulse to get start
        if key == 32:
            stdscr.move(height - 2, 0)
            stdscr.clrtoeol()
            movement(stdscr)
            stdscr.refresh()
            counter += 1

        stdscr.addstr(9, 0, var)

        while True:
            message = pyfiglet.figlet_format("TypingTest", font="slant")
            stdscr.addstr(0, 0, message)
            stdscr.addstr(7, 0, "     ________________________________________")
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
                if flag:
                    stdscr.addstr(height - 1, 0, f"Time: {duration:.2f}s | Accuracy: {accuracy_score:.2f}% | WPM: Test has not finished")
                    
                else:
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
    global height, flag

    if key == 27:
        flag = True
        return True
    
    elif line - 9 == len(length):
        return True
    
    elif key == 32:
        if var[cursor] == " " or var[cursor] == "\n":
            movement(stdscr)

        else:
            alphabet_handling(stdscr, key)

    elif key == 127:
        remove(stdscr)

    else:
        alphabet_handling(stdscr, key)


def alphabet_handling(stdscr, key):
    """Handle input || Color the value"""
    global counter, var

    if key == 32:
        var = var[:cursor] + " " + var[cursor + 1:]
        stdscr.addstr(9, 0, var, curses.color_pair(3))
        stdscr.addstr(line, cursor, " ", curses.color_pair(2))
        movement(stdscr)
        counter += 1

    else:
        if chr(key) == var[cursor - 1]:
            var = var[:cursor] + chr(key) + var[cursor:]
            stdscr.addstr(9, 0, var, curses.color_pair(3))
            stdscr.addstr(line, cursor, chr(key), curses.color_pair(1))
            movement(stdscr)
            counter += 1

        else:
            var = var[:cursor] + chr(key) + var[cursor + 1:]
            stdscr.addstr(9, 0, var, curses.color_pair(3))
            stdscr.addstr(line, cursor, chr(key), curses.color_pair(2))
            movement(stdscr)
            counter += 1
    

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




