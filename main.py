import helpers

def main():
    tools = [] # List to store tool usage history

    while True:
        print("\n=== Python Mini Toolkit ===")
        print("1. Grade Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Even or Odd Checker")
        print("5. View History")
        print("6. Exit")

        choice = input("Choose a tool (1-6): ")

        if choice == "1":
            helpers.grade_calculator()
            tools.append("Used Grade Calculator")
        elif choice == "2":
            helpers.todo_list()
            tools.append("Used To-Do List")
        elif choice == "3":
            helpers.number_guessing_game()
            tools.append("Used Number Guessing Game")
        elif choice == "4":
            helpers.even_odd_checker()
            tools.append("Used Even/Odd Checker")
        elif choice == "5":
            print("\n--- Usage History ---")
            if tools:
                for i, tool in enumerate(tools, 1):
                    print(f"{i}. {tool}")
            else:
                print("No tools used yet.")
        elif choice == "6":
            print("Thanks for using Python Mini Toolkit!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
