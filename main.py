# python-game
import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '/':
        num1 = num1 * num2  
    question = f"What is {num1} {operation} {num2}?"

    if operation == '/':
        answer = num1 / num2
    else:
        answer = eval(f"{num1} {operation} {num2}")

    return question, answer

def math_quiz():
    print("Welcome to the Math Quiz!")
    score = 0
    total_questions = 10

    for i in range(total_questions):
        question, answer = generate_question()
        print(f"Question {i + 1}: {question}")

        user_input = input("Your answer: ")
        try:
            user_answer = float(user_input)
        except ValueError:
            print("Invalid input.")
            continue

        if abs(user_answer - answer) < 0.01:  
            print("Correct")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer:.2f}")

    print(f"\nYour final score: {score}/{total_questions}")

    if score == total_questions:
        print("Brilliant ....... Keep going")
    elif score >= total_questions / 2:
        print("Good job..... Keep practicing")
    else:
        print("Better luck next time")

if _name_ == "_main_":
    math_quiz()
