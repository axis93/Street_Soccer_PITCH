from flask_restful import Resource
from models.formativeAssessment import FormativeAssessmentModel

class FormativeAssessment(Resource):
    def get(self, fa_id):
        try:
            assessment = FormativeAssessmentModel.find_by_id(fa_id)
        except:
            return {'message': 'An error occurred while reading the topic ID from the database'}, 500
        
        if assessment:
            return assessment.json()
        return {'message': 'Formative assessment with the ID {} not found'.format(fa_id)}, 404
