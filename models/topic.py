import sqlite3

class TopicModel:
    def __init__(self, topic_id, is_unlocked, name, needed_credit):
        self.topic_id = topic_id
        self.is_unlocked = is_unlocked
        self.name = name
        self.needed_credit = needed_credit
    
    @classmethod
    def find_by_id(cls, topic_id):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM topics WHERE topic_id=?"

        result = cursor.execute(query, (topic_id,))
        row = result.fetchone()
        if result:
            topic = cls(*row)
        else:
            topic = None
        
        connection.close()
        return topic
    
    def json(self):
        return {'topic_id': self.topic_id, 'is_unlocked': self.is_unlocked, 'name': self.name, 'needed_credit': self.needed_credit}