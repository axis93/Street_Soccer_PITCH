# Street Soccer PITCH
## Run the app for the first time 
***(Windows, with virtualenv, run locally, in development mode)***

- `py -m venv env` *get virtual env*
    - *On Linux, if you're required to download virtualenv, use* `pip3 install virtualenv`
- `.\env\Scripts\activate` *activate virtual env*
- `pip install -r requirements.txt` *install all required packages (flask etc.)*
    - *On Linux, if pip isn't present in the virtualenv, try* `env/bin/python -m pip install -r requirements.txt`
- `set FLASK_APP=app.py` *activate .py file to be the application*
- *To create and populate the database, you need to run the app (via* `python app.py` *)*
    - *With either, or both, of the following arguments:*
        - `--create` *(or* `-c` *) to create the 'database.db' file*
        - `--insert` *(or* `-i` *) to populate 'database.db' with the test data*
        - *Can be used as so:* `python app.py -c -i`
    - *Once you've created the database, the app can, from now on, be run as normal* 
    - *These only need to be ran once unless you delete the 'database.db' file, which you might want to do for testing purposes - if you run these more than once, you'll get a "UNIQUE constraint failed" error as it tries to insert the primary keys when they already exist*
- `set FLASK_ENV=development` *activate development mode*
- `python -m flask run --host=0.0.0.0` *run the application*
- Visit "http://localhost:5000/" *to see the application*
- `deactivate` *close the virtual environment after you close the app*

## Run the app with all environment setup

- `.\env\Scripts\activate` *activate virtual env*
- `set FLASK_APP=app.py` *activate .py file to be the application*
- `set FLASK_ENV=development` *activate development mode*
- `python -m flask run --host=0.0.0.0` *run the application*
    - *On Linux, if the virtualenv cannot be found when trying to run the app, use* `venv/bin/python app.py`
    - *If you've activated the virtualenv, you shouldn't have to use the directory to the virtualenv in order to do everything. These commands are here incase you cannot get it activated.*
- Visit "http://localhost:5000/" *to see the application*
- `deactivate` *close the virtual environment after you close the app*

/* *(All the commands (`command`) above are executed via the command line)* */

## Caching fix - during design and development of web pages
Flask automatically caches your static files the first time they're loaded via Flask and because of this, you may have noticed that any changes your making aren't being applied when you refresh the page. For the changes to me made, you need to clear the cache and refresh the page, which you can do by pressing `ctrl+F5`.