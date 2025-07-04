from daily_track.tracker import add_habit, list_today, mark_done_by_index

def prompt_ques():
    ques = []
    print("Enter questions for this habit (leave blank to finish):")
    while True:
        q = input("Q: ")
        if not q.strip():
            break
        ques.append(q)
    return ques

def main():
    initialize_today()  # Ensure today's log is initialized
    print("Welcome to your Daily Habit Tracker!")
    while True:
        list_today()
        print("\nDaily Habit Tracker")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            habit = input("Enter habit name: ")
            ques = prompt_ques()
            result = add_habit(habit, ques)
            print(result)
        elif choice == '2':
            try:
                num = int(input("Enter habit number to mark as done: ")) - 1
                result = mark_done_by_index(num)
                print(result)
            except ValueError:
                print("Invalid input, please enter a number.")
        elif choice == '3':
            print("Exiting the tracker.")
            break        
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()
# This code provides a simple command-line interface for the daily habit tracker.
# It allows users to add habits with associated questions and list today's habits.
# The `prompt_ques` function collects questions for the habit until the user leaves it blank.
# The `main` function provides a loop for user interaction, allowing them to choose between adding a habit, listing today's habits, or exiting the program.
# The tracker uses the `add_habit` and `list_today` functions from the `tracker` module to manage habits.