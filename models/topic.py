from database import database

class TopicModel(database.Model):
    __tablename__ = 'topics'

    topic_id = database.Column(database.Integer, primary_key=True, nullable=False)
    is_unlocked = database.Column(database.Boolean, nullable=False)
    name = database.Column(database.String(50), nullable=False)
    needed_credit = database.Column(database.Integer)

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

    def save_to_database(self, query, args=None):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()