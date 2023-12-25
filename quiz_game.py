
"""
Project 1: Python Quiz Game
"""

import time

# Setup & Basic Structure.
# create a list of dictionaries.
# each dictionary is a question, potential answers, and correct answer.

questions = [
    {
        "question": "Who founded Python?",
        "potential_answers": ["Larry Page", "Sergey Brin", "Guido van Rossum", "Mark Zuckerberg"],
        "correct_answer_index": 2
    },
    {
        "question": "What is the shortened version of boolean in python?",
        "potential_answers": ["bool", "boolean", "true", "false"],
        "correct_answer_index": 0
    },
    {
        "question": "what is 23 + 71?",
        "potential_answers": ["110", "107", "105", "94"],
        "correct_answer_index": 3
    },
    {
        "question": "When was Python created?",
        "potential_answers": ["1991", "1992", "1993", "1994"],
        "correct_answer_index": 0
    },
    {
        "question": "To assign a variable = or ==",
        "potential_answers": ["==", "=", "!", "!="],
        "correct_answer_index": 1
    }
]

# creat a quiz game function to play the game


def quiz_game():
    score = 0
    correct_answers = []
    incorrect_answers = []
    question_number = 1
    time_start = time.time()
    print("\nWelcome to the Python Quiz Game!\n")
    # loop through the questions
    for question in questions:
        valid_input = False
        # Keep asking the same question until valid input is received
        while not valid_input:
            # Display Question
            print(f"Question {question_number}: {question['question']}")
            answer_number = 1
            # Displaying Potential Answers
            for potential_answer in question["potential_answers"]:
                print(f" {answer_number}. {potential_answer}")
                answer_number += 1
            # take in user input
            try:
                user_answer = int(
                    input("Enter your answer (numbers 1-4): ")) - 1
                if (0 <= user_answer < len(question["potential_answers"])):
                    valid_input = True
                else:
                    print("Please enter a number from the list.\n")
            except ValueError as e:
                print(
                    f"Invalid input: {e}. Please enter a number from the list.\n")

        if user_answer == question["correct_answer_index"]:
            print("Correct!\n")
            score += 1
            correct_answers.append((question_number, question["question"]))
        else:
            print(
                f"Wrong! The correct answer was: {question['potential_answers'][question['correct_answer_index']]}\n")
            incorrect_answers.append(
                (question_number, question["question"], question['potential_answers'][question['correct_answer_index']]))

        question_number += 1

    # Display the final score and incorrect answers
    print(f"Your final score is {score}/{len(questions)}")

    # Display time spent on game
    time_end = time.time()
    time_spent = round(time_end - time_start, 2)
    print(f"Time spent on game: {time_spent} seconds")

    # Displays correct answers
    if correct_answers:
        print("\nQuestions Answered Correctly:")
        for q_num, q_text in correct_answers:
            print(f"Question {q_num}: {q_text}")

    # Displays incorrect answers
    if incorrect_answers:
        print("\nQuestions Answered Incorrectly:")
        for q_num, q_text, correct_answer in incorrect_answers:
            print(f"Question {q_num}: {q_text}")
            print(f"Correct answer: {correct_answer}\n")


# call the function to play the game
quiz_game()
