import json

DB_PATH = 'data/users.json'

def read_user():
    with open(DB_PATH, 'r') as f:
        return json.load(f)
    
def write_user(users):
    with open(DB_PATH, 'w') as f:
        json.dump(users, f, indent=2)