  
from flask import Flask, render_template, flash, redirect, url_for, request,send_from_directory, send_file
import sqlite3
import json
from os import path


app = Flask(__name__)


@app.route('/')
def index():
#This is the main point of the application, the home page or if you prefer the page before registration
	return render_template('home.html')

@app.route('/file-system/')
def filesystem():

	return render_template('file-system.html')

@app.route('/login/')
def login():

	return render_template('login.html')


@app.route('/register/')
def register():

	return render_template('register.html')


@app.route('/quiz-info/')
def quizinfo():

	return render_template('quiz-info.html')


@app.route('/quiz-multiple-choice/')
def quiztmultiplechoice():

	return render_template('quiz-multiple-choice.html')

@app.route('/test-result/')
def testresult():

	return render_template('test-result.html')

@app.route('/test-menu/')
def testtmenu():

	return render_template('test-menu.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)