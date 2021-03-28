from flask import Flask, render_template
from flask_restful import Api
from flask_jsglue import JSGlue
from database import database, insert_queries
from resources.topic import Topic
from resources.formativeAssessment import FormativeAssessment
from resources.test import Test
from resources.quiz import Quiz
from resources.answer import Answer
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
jsglue = JSGlue(app)
database.init_app(app) # this should be in the 'if is main' at the bottom of this file so that the database isn't re-initialized if 'app.py' is imported from another file, but that would mean that the database is never initialized if we run the app via Flask instead of Python

@app.before_first_request
def create_tables():
	if '--create' in sys.argv or '-c' in sys.argv:
		database.create_all()

	if '--insert' in sys.argv or '-i' in sys.argv:
		for query in insert_queries:
			database.session.execute(query) 
		database.session.commit()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/file-system')
def filesystem():
	return render_template('file-system.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/quiz')
def quiz_page():
	return render_template('quiz-page.html')

@app.route('/test-result')
def testresult():
	return render_template('test-result.html')

@app.route('/tests-test')
def testtest():
	return render_template('tests-testing.html')

@app.route('/test-menu')
def testmenu():
	return render_template('tests-menu.html')

@app.route('/formative-assessment')
def formativeAssessment():
	return render_template('formative-assessment.html')

api.add_resource(Topic, '/topics')
api.add_resource(FormativeAssessment, '/formativeAssessments')
api.add_resource(Test, '/tests')
api.add_resource(Quiz, '/quizzes')
api.add_resource(Answer, '/answers')

if __name__ == "__main__":
	
	app.run(host='127.0.0.1', debug=True)