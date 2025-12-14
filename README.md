Python Quiz Game (Programming Languages Project)

A simple console-based Python quiz game that loads multiple-choice questions from a CSV file, quizzes the user interactively, calculates the final score and percentage, and displays a bar chart showing correct vs. wrong answers using Matplotlib.

Features
- Loads quiz questions from a CSV file using csv.DictReader
- Displays questions with four options (A/B/C/D)
- Validates user input to accept only A, B, C, or D
- Calculates score, total questions, and percentage result
- Provides basic performance feedback based on the percentage
- Visualizes results in a bar chart (Correct vs. Wrong) using Matplotlib
- Includes a simple main menu (Start Quiz / Exit)

Project Structure
Recommended file structure:
- quiz_game.py (or any Python file name containing the code)
- python_quiz.csv (the dataset of questions)

Example:
project-folder/
quiz_game.py
python_quiz.csv

## CSV File Format
The program expects a CSV file named python_quiz.csv in the same folder as the Python script.

The CSV must include these column headers:
- question
- option_a
- option_b
- option_c
- option_d
- correct

Example row:
- correct should contain one letter: A, B, C, D

Requirements
- Python 3.x
- matplotlib

Install matplotlib:
bash
pip install matplotlib

How to Run
1.Place python_quiz.csv in the same folder as your Python script.
2.Run the program:
python quiz_game.py
	3.	From the main menu:

		Enter 1 to start the quiz
		Enter 2 to exit

After the quiz ends, a bar chart will appear showing the number of correct and wrong answers.

How It Works
	-	load_questions(filename): Reads questions and options from the CSV file and returns a list of question dictionaries.
	-	ask_question(question_dict): Prints a question, reads the user answer, validates it, and checks correctness.
	-	play_quiz(questions): Runs through all questions, calculates the score and percentage, and prints feedback.
	-	show_result_chart(score, total): Displays a Matplotlib bar chart summarizing the results.
	-	main(): Runs the menu loop and starts the quiz when selected.

Notes
	-	The file name is currently set to python_quiz.csv inside the code:
filename = "python_quiz.csv"
If you rename the CSV file, update this line accordingly.

License

This project was created for an academic Programming Languages course project.
