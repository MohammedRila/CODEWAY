import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Quiz questions and answers
quiz_questions = {
    "What is the capital of Japan?": "Tokyo",
    "Which planet is known as the Red Planet?": "Mars",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the currency of India?": "Rupee",
    "What is the chemical symbol for gold?": "Au"
}

# Function to display welcome message and rules
def display_welcome_message(text_widget):
    welcome_message = (
        "Welcome to the Quiz Game!\n"
        "Answer the following questions.\n"
        "Let's get started!\n\n"
    )
    text_widget.insert(tk.END, welcome_message)

# Function to present quiz questions
def present_quiz_questions(text_widget):
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        text_widget.insert(tk.END, f"Question: {question}\n")
        user_answer = simpledialog.askstring("Quiz Question", f"Question: {question}")
        correct_answer = quiz_questions[question].capitalize()

        if user_answer is not None:
            user_response = user_answer.strip().capitalize()
            if user_response == correct_answer:
                text_widget.insert(tk.END, "Result: Correct!\n\n")
                score += 1
            else:
                text_widget.insert(tk.END, f"Result: Incorrect! The correct answer is: {correct_answer}\n\n")
        else:
            text_widget.insert(tk.END, f"Result: The correct answer is: {correct_answer}\n\n")

    return score

# Function to display final results
def display_final_results(text_widget, score, total_questions):
    result_message = (
        "Quiz completed!\n"
        f"Your final score is: {score} / {total_questions}\n"
        f"Percentage: {score / total_questions * 100:.2f}%\n"
    )
    if score / total_questions >= 0.7:
        result_message += "Congratulations, you passed!"
    else:
        result_message += "Sorry, you did not pass. Better luck next time!"
    text_widget.insert(tk.END, result_message)

# Function to play again
def play_again():
    response = messagebox.askyesno("Play Again?", "Do you want to play again?")
    return response

# Main function to run the quiz game
def quiz_game(text_widget):
    display_welcome_message(text_widget)
    total_questions = len(quiz_questions)
    play = True

    while play:
        score = present_quiz_questions(text_widget)
        display_final_results(text_widget, score, total_questions)
        play = play_again()

# Create main window
root = tk.Tk()
root.title("Quiz Game")

# Text widget to display messages
output_text = tk.Text(root, height=20, width=50)
output_text.pack(pady=20)

# Start button
start_button = tk.Button(root, text="Start Quiz", command=lambda: quiz_game(output_text))
start_button.pack(pady=10)

# Run the application
root.mainloop()
