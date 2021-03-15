import sqlite3
from models.quiz import QuizModel


class TestModel:
    def __init__(self, test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, time_limit, description, is_retakeable, is_official):
        self.test_id = test_id
        self.topic_id = topic_id
        self.is_unlocked = is_unlocked
        self.max_credit = max_credit
        self.order_num = order_num
        self.gained_credit = gained_credit
        self.pass_credit = pass_credit
        self.time_limit = time_limit
        self.description = description
        self.is_retakeable = is_retakeable
        self.is_official = is_official
    
    def json(self, withQuizzes=True, withAnswers=True): # This parameter exists as, ideally, we'd use a GET request which specifies if these are true in order to prevent getting data we don't need and slowing down the request - they're 'True' for now so we can perform tests
        quizzes = []
        if withQuizzes:
            for quiz in QuizModel.query_db(QuizModel, "SELECT * FROM quizzes WHERE test_id=?", (self.test_id,)):
                quizzes.append(QuizModel(*quiz).json(withAnswers=withAnswers))
        
        return {
            'test_id': self.test_id,
            'topic_id': self.topic_id,
            'is_unlocked': self.is_unlocked,
            'max_credit': self.max_credit,
            'order_num': self.order_num,
            'gained_credit': self.gained_credit,
            'pass_credit': self.pass_credit,
            'time_limit': self.time_limit,
            'description': self.description,
            'is_retakeable': self.is_retakeable,
            'is_official': self.is_official,
            'quizzes': quizzes
        }

    def query_db(self, query, args):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, args).fetchall()

        connection.close()

        return result

    def update_db(self, query, args):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute(query, args)

        connection.commit()
        connection.close()

    @classmethod
    def find_by_id(cls, test_id):
        result = cls.query_db(cls, "SELECT * FROM tests WHERE test_id=?", (test_id,))

        if result:
            test = cls(*result[0])
        else:
            test = None
        
        return test