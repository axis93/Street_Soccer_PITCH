import sqlite3

class UserModel:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
    
    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            # the user's password should never be sent to the front end
            'email': self.email
        }

    def query_db(self, query, args):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, args)
        row = result.fetchone()

        connection.close()

        return row

    @classmethod
    def find_by_id(cls, user_id):
        result = cls.query_db(cls, "SELECT * FROM users WHERE user_id=?", (user_id,))

        if result:
            user = cls(*result)
        else:
            user = None
        
        return user