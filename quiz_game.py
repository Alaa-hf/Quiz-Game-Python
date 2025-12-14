import csv
import matplotlib.pyplot as plt

def load_questions(filename):
    questions = []

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question_text = row["question"]
            options = [
                row["option_a"],
                row["option_b"],
                row["option_c"],
                row["option_d"]
            ]
            correct = row["correct"].strip().upper() # A or B for example

            questions.append({
                "question": question_text,
                "options": options,
                "correct": correct
            })

    return questions


# ASK ONE QUESTION

def ask_question(question_dict):
    print("\n" + question_dict["question"])
    option_labels = ["A", "B", "C", "D"]

    # print options
    for i, option in enumerate(question_dict["options"]):
        print(f"{option_labels[i]}) {option}")

    # get & validate user answer
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in option_labels:
            break
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

    # check if correct
    if answer == question_dict["correct"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer is {question_dict['correct']}.")
        return False


# PLAY ONE QUIZ ROUND

def play_quiz(questions):
    print("\n Python Quiz Game ")
    score = 0
    total = len(questions)

    for q in questions:
        if ask_question(q):
            score += 1

    print("\n Quiz Finished ")
    print(f"Your score: {score} / {total}")

    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 50:
        print("Not bad, keep practicing ")
    else:
        print("Keep studying Python, you can do it! ")

def show_result_chart(score, total):
    Wrong = total - score
    plt.figure()
    plt.title("Current Quiz Result")
    plt.bar(["Correct", "Wrong"], [score, Wrong], color=["green", "red"])
    plt.ylabel("Number of questions")
    plt.text(0, score + 0.3, str(score), ha='center')
    plt.text(1, Wrong + 0.3, str(Wrong), ha='center')
    plt.ylim(0, total)
    plt.show()


# Main Screen

def main():
    filename = "python_quiz.csv"
    questions = load_questions(filename)

    while True:
        print("\n MAIN MENU ")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            score, total = play_quiz(questions)
            show_result_chart(score, total)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
