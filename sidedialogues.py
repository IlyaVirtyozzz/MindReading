from helper import add_log_text
import random
from constants import data


class SideDialogues():
    def __init__(self, req, res):
        self.req = req
        self.res = res

    def get_answer(self, tokens, command, payload):
        text, tts, buttons = False, False, False
        if all(word in tokens for word in ["что", "умеешь"]):
            text, tts = data["ican"]
            buttons = []

        elif all(word in tokens for word in ["как", "дела"]) or all(
                word in tokens for word in ["как", "настроение"]):
            text, tts = [
                "Нормально, нормально нереально, не будем тратить время на житейские разговоры, приступим к делу.",
                "Норм+ально, норм+ально нере+ально,"
                " не б+удем тр+атить вр+емя на жит+ейские разгов+оры, прист+упим к д+елу."]
            buttons = []

        elif all(word in tokens for word in ["оценить", "навык"]):
            text, tts = [
                "Благодарю Тебя.",
                "Благодар+ю Теб+я."]
            buttons = []

        # elif any(word in tokens for word in ["спасибо", "благодарю", "сенкс"]):
        #     text, tts = ["Тебе спасибо, что зашёл)",
        #                  "Тебе спас+ибо, что заш+ёл"]
        #     buttons = self.user["previous_buttons"]
        #     self.user['pls_like'] = True
        #     buttons_1 = buttons[:]
        #     buttons_1.insert(0, {
        #         "title": "Оценить навык",
        #         "url": "https://dialogs.yandex.ru/store/skills/376e3bb3-prokachaj-leksiko",
        #         "hide": True
        #     })
        #     buttons = buttons_1[:]

        elif all(word in tokens for word in ["как", "это"]) or all(
                word in tokens for word in ["почему", "так"]) or all(
            word in tokens for word in ["почему", "это"]):
            text, tts = ["Вот так вот)",
                         "Вот так вот"]
            buttons = []
        elif any(word in tokens for word in ["алиса", "alice", "алис"]):
            text, tts = [
                "Ой. Я не Алиса. Можно сказать, я её друг.",
                "Ой. Я не Ал+иса. Можно сказ+ать, я её др+уг."]
            buttons = []

        elif any(word in tokens for word in data['is_hello']):
            text, tts = random.choice(data['hello'])
            buttons = self.user["previous_buttons"]

        elif all(word in tokens for word in ["ты", "кто"]):
            text, tts = [
                "Я тот кто может научить Тебя полезным словам)",
                "Я тот кто м+ожет науч+ить Теб+я пол+езным слов+ам)"]
            buttons = self.user["previous_buttons"]

        elif all(word in tokens for word in ["ты", "мальчик"]):
            text, tts = [
                "Скорее всего, я навык мужского пола. Увы, так исторически сложилось.",
                "Скор+ее вс+его, я н+авык мужск+ого п+ола. Ув+ы, так истор+ически слож+илось."]
            buttons = self.user["previous_buttons"]

        elif all(word in tokens for word in ["как", "приложение", "называется"]) or all(
                word in tokens for word in ["как", "навык", "называется"]):
            text, tts = [
                "\"Прокачай Лексикон\" По-моему звучит прикольно)",
                "\"Прокач+ай Лексик+он\" По-м+оему звуч+ит прик+ольно!)"]
            buttons = []

        elif all(word in tokens for word in ["ау", "эй", "уау"]):
            text, tts = [
                "Да-да, я здесь.",
                "Да-да, я зд+есь."]
            buttons = []

        elif any(word in tokens for word in data['is_bye']):
            text, tts = random.choice(data['bye'])
            buttons = []

        elif any(word in command.split() for word in data['fuck_words']):
            text, tts = random.choice(data["fuck_answer"])
            buttons = []
            add_log_text(command)

        elif all(word in tokens for word in ["как", "тебя", "зовут"]) or all(
                word in tokens for word in ["как", "вас", "зовут"]):
            text, tts = ["Сам прихожу. А так, имени у меня нет)",
                         "Сам прихож+у. А т+ак, +имени у мен+я н+ет)"]
            buttons = []

        elif any(word in tokens for word in ["ясно", "понятно"]):
            text, tts = ["Хе-хе",
                         "Хе-хе"]
            buttons =[]
        if all([text, tts, buttons]):
            return text, tts, buttons
        else:
            return False
