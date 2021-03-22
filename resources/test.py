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
    parser.add_argument('topic_id', type=int)
    parser.add_argument('is_unlocked', type=bool)
    parser.add_argument('max_credit', type=int)
    parser.add_argument('order_num', type=int)
    parser.add_argument('gained_credit', type=int)
    parser.add_argument('pass_credit', type=int)
    parser.add_argument('time_limit', type=str) # is there a way to convert a string to an SQL 'TIME' data type?
    parser.add_argument('description', type=str)
    parser.add_argument('is_retakeable', type=bool)
    parser.add_argument('is_official', type=bool)

    def get(self):
        request_data = Test.parser.parse_args()

        try:
            test = TestModel.find_by_id(request_data['test_id'])
        except:
            return {'message': 'An error occurred while reading the test ID from the database'}, 500
        
        if test:
            return test.json()
        return {'message': 'Test with the ID {} not found'.format(request_data['test_id'])}, 404
    
    def put(self):
        request_data = Test.parser.parse_args()
        test = TestModel.find_by_id(request_data['test_id'])
        
        try:
            if not test:
                test = TestModel(**request_data)
            else: # if 'test' is defined, this means there's an existing record under this ID, so update it with the values we have
                if request_data['test_id'] != None:
                    test.test_id = request_data['test_id']
                
                if request_data['topic_id'] != None:
                    test.topic_id = request_data['topic_id']
                
                if request_data['is_unlocked'] != None:
                    test.is_unlocked = request_data['is_unlocked']
                
                if request_data['max_credit'] != None:
                    test.max_credit = request_data['max_credit']
                
                if request_data['order_num'] != None:
                    test.order_num = request_data['order_num']
                
                if request_data['gained_credit'] != None:
                    test.gained_credit = request_data['gained_credit']
                
                if request_data['pass_credit'] != None:
                    test.pass_credit = request_data['pass_credit']
                
                if request_data['time_limit'] != None:
                    test.time_limit = request_data['time_limit']
                
                if request_data['description'] != None:
                    test.description = request_data['description']
                
                if request_data['is_retakeable'] != None:
                    test.is_retakeable = request_data['is_retakeable']
                
                if request_data['is_official'] != None:
                    test.is_official = request_data['is_official']
        except:
            return {'message': 'An error occurred while reading the test ID from the database'}, 500

        try:
            test.save_to_database()
            return test.json()
        except:
            return {'message': 'An error occurred while updating the test in the database'}, 500

    def delete(self):
        request_data = TestModel.parser.parse_args()
        test = TestModel.find_by_id(request_data['test_id'])

        if test:
            test.delete_from_database()

        return {'message': 'Test with ID {} deleted.'.format(request_data['test_id'])}, 200