from database import database

class FormativeAssessmentModel(database.Model):
    __tablename__ = 'formativeAssessments'

    fa_id = database.Column(database.Integer, primary_key=True, nullable=False)
    topic_id = database.Column(database.Integer)
    is_unlocked = database.Column(database.Boolean, nullable=False)
    order_num = database.Column(database.Integer, nullable=False)
    gained_credit = database.Column(database.Integer)
    answer = database.Column(database.String)
    pass_credit = database.Column(database.Integer)
    instructions = database.Column(database.String)
    title = database.Column(database.String(100), nullable=False)
    path_to_attachment = database.Column(database.String)
    deadline = database.Column(database.String)
    reviewer_comment = database.Column(database.String)
    is_marked = database.Column(database.Boolean)

    def __init__(self, fa_id, topic_id, is_unlocked, order_num, gained_credit, answer, pass_credit, instructions, title, path_to_attachment, deadline, reviewer_comment, is_marked):
        self.fa_id = fa_id
        self.topic_id = topic_id
        self.is_unlocked = is_unlocked
        self.order_num = order_num
        self.gained_credit = gained_credit
        self.answer = answer
        self.pass_credit = pass_credit
        self.instructions = instructions
        self.title = title
        self.path_to_attachment = path_to_attachment
        self.deadline = deadline
        self.reviewer_comment = reviewer_comment
        self.is_marked = is_marked
    
    def json(self):
        return {
            'fa_id': self.fa_id,
            'topic_id': self.topic_id,
            'is_unlocked': self.is_unlocked,
            'order_num': self.order_num,
            'gained_credit': self.gained_credit,
            'answer': self.answer,
            'pass_credit': self.pass_credit,
            'instructions': self.instructions,
            'title': self.title,
            'path_to_attachment': self.path_to_attachment,
            'deadline': self.deadline,
            'reviewer_comment': self.reviewer_comment,
            'is_marked': self.is_marked
        }

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_database(self, query, args):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, fa_id):
        return cls.query.filter_by(fa_id=fa_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_all_for_topic(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id).all()