import os.path
from database import ManagementDataBase


class Reports():
    def __init__(self, db):
        self.db = db
        self.management = ManagementDataBase(self.db)

    def thought_incorrect(self, from_user_id, thought_id):
        thought = self.management.get_thought(thought_id)
        text = from_user_id[:5] + " | " + thought.id + " | " + thought.text
        if os.path.exists("program_error.txt"):
            with open("program_error.txt", "a", encoding='utf-8') as file:
                file.write(text)
        else:
            with open("program_error.txt", "w", encoding='utf-8') as file:
                file.write(text)
        return True
