from flask_restful import Resource, reqparse
from models.quiz import QuizModel

class Quiz(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'quiz_id',
        type=int,
        required=True,
        help='An error occurred - \'quiz_id\' was empty'
    )
    parser.add_argument('gained_credit', type=int)

    def get(self):
        request_data = Quiz.parser.parse_args()

        try:
            quiz = QuizModel.find_by_id(request_data['quiz_id'])
        except:
            return {'message': 'An error occurred while reading the quiz ID from the database'}, 500
        
        if quiz:
            return quiz.json()
        return {'message': 'Quiz with the ID {} not found'.format(request_data['quiz_id'])}, 404
    
    def put(self):
        request_data = Quiz.parser.parse_args()
        
        if request_data['gained_credit'] == None:
            return {'message': 'An error occurred - \'gained_credit\' was empty'}

        try:
            if not QuizModel.find_by_id(request_data['quiz_id']):
                return {'message': 'Quiz with ID {} doesn\'t exist in the database'}.format(request_data['quiz_id']), 404
        except:
            return {'message': 'An error occurred while reading the quiz ID from the database'}, 500

        # there is, currently, only the option to update the item in the database: all test data is inserted prior to the app starting and we have no need to insert any data during runtime yet
        try:
            QuizModel.update_db(self, "UPDATE quizzes SET gained_credit=? WHERE quiz_id=?", (request_data['gained_credit'], request_data['quiz_id']))
        except:
            return {'message': 'An error occurred while updating the quiz in the database'}, 500
