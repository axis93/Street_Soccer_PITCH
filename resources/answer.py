from flask_restful import Resource, reqparse
from models.answer import AnswerModel

class Answer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'answer_id',
        type=int,
        required=True,
        help='An error occurred - \'answer_id\' was empty'
    )
    parser.add_argument('is_selected', type=bool)

    def get(self):
        request_data = Answer.parser.parse_args()

        try:
            topic = AnswerModel.find_by_id(request_data['answer_id'])
        except:
            return {'message': 'An error occurred while reading the answer ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'Answer with the ID {} not found'.format(request_data['answer_id'])}, 404

    def put(self):
        request_data = Answer.parser.parse_args()
        
        if request_data['is_selected'] == None:
            return {'message': 'An error occurred - \'is_selected\' was empty'}

        try:
            if not AnswerModel.find_by_id(request_data['answer_id']):
                return {'message': 'Answer with ID {} doesn\'t exist in the database'}.format(request_data['answer_id']), 404
        except:
            return {'message': 'An error occurred while reading the answer ID from the database'}, 500

        # there is, currently, only the option to update the item in the database: all test data is inserted prior to the app starting and we have no need to insert any data during runtime yet
        try:
            AnswerModel.update_db(self, "UPDATE answers SET is_selected=? WHERE answer_id=?", (request_data['is_selected'], request_data['answer_id']))
        except:
            return {'message': 'An error occurred while updating the answer in the database'}, 500

