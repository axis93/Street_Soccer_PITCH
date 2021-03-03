from flask_restful import Resource
from models.topic import TopicModel

class Topic(Resource):
    def get(self, topic_id):
        #try:
        topic = TopicModel.find_by_id(topic_id)
        #except:
        #    return {'message': 'An error occurred while reading the topic ID from the database'}, 500
        
        if topic:
            return topic.json()
        return {'message': 'Topic with the ID {} not found'.format(topic_id)}, 404
