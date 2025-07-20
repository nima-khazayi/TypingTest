import curses

class TypingSession:

    def __init__(self, words):
        """Initializing the counter of letters and wrong typed counted letters"""
        self.text = ""
        for i in range(len(words)):
            self.text += words[i]
        self.counter = 0
        self.prev_counter = -1
        self.fore_counter = 1
        self.wrong = 0
        self.correct = 0

    def run(self, stdscr, key):
        """Handles the number of correct and wrong key presses."""

        if self.counter >= len(self.text):
            return

        if key in (127, curses.KEY_BACKSPACE):

            if self.counter == self.prev_counter: 
                pass # This part has been added to prevent counter reduction
                # By pressing backspace after once, and being locked

            else:
                if self.counter > 0:
                    self.counter -= 1
                    self.prev_counter = self.counter

                return

        try:
            input_char = chr(key)
        except ValueError:
            return  # Skip non-character keys

        expected_char = self.text[self.counter]

        if self.counter == self.fore_counter:
                pass # This part has been added to prevent counter increment
                # By pressing char keys after a wrong char pressed once, and being locked
        
        else:
            if input_char == expected_char:
                self.correct += 1
                self.counter += 1
                self.fore_counter += 1

            else:
                self.wrong += 1
                self.counter = self.fore_counter
                # Don't advance the counter on wrong char here
                # Let the frontend logic control when to allow retry


    def get_accuracy(self):
        """Return the accuracy"""
        total = self.correct + self.wrong
        if total == 0:
            return 0.0
        return (self.correct / total) * 100

    