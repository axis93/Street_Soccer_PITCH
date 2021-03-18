from models.quiz import QuizModel
from database import database

class TestModel(database.Model):
    __tablename__ = 'tests'

    test_id = database.Column(database.Integer, primary_key=True, nullable=False)
    topic_id = database.Column(database.Integer, database.ForeignKey('topics.topics_id'), nullable=False)
    is_unlocked = database.Column(database.Boolean)
    max_credit = database.Column(database.Integer, nullable=False)
    order_num = database.Column(database.Integer, nullable=False)
    gained_credit = database.Column(database.Integer)
    pass_credit = database.Column(database.Integer, nullable=False)
    time_limit = database.Column(database.Time)
    description = database.Column(database.String)
    is_retakeable = database.Column(database.Boolean)
    is_official = database.Column(database.Boolean, nullable=False)

    topic = database.relationship('TopicModel')
    quizzes = database.relationship('QuizModel', lazy='dynamic')

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
    
    def json(self):
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
            'quizzes': [q.json() for q in self.quizzes.all()]
        }

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_database(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, test_id):
        return cls.query.filter_by(test_id=test_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_all_for_topic(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id).all()