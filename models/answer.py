import sqlite3

class AnswerModel:
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

        connection .commit()
        connection.close()

    @classmethod
    def find_by_id(cls, answer_id):
        result = cls.query_db(cls, "SELECT * FROM answers WHERE answer_id=?", (answer_id,))

        if result:
            answer = cls(*result[0])
        else:
            answer = None
        
        return answer