# Street Soccer PITCH
## Run the app for the first time 
***(Windows, with virtual env, run locally, in development mode)***

- `py -m venv env` *get virtual env*
- `.\env\Scripts\activate` *activate virtual env*
- `pip install -r requirements.txt` *install all required packages (flask etc.)*
- `set FLASK_APP=app.py` *activate .py file to be the application*
- `set FLASK_ENV=development` *activate development mode*
- `python -m flask run --host=0.0.0.0` *run the application*
- visit "http://localhost:5000/" *to see the application*
- `deactivate` *close the virtual environment after you close the app*

## Run the app with all environment setup

- `.\env\Scripts\activate` *activate virtual env*
- `set FLASK_APP=app.py` *activate .py file to be the application*
- `set FLASK_ENV=development` *activate development mode*
- `python -m flask run --host=0.0.0.0` *run the application*
- visit "http://localhost:5000/" *to see the application*
- `deactivate` *close the virtual environment after you close the app*

/* *(All the commands (`command`) above are executed via the command line)* */