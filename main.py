import random
from constants import db, logging
from database import ManagementDataBase
from sidedialogues import SideDialogues
from top import Top
from reflection import Reflection
from userthoughts import UserThought
from helper import Helps


class Main_class():
    def __init__(self, res, req):
        self.res = res
        self.db = db
        self.req = req
        self.management = ManagementDataBase(self.db)
        self.user_id = req['session']['user_id']
        self.payload = False
        if self.management.check_is_user(self.user_id):
            self.management.add_new_user(self.user_id)
        self.user = self.management.get_user(self.user_id)

    def start(self):
        text, tts, buttons = "", "", []
        if self.req['session']['new']:
            if not self.user.contribution:
                text, tts, buttons = "Привет Взнос", "Привет Взнос", []
                return
            else:
                text, tts, buttons = "С возвращением", "С возвращением", []
                return
        else:
            if self.req['request'].get("original_utterance"):
                command = self.req['request']["original_utterance"].strip()
                tokens = self.req['request']['nlu']['tokens']
                self.payload = False
            else:
                command = self.req['request']["payload"]["text"]
                tokens = list(map(lambda x: x.lower(), self.req['request']["payload"]["text"].split()))
                self.payload = True
            command = command.lower()
            if not self.user.contribution:
                user = UserThought(db, self.user)
                text, tts, buttons = user.get_contribution(command)
            elif self.user.first_help_num <= 3:
                helps = Helps(self.db, self.user)
                text, tts, buttons = helps.get_first_helps()
            else:
                self.way(tokens, command, self.payload)

        self.res['response']['text'] = text
        self.res['response']['tts'] = tts
        self.res['response']['buttons'] = buttons[:]
        return self.res

    def way(self, tokens, command, payload):

        check_element = SideDialogues(self.req, self.res)
        check = check_element.get_answer(tokens, command, payload)
        if check:
            self.res['response']['text'] = check[0]
            self.res['response']['tts'] = check[1]
            self.res['response']['buttons'] = check[2]
        else:
            if self.user.passage_num == 0:
                "меню"
            elif self.user.passage_num == 1:
                "Добавить"
            elif self.user.passage_num == 2:
                "Мои мысли"
            elif self.user.passage_num == 3:
                "Чужые мысли"
            elif self.user.passage_num == 4:
                top = Top(self.db, self.user)
                top.way(tokens)
                "Топ"
        return self.res

    def get_response(self):
        if self.req['session']["message_id"] >= 20 and not self.user['pls_like'] and self.user["passage_num"] != 0:
            self.user['pls_like'] = True

            if self.res['response'].get('tts'):
                self.res['response'][
                    'text'] = "Понравился навык? Оцени, пожалуйста) Твоё мнение для меня на вес золота.\n\n" + \
                              self.res['response']['text']
                self.res['response']['tts'] = "Понр+авился н+авык? Оцени, пож+алуйста)" \
                                              " Тво+ё мн+ение для мен+я на в+ес з+олота. sil <[500]>" + \
                                              self.res['response']['tts']
            else:
                text = self.res['response']['text'][:]
                self.res['response'][
                    'text'] = "Понравился навык? Оцени, пожалуйста) Твоё мнение для меня на вес золота.\n\n" + text
                self.res['response'][
                    'tts'] = "Понр+авился н+авык? Оцен+и, пож+алуйста) Тво+ё мн+ение для мен+я на в+ес з+олота.\n\n" + \
                             text
            buttons = self.res['response']['buttons'][:]
            buttons.insert(0, {
                "title": "Оценить навык",
                "url": "https://dialogs.yandex.ru/store/skills/376e3bb3-prokachaj-leksiko",
                "hide": True
            })
            self.res['response']['buttons'] = buttons

        return self.res
