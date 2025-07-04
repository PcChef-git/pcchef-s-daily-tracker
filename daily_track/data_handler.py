import json
from daily_track.config import HABITS_FILE, LOGS_FILE

def load_habits():
    if not os.path.exists(HABITS_FILE):
        return []
    with open(HABITS_FILE, 'r') as file:
        return json.load(file)
    
def save_habits(habits):
    with open(HABITS_FILE, 'w') as file:
        json.dump(habits, file, indent=4)
        
def load_logs():
    if not os.path.exists(LOGS_FILE):
        return {}
    with open(LOGS_FILE, 'r') as file:
        return json.load(file)

def save_logs(logs):
    with open(LOGS_FILE, 'w') as file:
        json.dump(logs, file, indent=2)