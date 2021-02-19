# Street Soccer Pitch

## The application is built using Python Flask 

### In order to use run this application on your local machine you will need to install the following packages from comand line

### Navigate to the main directory > sudo apt install virtualenv (this is for Linux users - search for windows commands)

### Once it has been installed do the following:

### virtualenv env 
### source env/bin/activate
### This will open the virtualenv "env" that will be used for development and will make sure that everybody is going to use the same modules
### Before closing the application or to push any change, make sure you deactivate the virtualenv by typing "deactivate" in the terminal, then push your changes

### To run the application do the following:

### export FLASK_APP=Street_Soccer_PITCH.py
### export FLASK_ENV=development
### python3 -m flask run --host=0.0.0.0

### Typing :5000 on a web browser should serve the purpose and you should be able to redirected to the home page