from flask_restful import Resource, reqparse
from models.formativeAssessment import FormativeAssessmentModel

class FormativeAssessment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'fa_id',
        type=int,
        required=True,
        help='An error occurred - \'fa_id\' was empty'
    )
    parser.add_argument('topic_id', type=int)
    parser.add_argument('is_unlocked', type=bool)
    parser.add_argument('order_num', type=int)
    parser.add_argument('gained_credit', type=int)
    parser.add_argument('answer', type=str)
    parser.add_argument('pass_credit', type=int)
    parser.add_argument('instructions', type=str)
    parser.add_argument('title', type=str)
    parser.add_argument('path_to_attachment', type=str)
    parser.add_argument('deadline', type=str) # is there a way to convert a string to an SQL 'TIME' data type?
    parser.add_argument('reviewer_comment', type=str)
    parser.add_argument('is_marked', type=bool)

    def get(self):
        request_data = FormativeAssessment.parser.parse_args()

        try:
            formativeAssessment = FormativeAssessmentModel.find_by_id(request_data['fa_id'])
        except:
            return {'message': 'An error occurred while reading the formative assessment ID from the database'}, 500
        
        if formativeAssessment:
            return formativeAssessment.json()
        return {'message': 'Formative assessment with the ID {} not found'.format(request_data['fa_id'])}, 404

    def put(self):
        request_data = FormativeAssessment.parser.parse_args()
        formativeAssessment = FormativeAssessmentModel.find_by_id(request_data['fa_id'])

        try:
            if not formativeAssessment:
                formativeAssessment = FormativeAssessmentModel(**request_data)
            else:
                formativeAssessment.fa_id = request_data['fa_id']
                formativeAssessment.topic_id = request_data['topic_id']
                formativeAssessment.is_unlocked = request_data['is_unlocked']
                formativeAssessment.order_num = request_data['order_num']
                formativeAssessment.gained_credit = request_data['gained_credit']
                formativeAssessment.answer = request_data['answer']
                formativeAssessment.pass_credit = request_data['pass_credit']
                formativeAssessment.instructions = request_data['instructions']
                formativeAssessment.title = request_data['title']
                formativeAssessment.path_to_attachment = request_data['path_to_attachment']
                formativeAssessment.deadline = request_data['deadline']
                formativeAssessment.reviewer_comment = request_data['reviewer_comment']
                formativeAssessment.is_marked = request_data['is_marked']
        except:
            return {'message': 'An error occurred while reading the formative assessment ID from the database'}, 500

        try:
            formativeAssessment.save_to_database()
            return formativeAssessment.json()
        except:
            return {'message': 'An error occurred while updating the formative assessment in the database'}, 500

    def delete(self):
        request_data = FormativeAssessment.parser.parse_args()
        formativeAssessment = FormativeAssessmentModel.find_by_id(request_data['fa_id'])

        if formativeAssessment:
            formativeAssessment.delete_from_database()

        return {'message': 'Formative assessment with ID {} deleted.'.format(request_data['fa_id'])}, 200