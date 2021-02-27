from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file
import sqlite3
import os

app = Flask(__name__)

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
	return render_template('tests-menu.html')

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