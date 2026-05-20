import random

def grade_calculator():
    print("\n--- Grade Calculator ---")
    try:
        score = float(input("Enter your score (0-100): "))
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Your grade is: {grade}")
        return grade
    except ValueError:
        print("Please enter a valid number.")

def todo_list():
    print("\n--- To-Do List ---")
    todos = []
    while True:
        print("\n1. Add task 2. View tasks 3. Back to menu")
        option = input("Choose: ")
        if option == "1":
            task = input("Enter task: ")
            todos.append(task)
            print(f"Added: {task}")
        elif option == "2":
            if todos:
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
        elif option == "3":
            break

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    number = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number 1-10: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You got it in {attempts} attempts.")
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Enter a valid number.")

def even_odd_checker():
    print("\n--- Even or Odd Checker ---")
    try:
        num = int(input("Enter a number: "))
        # Bonus: using modulus and and/or
        if num % 2 == 0 and num!= 0:
            print(f"{num} is even.")
        elif num % 2!= 0:
            print(f"{num} is odd.")
        else:
            print("0 is neither even nor odd.")
    except ValueError:
        print("Please enter a valid integer.")