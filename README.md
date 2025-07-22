# TypingTest

#### Video Demo: <https://youtu.be/nty1rE6nezo?si=tlLzKj6rgLkLKyWq>

#### Description:
A typing test is a structured assessment designed to evaluate a person's typing speed and accuracy. It typically involves typing a series of words, sentences, or passages within a specified time limit. These tests are commonly used in educational settings, professional environments, and self-improvement initiatives to help individuals develop their typing skills and increase productivity.

The Typing Test project provides a robust and engaging platform for users to practice and refine their typing abilities, catering to typists of all levels—from beginners to advanced users. This application is meticulously crafted to create an immersive learning experience that emphasizes both usability and effectiveness.

Key features of the Typing Test application include:

- **Dynamic Word Selection**: Users can customize their typing sessions by selecting the number of words and setting a maximum length for those words. This flexibility allows for tailored practice sessions, whether users seek a quick warm-up or a more challenging workout.

- **Inclusion of Uppercase Letters**: The option to include uppercase letters adds complexity to the tests, helping users improve their proficiency in handling diverse typing scenarios, such as typing names, titles, or acronyms.

- **Real-Time Feedback**: The application provides instant visual feedback through color-coded messaging. Correctly typed characters are displayed in green, while mistakes are highlighted in red. This immediate reinforcement helps users recognize typing habits and encourages them to adjust their approach in real-time.

- **Performance Metrics**: Comprehensive metrics, including Words Per Minute (WPM) and accuracy percentages, are calculated during each session. These metrics are invaluable for users to track their progress, set goals, and celebrate improvements over time, allowing them to visualize their growth and identify specific areas that require further practice.

- **Interactive Curses Interface**: Utilizing the `curses` library, the application presents a responsive and user-friendly terminal interface. This design promotes concentration by minimizing distractions, enabling users to focus entirely on their typing. The seamless interaction encourages longer practice sessions, making learning more effective.

- **ASCII Art and Engaging Prompts**: The application enhances the user experience with visually appealing ASCII art that serves as a welcoming introduction to each session. Thoughtfully crafted prompts guide users through the process, ensuring clarity and ease of use.

This Typing Test project not only aims to improve typing speed but also emphasizes accuracy and overall typing fluency. It serves as an excellent tool for students, professionals, and anyone looking to enhance their typing skills in a fun and interactive way.

Join a community of learners dedicated to mastering the art of typing. Dive into the Typing Test project and discover how enjoyable and rewarding improving your typing skills can be!

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
