from datetime import date
from daily_track.data_handler import load_habits, save_habits, load_logs, save_logs

def initialize_today():
    habits = load_habits()
    logs = load_logs()
    today = str(date.today())
    if today not in logs:
        logs[today] = {habit["name"]: False for habit in habits}
        save_logs(logs)

def add_habit(habit, ques=None):
    if ques is None: 
        ques = []
    habits = load_habits()
    # Check if the habit already exists for today
    for h in habits:
        if h['name'] == habit:
            return f"Habit '{habit}' already exists in your list."
    habits.append({"name": habit, "ques": ques, "done": False})
    save_habits(habits)
    return f"Habit '{habit}' added to your habits list."
    

def list_today():
    logs = load_logs()
    habits = load_habits()
    today = str(date.today())
    today_log = logs.get(today, {})
    if not habits:
        print("No habits in your list. Add some habits first!")
        return
    print(f"Today's habits for {today}:")
    for i, habit in enumerate(habits):
        status = "✔" if today_log.get(habit["name"]) else " "
        print(f"{i + 1}. [{status}] {habit['name']}")
        if habit[ques]:
            print("   Ques:")
            for q in habit['ques']:
                print(f"   - {q}")
                
def mark_done_by_index(index):
    habits = load_habits()
    logs = load_logs()
    today = str(date.today())
    if not today in logs:
        logs[today] = {habit["name"]: False for habit in habits}
        if 0