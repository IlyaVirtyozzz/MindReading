import json, os.path


def read_json():
    with open("data.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


def dumb_json(data):
    with open("data.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)


def create_dont_know_log():
    with open("mysite/dont_know.txt", "w", encoding='utf-8') as write_file:
        pass


def add_log_text(text):
    if not os.path.exists("mysite/dont_know.txt"):
        create_dont_know_log()
    with open("mysite/dont_know.txt", "a", encoding='utf-8') as write_file:
        write_file.write(text + "\n")


class Helps():
    def __init__(self, db, user):
        self.db = db
        self.user = user

    def get_first_helps(self):
        if self.user.first_help_num == 0:
            text = "бе бе бе 1"
            tts = "бе бе бе 1"

        elif self.user.first_help_num == 1:
            text = "бе бе бе 2"
            tts = "бе бе бе 2"

        elif self.user.first_help_num == 2:
            text = "бе бе бе 3"
            tts = "бе бе бе 3"

        elif self.user.first_help_num == 3:
            text = "бе бе бе 4"
            tts = "бе бе бе 4"

        buttons = [{
            "title": "Дальше",
            "hide": True
        }]
        self.user.first_help_num += 1
        self.db.session.commit()
