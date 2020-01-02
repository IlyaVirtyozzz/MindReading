from database import User, ThoughtList, ManagementDataBase
from constants import data
import pymorphy2, string


class UserThought():
    def __init__(self, db, user):
        self.db = db
        self.user = user
        self.management = ManagementDataBase(self.db)

    def way(self):
        if self.user.thought_num == 0:
            text = "Добавить" + "Посмотреть"
        elif self.user.thought_num == 1:
            "Добавить"
        elif self.user.thought_num == 2:
            "Посмотреть"
        return

    def get_contribution(self, user_text):
        result = self.check_correctness_thought(user_text)
        if result == 0:
            self.management.add_new_thought(self.user.user_id, user_text)
            self.user.contribution = True
            self.db.session.commit()
            text = "Отлично"
            tts = "Отлично"
            buttons = []
        elif result == 1:
            text = "Мало слов"
            tts = "Мало слов"
            buttons = []
        elif result == 2:
            text = "Слова херовые"
            tts = "Слова херовые"
            buttons = []
        elif result == 3:
            text = "Введите корректные данные"
            tts = "Введите корректные данные"
            buttons = []
        return text, tts, buttons

    def check_correctness_thought(self, text):
        morph = pymorphy2.MorphAnalyzer()
        text = "".join(l for l in text if l not in string.punctuation).lower()
        text = text.split()
        if len(text) < 4:
            return 1
        if any(word in text for word in data['fuck_words']):
            return 2
        for i in text:
            a = morph.parse(i)[0]
            if str(a.methods_stack[0][0]) == "<FakeDictionary>" or str(a.methods_stack[0][0]) == "<UnknAnalyzer>":
                return 3

        return 0
