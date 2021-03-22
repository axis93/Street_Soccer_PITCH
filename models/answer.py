from database import database

class AnswerModel(database.Model):
    __tablename__ = 'answers'

    answer_id = database.Column(database.Integer, primary_key=True, nullable=False)
    quiz_id = database.Column(database.Integer, database.ForeignKey('quizzes.quiz_id'), nullable=False)
    body = database.Column(database.String)
    is_correct = database.Column(database.Boolean)
    path_to_attachment = database.Column(database.String)
    is_selected = database.Column(database.Boolean)

    quiz = database.relationship('QuizModel')

    def __init__(self, answer_id, quiz_id, body, is_correct, path_to_attachment, is_selected):
        self.answer_id = answer_id
        self.quiz_id = quiz_id
        self.body = body
        self.is_correct = is_correct
        self.path_to_attachment = path_to_attachment
        self.is_selected = is_selected
    
    def json(self):
        return {
            'answer_id': self.answer_id,
            'quiz_id': self.quiz_id,
            'body': self.body,
            'is_correct': self.is_correct,
            'path_to_attachment': self.path_to_attachment,
            'is_selected': self.is_selected,
        }

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_database(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, answer_id):
        return cls.query.filter_by(answer_id=answer_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_all_for_quiz(cls, quiz_id):
        return cls.query.filter_by(quiz_id=quiz_id).all()