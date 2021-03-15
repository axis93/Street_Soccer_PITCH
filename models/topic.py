import sqlite3
from models.test import TestModel
from models.formativeAssessment import FormativeAssessmentModel

class TopicModel:
    def __init__(self, topic_id, is_unlocked, name, needed_credit):
        self.topic_id = topic_id
        self.is_unlocked = is_unlocked
        self.name = name
        self.needed_credit = needed_credit
    
    def json(self, withTests=True, withQuizzes=True, withAnswers=True, withFormativeAssessments=True): # This parameter exists as, ideally, we'd use a GET request which specifies if these are true in order to prevent getting data we don't need and slowing down the request - they're 'True' for now so we can perform tests
        tests = []
        if withTests:
            for test in TestModel.query_db(TestModel, "SELECT * FROM tests WHERE topic_id=?", (self.topic_id,)):
                tests.append(TestModel(*test).json(withQuizzes=withQuizzes, withAnswers=withAnswers))

        formativeAssessments = []
        if withFormativeAssessments:
            for fa in FormativeAssessmentModel.query_db(FormativeAssessmentModel, "SELECT * FROM formativeAssessments WHERE topic_id=?", (self.topic_id,)):
                formativeAssessments.append(FormativeAssessmentModel(*fa).json())

        return {
            'topic_id': self.topic_id,
            'is_unlocked': self.is_unlocked,
            'name': self.name,
            'needed_credit': self.needed_credit,
            'tests': tests,
            'formative_assessments': formativeAssessments
        }

    def query_db(self, query, args=None):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        if args:
            result = cursor.execute(query, args).fetchall()
        else:
            result = cursor.execute(query).fetchall()

        connection.close()

        return result

    @classmethod
    def find_by_id(cls, topic_id):
        result = cls.query_db(cls, "SELECT * FROM topics WHERE topic_id=?", args=(topic_id,))

        if result:
            topic = cls(*result[0])
        else:
            topic = None
        
        return topic

    @classmethod
    def get_topics(cls):
        result = cls.query_db(cls, "SELECT * FROM topics")

        topics = []
        if result:
            for topic in result:
                topics.append(cls(*topic))
        
        return topics