import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal in the world?": "Blue whale",
    "What is the chemical symbol for water?": "H2O",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What year did the Titanic sink?": "1912"
}

# Function to display welcome message and rules
def display_welcome_message():
    welcome_message = (
        "Welcome to the Quiz Game!\n"
        "Answer the following questions.\n"
        "Let's get started!\n"
    )
    messagebox.showinfo("Welcome", welcome_message)

# Function to present quiz questions
def present_quiz_questions():
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        user_answer = messagebox.askquestion("Quiz Question", question)
        correct_answer = quiz_questions[question].capitalize()

        if user_answer.lower() == "yes":
            user_response = messagebox.askstring("Your Answer", "Your answer:")
            user_response = user_response.strip().capitalize()
            if user_response == correct_answer:
                messagebox.showinfo("Result", "Correct!")
                score += 1
            else:
                messagebox.showerror("Result", "Incorrect! The correct answer is: " + correct_answer)
        else:
            messagebox.showinfo("Result", "The correct answer is: " + correct_answer)

    return score

# Function to display final results
def display_final_results(score, total_questions):
    result_message = (
        "Quiz completed!\n"
        f"Your final score is: {score} / {total_questions}\n"
        f"Percentage: {score / total_questions * 100:.2f}%\n"
    )
    if score / total_questions >= 0.7:
        result_message += "Congratulations, you passed!"
    else:
        result_message += "Sorry, you did not pass. Better luck next time!"
    messagebox.showinfo("Quiz Completed", result_message)

# Function to play again
def play_again():
    response = messagebox.askyesno("Play Again?", "Do you want to play again?")
    return response

# Main function to run the quiz game
def quiz_game():
    display_welcome_message()
    total_questions = len(quiz_questions)
    play = True

    while play:
        score = present_quiz_questions()
        display_final_results(score, total_questions)
        play = play_again()

# Create main window
root = tk.Tk()
root.title("Quiz Game")

# Start button
start_button = tk.Button(root, text="Start Quiz", command=quiz_game)
start_button.pack(pady=20)

# Run the application
root.mainloop()
