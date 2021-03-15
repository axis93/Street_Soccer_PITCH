import sqlite3

class FormativeAssessmentModel:
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
    def find_by_id(cls, fa_id):
        result = cls.query_db(cls, "SELECT * FROM formativeAssessments WHERE fa_id=?", (fa_id,))

        if result:
            assessment = cls(*result[0])
        else:
            assessment = None
        
        return assessment