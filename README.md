# Whats Inside
A project to practice (hopefully) a lot of technologies such as Django, DRF, Angular, SASS, and PostgreSQL.

## Running on WSL

At root of project, run source env3/bin/activate, enabling the virtual environment. If you're not me for some reason, you'll need to run `pip install -r requirements.txt.`

Control the postgres database using `sudo /etc/init.d/postgresql [restart/start/stop]`


Locally boot up the site using `python manage.py runserver.`


**Note: systemctl is not working on WSL as of yet, making use of gunicorn sockets kinda tough.** See [here](https://github.com/Microsoft/WSL/issues/2209).


## Running on Windows pre-Creator's update
At root of project, run workon env3, enabling the virtual environment (virutalenv). If you're not me for some reason, you'll need to run pip install -r requirements.txt.

Locally boot up the site using python manage.py runserver.

Deploying to Heroku is a bit more annoying because it doesn't like to accept your login info.

heroku login
heroku auth:token
git push heroku master use the auth token as the password, leave the name blank.
Want to check how often the site has been booted up (ie, a dyno has been created)? Use heroku ps