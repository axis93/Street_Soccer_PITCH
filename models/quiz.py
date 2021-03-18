from models.answer import AnswerModel
from database import database

class QuizModel(database.Model):
    __tablename__ = 'quizzes'

    quiz_id = database.Column(database.Integer, primary_key=True, nullable=False)
    test_id = database.Column(database.Integer, nullable=False)
    order_num = database.Column(database.Integer, nullable=False)
    credit_value = database.Column(database.Integer, nullable=False)
    gained_credit = database.Column(database.Integer)
    quiz_type = database.Column(database.String)
    text_body = database.Column(database.String)
    path_to_attachment = database.Column(database.String)
    title = database.Column(database.String(100))
    instructions = database.Column(database.String)

    def __init__(self, quiz_id, test_id, order_num, credit_value, gained_credit, quiz_type, text_body, path_to_attachment, title, instructions):
        self.quiz_id = quiz_id
        self.test_id = test_id
        self.order_num = order_num
        self.credit_value = credit_value
        self.gained_credit = gained_credit
        self.quiz_type = quiz_type # 'type' is a key word in Python
        self.text_body = text_body
        self.path_to_attachment = path_to_attachment
        self.title = title
        self.instructions = instructions
    
    def json(self):
        return {
            'quiz_id': self.quiz_id,
            'test_id': self.test_id,
            'order_num': self.order_num,
            'credit_value': self.credit_value,
            'gained_credit': self.gained_credit,
            'type': self.type,
            'text_body': self.text_body,
            'path_to_attachment': self.path_to_attachment,
            'title': self.title,
            'instructions': self.instructions,
            'answers': [a for a in AnswerModel.get_all()]
        }

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def update_db(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, quiz_id):
        return cls.query.filter_by(quiz_id=quiz_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()