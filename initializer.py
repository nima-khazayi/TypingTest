import pyfiglet
import curses
from wpm import TypingSession
import time

# Global variables (initialized here to avoid None issues)
var = None
line = None
cursor = None
height = None
width = None
session = None
start_time = None
end_time = None
flag = None
permisson = None
letter_counter = None
word_counter = None
each_wrd_len = []
words = []
length = []

"""
    Summary: The init function sets up global variables, processes the input text into words and line lengths,
    and initializes the TypingSession for tracking typing metrics.
"""

def init(text, h, w):
    """Take the global variable text"""
    global var, line, cursor, height, width, words, length, session, flag, each_wrd_len, letter_counter, word_counter, permisson

    # Initialize global variables
    height = h
    width = w
    var = text
    line = 9
    cursor = 0
    flag = False
    permisson = False
    letter_counter = 0
    word_counter = 0
    words = []
    each_wrd_len = []
    length = [0]

    # Split words in a list called words
    words = var.split(" ")
    for word in range(len(words)):
        words[word] += " "

    for word in words:
        each_wrd_len.append(len(word))
        if length[-1] + each_wrd_len[-1] + 1 >= width:
            length.append(0)
            length[-1] += each_wrd_len[-1]

        else:    
            length[-1] += each_wrd_len[-1]


    # Initialize TypingSession
    session = TypingSession(words)


def root(text, h, w):
    """This is called in other modules to start the app."""
    init(text, h, w)  # Call init with the provided parameters
    curses.wrapper(screen)

"""
    Summary: The running part (screen function) handles the main curses loop, displays the UI,
    processes user input, tracks typing progress, and calculates metrics at the end.
"""    

def screen(stdscr):
    global var, line, cursor, height, width, words, length, session, start_time, end_time, flag, letter_counter, word_counter, each_wrd_len

    try:
        """Main screen object"""
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.clear()
        stdscr.refresh()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # Correct
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Incorrect
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # Neutral

        # Display initial content
        stdscr.addstr(height - 2, width // 2 - 12, "Press Space To Continue", curses.A_BOLD)
        key = stdscr.getch() # Pulse to get start
        if key == 32:
            stdscr.move(height - 2, 0)
            stdscr.clrtoeol()
            stdscr.refresh()
            start_time = time.time()  # Fix: Start timer here after prompt

        # Display the text to type
        sum_of_lines = 0
        counter = 0

        while True:
            if sum_of_lines >= len(length):
                break

            temporary = 0
            while temporary < length[line - 9] and counter < len(words):
                stdscr.addstr(line, cursor, words[counter], curses.color_pair(3))
                temporary += each_wrd_len[counter]
                cursor += each_wrd_len[counter]
                counter += 1

            line += 1
            cursor = 0
            sum_of_lines += 1 

        line = 9
        cursor = 0   

        while True:
            # Display title
            message = pyfiglet.figlet_format("TypingTest", font="slant")
            stdscr.addstr(0, 0, message)
            stdscr.addstr(7, 0, "     ________________________________________")

            stdscr.move(line, cursor)
            stdscr.refresh()  # Ensure screen updates

            # Check if line index is within bounds
            if line - 9 < len(length) and word_counter == length[line - 9] - 1:
                line += 1
                cursor = 0
                stdscr.move(line, cursor)

            key = stdscr.getch()
            session.run(stdscr, key)            

            if handle_input(stdscr, key):
                # End of test handling
                end_time = time.time()
                duration = end_time - start_time if start_time else 0

                words_typed = word_counter + (1 if letter_counter > 0 else 0)
                words_per_minute = (words_typed / (duration / 60)) if duration > 0 else 0
                accuracy_score = session.get_accuracy()

                if flag: # Incomplete test
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

    if key == 27: # ESC to quit
        flag = True
        return True
    
    # Check if the user has typed all words
    if word_counter >= len(words):  # End condition
        return True

    elif key in (127, curses.KEY_BACKSPACE):
        remove(stdscr)

    else:
        alphabet_handling(stdscr, key)


def alphabet_handling(stdscr, key):
    """Handle input || Color the value"""
    global words, line, cursor, each_wrd_len, letter_counter, word_counter, permisson

    if permisson:
        return
    
    else:
        if word_counter >= len(words):
            return True # Prevent index errors
        
        expected_char = words[word_counter][letter_counter]

        input_char = chr(key)
        if input_char == expected_char: # Green or red
            stdscr.addstr(line, cursor, input_char, curses.color_pair(1))
            movement(stdscr)

        else:
            stdscr.addstr(line, cursor, input_char, curses.color_pair(2))
            movement(stdscr)
            permisson = True

        letter_counter += 1

        if letter_counter == each_wrd_len[word_counter]:
            letter_counter = 0
            word_counter += 1


def remove(stdscr):
    """Handle backspace: Remove last character and decrement counters."""
    global words, line, cursor, each_wrd_len, letter_counter, word_counter, permisson

    if permisson:

        if cursor == 0:
            line -= 1
            cursor = length[line - 9] - 1

        else:
            cursor -= 1

        if letter_counter == 0:
            word_counter -= 1
            letter_counter = each_wrd_len[word_counter] - 1
            stdscr.move(line, cursor)
            stdscr.refresh()
            stdscr.addstr(line, cursor, " ")

        else:
            letter_counter -= 1

            stdscr.move(line, cursor)
            stdscr.refresh()
            expected_char = words[word_counter][letter_counter]
            stdscr.addstr(line, cursor, expected_char, curses.color_pair(3))

        permisson = False

    else:
        return

def movement(stdscr):
    """Advance cursor and handle timer start."""
    global cursor, start_time

    if start_time is None:
        start_time = time.time()

    cursor += 1
    boundary_controller(stdscr)  # Call here to immediately check bounds

def boundary_controller(stdscr):
    """Keep cursor within screen and line bounds."""
    global length, cursor, line

    if line - 9 >= len(length):
        return  # End of text

    max_line_len = length[line - 9] - 1
    if cursor > max_line_len:  # Use > to catch overflow
        cursor = 0  # Reset to start of next line
        line += 1


