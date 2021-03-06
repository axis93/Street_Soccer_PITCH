from flask_restful import Resource, reqparse
from models.topic import TopicModel

class Topic(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)

    def get(self):
        request_data = Topic.parser.parse_args()

        try:
            if request_data['id']:
                topic = TopicModel.find_by_id(request_data['id'])
                return topic.json()
            else:
                topic = TopicModel.get_topics()
                return {'topics': t.json() for t in topic}
        except:
            return {'message': 'An error occurred while reading the topic ID from the database'}, 500

        return {'message': 'Topic with the ID {} not found'.format(request_data['id'])}, 404
