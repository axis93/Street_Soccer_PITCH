from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file, g
from flask_restful import Api
from resources.topic import Topic
import sqlite3
import os
import json

app = Flask(__name__)
api = Api(app)

db_location = 'database.db'

def get_db():
	db = getattr(g, 'db', None)
	if db is None:
		db = sqlite3.connect(db_location)
		g.db = db
	return db


@app.teardown_appcontext
def close_db_connection(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

def init_db(queries):
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())

		if db and queries:
			for query in queries:
				db.cursor().execute(query)

		db.commit()


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

@app.route('/quiz-info')
def quizinfo():
	return render_template('quiz-info.html')

@app.route('/quiz-multiple-choice')
def quiztmultiplechoice():
	return render_template('quiz-multiple-choice.html')

@app.route('/test-result')
def testresult():
	return render_template('test-result.html')

@app.route('/test-menu')
def testmenu():
	topics=[]
	topic1 = ['Children Protection Programme',[1,2,3,4,5]]
	topics.append(topic1)
	for x in range(1,11):
		topic=[]
		topicName='Topic'+ str(x)
		topic.append(topicName)
		tests=[]
		for y in range(1,5):
			tests.append(y)
		topic.append(tests)
		topics.append(topic)
	return render_template('tests-menu.html',topics=topics)

@app.route('/foo-bar')
def feandbetest():
	return render_template('fe-and-be-test.html')

api.add_resource(Topic, '/topics/<string:topic_id>')
api.add_resource(Topic, '/formative-assessments/<string:fa_id>')

"""
use Ctrl+F5 to clear the cache and refresh

caching stops the static files from being refreshed when the page
is refreshed

this was an attempt to clear the browser cache for this page
automatically so we don't have to do it manually everytime we test
changes on a page

@app.context_processor
def override_url_for():
	return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
	if endpoint == 'static':
		filename = values.get('filename', None)
		if filename:
			file_path = os.path.join(app.root_path, endpoint, filename)
			values['q'] = int(os.stat(file_path).st_mtime)
	return url_for(endpoint, **values)
"""

if __name__ == "__main__":
	app.run(host='127.0.0.1', debug=True)