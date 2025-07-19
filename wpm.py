
class TypingSession:

    def __init__(self, words):
        """Initializing the counter of letters and wrong typed counted letters"""
        self.text = " ".join(words)
        self.counter = -1
        self.wrong = 0

    def run(self, stdscr, key):
        """Handles the number of wrong key pressed"""
        if self.counter >= len(self.text) - 1:
            return

        if key == 32 and self.text[self.counter + 1] == " ":
            self.counter += 1

        elif key == 127:
            self.counter = max(-1, self.counter - 1) # For each backspace we must get back but the last one

        else:
            if self.counter + 1 < len(self.text) and chr(key) != self.text[self.counter + 1]:
                self.wrong += 1

            self.counter += 1


    def get_accuracy(self):
        """Return the accuracy"""
        correct = len(self.text) - self.wrong
        return (correct / len(self.text)) * 100
    