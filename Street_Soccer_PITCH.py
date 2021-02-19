from flask import Flask, render_template, flash, redirect, url_for, request,send_from_directory, send_file
import sqlite3
import json
from os import path


app = Flask(__name__)


@app.route('/')
def index():
#This is the main point of the application, the home page or if you prefer the page before registration
	return render_template('index.html')

@app.route('/file-system/')
def file-system():

	return render_template('file-system.html')

@app.route('/login/')
def login():

	return render_template('login.html')


@app.route('/register/')
def register():

	return render_template('register.html')


@app.route('/quiz-info/')
def quiz-info():

	return render_template('quiz-info.html')


@app.route('/quiz-multiple-choice/')
def quiz-multiple-choice():

	return render_template('quiz-multiple-choice.html')

@app.route('/test-result/')
def test-result():

	return render_template('test-result.html')

@app.route('/test-menu/')
def test-menu():

	return render_template('test-menu.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)