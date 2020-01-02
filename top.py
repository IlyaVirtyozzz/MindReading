from database import ThoughtList


class Top():
    def __init__(self, db, user):
        self.db = db
        self.user = user

    def way(self, tokens):
        if self.user.first_top:
            "здесь ты можешь бебебе"
            text, tts, buttons = 0, 0, 0
        else:
            def create_answer():
                thought = self.get_top_thought(self.user.top_num)
                if self.user.top_num < 0:

                    text = "Меньше 0"
                    tts = "Меньше 0"
                    buttons = [
                        {
                            "title": "Следующая мысль",
                            "hide": True
                        }, {
                            "title": "В меню",
                            "hide": True
                        }]
                elif 0 <= self.user.top_num <= 32:
                    text = thought.text
                    tts = thought.text
                    buttons = [
                        {
                            "title": "Следующая мысль",
                            "hide": True
                        }, {
                            "title": "В меню",
                            "hide": True
                        }]
                elif self.user.top_num > 32:
                    text = "Больше 32"
                    tts = "Больше 32"
                    buttons = [
                        {
                            "title": "В меню",
                            "hide": True
                        }]
                return text, tts, buttons
            if any(word in tokens for word in ["Далее"]):
                if self.user.top_num <= 32:
                    self.user.top_num += 1
                self.db.session.commit()
                text, tts, buttons = create_answer()
            elif any(word in tokens for word in ["Назад"]):
                if self.user.top_num >= 0:
                    self.user.top_num -= 1
                self.db.session.commit()
                create_answer()
            else:
                text = "Рэпчик"
                tts = "Рэпчик"
                buttons = [
                    {
                        "title": "В меню",
                        "hide": True
                    }, ]
                if self.user.top_num < 0:
                    buttons.insert(0, {
                        "title": "Дальше",
                        "hide": True
                    })
                elif 0 <= self.user.top_num <= 32:
                    buttons.insert(0, {
                        "title": "Дальше",
                        "hide": True
                    })
                    buttons.insert(0, {
                        "title": "Назад",
                        "hide": True
                    })
                elif self.user.top_num > 32:
                    buttons.insert(0, {
                        "title": "Назад",
                        "hide": True
                    })
        return text, tts, buttons

    def get_top_thought(self, count=0):
        thought = self.db.session.query(ThoughtList).all()
        thought = sorted(thought, key=lambda x: (x.like - x.dislike))[:33][count]
        return thought
