import sqlite3
from models.answer import AnswerModel

class QuizModel:
    def __init__(self, quiz_id, test_id, order_num, credit_value, gained_credit, quiz_type, text_body, path_to_attachment, title, instructions):
        self.quiz_id = quiz_id
        self.test_id = test_id
        self.order_num = order_num
        self.credit_value = credit_value
        self.gained_credit = gained_credit
        self.type = quiz_type # 'type' is a key word in Python
        self.text_body = text_body
        self.path_to_attachment = path_to_attachment
        self.title = title
        self.instructions = instructions
    
    def json(self, withAnswers=True): # This parameter exists as, ideally, we'd use a GET request which specifies if these are true in order to prevent getting data we don't need and slowing down the request - they're 'True' for now so we can perform tests

        # creates a list of the answers to this question
        answers = []
        if withAnswers:
            for answer in AnswerModel.query_db(AnswerModel, "SELECT * FROM answers WHERE quiz_id=?", (self.quiz_id,)):
                answers.append(AnswerModel(*answer).json())

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
            'answers': answers
        }

    def query_db(self, query, args):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, args).fetchall()

        connection.close()

        return result

    @classmethod
    def find_by_id(cls, quiz_id):
        result = cls.query_db(cls, "SELECT * FROM quizzes WHERE quiz_id=?", (quiz_id,))

        if result:
            quiz = cls(*result[0])
        else:
            quiz = None
        
        return quiz