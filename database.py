from constants import *
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contribution = db.Column(db.Boolean, unique=False, nullable=False)
    first_help_num = db.Column(db.Integer, unique=False, nullable=False)
    first_top = db.Column(db.Boolean, unique=False, nullable=False)
    first_reflection = db.Column(db.Boolean, unique=False, nullable=False)
    first_my_thought = db.Column(db.Boolean, unique=False, nullable=False)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    points = db.Column(db.Integer, unique=False, nullable=False)
    passage_num = db.Column(db.Integer, unique=False, nullable=False)
    top_num = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<User {} {} {} {}>".format(self.id, self.age, self.step, self.step_test)


class ThoughtList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, unique=False, nullable=False)
    text = db.Column(db.String, unique=False, nullable=False)
    like = db.Column(db.Integer, unique=False, nullable=False)
    dislike = db.Column(db.Integer, unique=False, nullable=False)


class ManagementDataBase():
    def __init__(self, db):
        self.db = db

    def add_new_thought(self, user_id, text):
        thought = ThoughtList(user_id=user_id, creation_date=datetime.now().strftime("%Y-%m-%d-%H.%M.%S"), text=text,
                              like=0, dislike=0)
        self.db.session.add(thought)
        self.db.session.commit()

    def add_new_user(self, user_id):
        user = User(user_id=user_id, age=0, step=0, step_test=0)
        self.db.session.add(user)
        self.db.session.commit()

    def check_is_user(self, user_id):
        user = self.db.session.query(User).filter_by(user_id=user_id).first()
        if user:
            return True
        return False

    def get_user(self, user_id):
        user = self.db.session.query(User).filter_by(user_id=user_id).first()
        return user

    def get_users_thoughts(self, user_id, count=0):
        thought = self.db.session.query(ThoughtList).filter_by(user_id=user_id).all()[count]
        return thought

    def get_thought(self, thought_id):
        thought = self.db.session.query(ThoughtList).filter_by(id=thought_id).first()
        return thought

    def delete_user_thought(self, thought_id):
        thought = self.db.session.query(ThoughtList).filter_by(id=thought_id).first()
        self.db.session.delete(thought)
        self.db.session.commit()
        return True

    def get_top_thought(self, count=0):
        thought = self.db.session.query(ThoughtList).all()
        thought = sorted(thought, key=lambda x: (x.like - x.dislike))[:33][count]
        return thought


if __name__ == '__main__':
    db.create_all()
