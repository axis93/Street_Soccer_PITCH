from flask_restful import Resource, reqparse
from models.test import TestModel

class Test(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'test_id',
        type=int,
        required=True,
        help='An error occurred - \'test_id\' was empty'
    )
    parser.add_argument('gained_credit', type=int)

    def get(self):
        request_data = Test.parser.parse_args()

        try:
            topic = TestModel.find_by_id(request_data['test_id'])
        except:
            return {'message': 'An error occurred while reading the test ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'Test with the ID {} not found'.format(request_data['test_id'])}, 404
    
    def put(self):
        request_data = Test.parser.parse_args()
        
        if request_data['gained_credit'] == None:
            return {'message': 'An error occurred - \'gained_credit\' was empty'}

        try:
            if not TestModel.find_by_id(request_data['test_id']):
                return {'message': 'Test with ID {} doesn\'t exist in the database'}.format(request_data['test_id']), 404
        except:
            return {'message': 'An error occurred while reading the test ID from the database'}, 500

        # there is, currently, only the option to update the item in the database: all test data is inserted prior to the app starting and we have no need to insert any data during runtime yet
        try:
            TestModel.update_db(self, "UPDATE tests SET gained_credit=? WHERE test_id=?", (request_data['gained_credit'], request_data['test_id']))
        except:
            return {'message': 'An error occurred while updating the test in the database'}, 500
