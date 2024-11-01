
"""
Project 1: Python Quiz Game:
This implementation provides a basic interface for adding new questions to the quiz. 
The new questions added during runtime will be lost when the program ends.
"""

import time

# Setup & Basic Structure.
# create a list of dictionaries.
# each dictionary is a question, potential answers, and correct answer.

questions_by_category = {
    "Python": [
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
    ],
    "General Knowledge": [
        {
            "question": "Who was the first president of the United States?",
            "potential_answers": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
            "correct_answer_index": 0
        },
        {
            "question": "What is the largest planet in our Solar System?",
            "potential_answers": ["Earth", "Saturn", "Jupiter", "Mars"],
            "correct_answer_index": 2
        },
        {
            "question": "In which year did World War II end?",
            "potential_answers": ["1945", "1946", "1947", "1948"],
            "correct_answer_index": 0
        },
        {
            "question": "Which ocean is the largest in the world?",
            "potential_answers": ["Atlantic", "Indian", "Pacific", "Arctic"],
            "correct_answer_index": 2
        },
        {
            "question": "Which language is the most spoken worldwide?",
            "potential_answers": ["English", "Spanish", "Mandarin", "Hindi"],
            "correct_answer_index": 2
        }
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "potential_answers": ["H2O", "CO2", "N2O", "H2SO4"],
            "correct_answer_index": 0
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "potential_answers": ["Mars", "Jupiter", "Saturn", "Venus"],
            "correct_answer_index": 0
        },
        {
            "question": "What force keeps us on the ground?",
            "potential_answers": ["Magnetism", "Gravity", "Friction", "Inertia"],
            "correct_answer_index": 1
        }
    ],
    "Mathematics": [
        {
            "question": "What is the value of Pi to two decimal places?",
            "potential_answers": ["3.14", "3.15", "3.16", "3.17"],
            "correct_answer_index": 0
        },
        {
            "question": "What is the square root of 64?",
            "potential_answers": ["6", "7", "8", "9"],
            "correct_answer_index": 2
        },
        {
            "question": "In geometry, how many sides does a hexagon have?",
            "potential_answers": ["5", "6", "7", "8"],
            "correct_answer_index": 1
        }
    ],
    "Literature": [
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "potential_answers": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct_answer_index": 1
        },
        {
            "question": "Which novel features the character 'Holden Caulfield'?",
            "potential_answers": ["The Great Gatsby", "To Kill a Mockingbird", "The Catcher in the Rye", "1984"],
            "correct_answer_index": 2
        },
        {
            "question": "What is the main theme of George Orwell's 'Animal Farm'?",
            "potential_answers": ["Friendship", "Love", "Politics", "War"],
            "correct_answer_index": 2
        }
    ]
}

# Function to give user the option to play quiz, add a question or exit game.


def quiz_game():
    while True:
        print("\n1. Play Quiz")
        print("2. Add New Question")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            play_quiz()  # quiz game logic
        elif choice == '2':
            add_new_question()  # add a question
        elif choice == '3':
            break  # quit game
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Function to add new question to the quiz game


def add_new_question():
    print("Select a category to add a question to:")
    for category in questions_by_category:
        print(category)

    user_input = input("Enter category: ").strip().lower()
    category_found = False

    for category in questions_by_category:
        if user_input == category.lower():
            category_found = True
            selected_category = category
            break

    if not category_found:
        print(f"No such category '{user_input}'. Returning to main menu.")
        return

    question = input("Enter the new question: ").strip()
    potential_answers = []
    for i in range(4):
        answer = input(f"Enter answer option {i+1}: ").strip()
        potential_answers.append(answer)

    correct_answer_index = int(
        input("Enter the index of the correct answer (1-4): ")) - 1
    new_question = {
        "question": question,
        "potential_answers": potential_answers,
        "correct_answer_index": correct_answer_index
    }

    questions_by_category[selected_category].append(new_question)
    print("New question added successfully.")


# Function to play the quiz game
def play_quiz():
    selected_category = None
    while selected_category is None:
        print("\nSelect a category:")
        for category in questions_by_category:
            print(category)

        # Convert user input to lowercase
        user_input = input("Enter category: ").lower()
        for category in questions_by_category:
            if user_input == category.lower():
                selected_category = category
                break

        if selected_category is None:
            print("Category not found. Please try again.")

    # Load questions for the selected category
    questions = questions_by_category[selected_category]

    score = 0
    correct_answers = []
    incorrect_answers = []
    question_number = 1
    time_start = time.time()
    print("\nWelcome to the Quiz Game!\n")
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
