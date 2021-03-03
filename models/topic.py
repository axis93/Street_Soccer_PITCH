import sqlite3

class TopicModel:
    def __init__(self, topic_id, is_unlocked, name, needed_credit):
        self.topic_id = topic_id
        self.is_unlocked = is_unlocked
        self.name = name
        self.needed_credit = needed_credit
    
    def json(self):
        return {'topic_id': self.topic_id, 'is_unlocked': self.is_unlocked, 'name': self.name, 'needed_credit': self.needed_credit}

    def query_db(self, query, args):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, args)
        row = result.fetchone()

        connection.close()

        return row

    @classmethod
    def find_by_id(cls, topic_id):
        result = cls.query_db(cls, "SELECT * FROM topics WHERE topic_id=?", (topic_id,))

        if result:
            topic = cls(*result)
        else:
            topic = None
        
        return topic