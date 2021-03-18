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
    parser.add_argument('quiz_id', type=int)
    parser.add_argument('body', type=str)
    parser.add_argument('is_correct', type=bool)
    parser.add_argument('path_to_attachment', type=str)
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
        answer = AnswerModel.find_by_id(request_data['answer_id'])

        try:
            if not answer:
                answer = AnswerModel(**request_data)
            else:
                answer.answer_id = request_data['answer_id']
                answer.quiz_id = request_data['quiz_id']
                answer.body = request_data['body']
                answer.is_correct = request_data['is_correct']
                answer.path_to_attachment = request_data['path_to_attachment']
                answer.is_selected = request_data['is_selected']
        except:
            return {'message': 'An error occurred while reading the answer ID from the database'}, 500
        
        try:
            answer.save_to_database()
            return answer.json()
        except:
            return {'message': 'An error occurred while updating the answer in the database'}, 500

    def delete(self):
        request_data = Answer.parser.parse_args()
        answer = AnswerModel.find_by_id(request_data['answer_id'])

        if answer:
            answer.delete_from_database()

        return {'message': 'Answer with ID {} deleted.'.format(request_data['answer_id'])}, 200


