from flask_restful import Resource
from models.answer import AnswerModel

class Answer(Resource):
    def get(self, answer_id):
        try:
            topic = AnswerModel.find_by_id(answer_id)
        except:
            return {'message': 'An error occurred while reading the answer ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'Answer with the ID {} not found'.format(answer_id)}, 404
