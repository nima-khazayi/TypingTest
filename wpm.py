import curses

def run(stdscr, w, k):
    """Callable function to pass arguments"""
    text = " ".join(w)
    accuracy(text, k)
    


def wpm():
    pass

def accuracy(text, key):
    wrong = 0
    sum = len(text)