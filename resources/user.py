from flask_restful import Resource
from models.user import UserModel

class User(Resource):
    def get(self, user_id):
        try:
            topic = UserModel.find_by_id(user_id)
        except:
            return {'message': 'An error occurred while reading the user ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'User with the ID {} not found'.format(user_id)}, 404
