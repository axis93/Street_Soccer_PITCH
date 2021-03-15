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
    parser.add_argument('gained_credit', type=int)

    def get(self):
        request_data = FormativeAssessment.parser.parse_args()

        try:
            assessment = FormativeAssessmentModel.find_by_id(request_data['fa_id'])
        except:
            return {'message': 'An error occurred while reading the formative assessment ID from the database'}, 500
        
        if assessment:
            return assessment.json()
        return {'message': 'Formative assessment with the ID {} not found'.format(request_data['fa_id'])}, 404

    def put(self):
        request_data = FormativeAssessment.parser.parse_args()
        
        if request_data['gained_credit'] == None:
            return {'message': 'An error occurred - \'gained_credit\' was empty'}

        try:
            if not FormativeAssessmentModel.find_by_id(request_data['fa_id']):
                return {'message': 'Formative assessment with ID {} doesn\'t exist in the database'.format(request_data['fa_id'])}, 404
        except:
            return {'message': 'An error occurred while reading the formative assessment ID from the database'}, 500

        # there is, currently, only the option to update the item in the database: all test data is inserted prior to the app starting and we have no need to insert any data during runtime yet
        try:
            FormativeAssessmentModel.update_db(self, "UPDATE formativeAssessments SET gained_credit=? WHERE fa_id=?", (request_data['gained_credit'], request_data['fa_id']))
        except:
            return {'message': 'An error occurred while updating the formative assessment in the database'}, 500