from flask_restful import Resource
from models.test import TestModel

class Test(Resource):
    def get(self, test_id):
        #try:
        topic = TestModel.find_by_id(test_id)
        #except:
        #    return {'message': 'An error occurred while reading the test ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'Test with the ID {} not found'.format(test_id)}, 404
