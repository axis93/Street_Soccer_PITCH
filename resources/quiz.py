from flask_restful import Resource
from models.quiz import QuizModel

class Quiz(Resource):
    def get(self, quiz_id):
        try:
            quiz = QuizModel.find_by_id(quiz_id)
        except:
            return {'message': 'An error occurred while reading the quiz ID from the database'}, 500
        
        if quiz:
            return quiz.json()
        return {'message': 'Quiz with the ID {} not found'.format(quiz_id)}, 404
