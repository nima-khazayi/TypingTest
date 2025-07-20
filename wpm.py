import curses

class TypingSession:

    def __init__(self, words):
        """Initializing the counter of letters and wrong typed counted letters"""
        self.text = ""
        for i in range(len(words)):
            self.text += words[i]
        self.counter = 0
        self.wrong = 0
        self.correct = 0

    def run(self, stdscr, key):
        """Handles the number of wrong key pressed"""

        if len(self.text) == self.counter:
            return
        
        else:
            if key in (127, curses.KEY_BACKSPACE):
                self.counter -= 1

            else:
                if chr(key) == self.text[self.counter]:
                    self.correct += 1

                else:
                    self.wrong += 1

                self.counter += 1


    def get_accuracy(self):
        """Return the accuracy"""
        file = open("file.txt", "w")
        file.write(self.text)
        return self.wrong
    