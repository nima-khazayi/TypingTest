# Typing Test

#### Video Demo: <URL HERE>

#### Description:
This Typing Test project allows users to practice typing with varying levels of difficulty. It includes features such as colored output, customizable word selection, and typing metrics.

### Features:
- **Clear Screen**: Clears the terminal before starting the test.
- **Colorized Messages**: Displays messages in various colors for better user experience.
- **Word Selection**: Users can choose the number of words and their lengths for the typing test.
- **Typing Metrics**: Calculates words per minute (WPM) and accuracy based on user input.
- **Curses Interface**: Utilizes the curses library for an interactive terminal interface.

### Requirements:
To run this project, ensure you have the following Python packages installed:
- `nltk==3.9.1`
- `rich==14.0.0`
- `pyfiglet==1.0.3`
- `pytest==8.4.1`

### How to Run:
1. Clone the repository.
2. Install the required packages using:
   ```bash

   pip install -r requirements.txt
   ```
3. Run the main application:
   ```bash

   python project.py
   ```

### Testing:
To run the tests, use:
```bash

pytest test_project.py

```