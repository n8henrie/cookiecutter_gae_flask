# cookiecutter_gae_flask

A Flask / Google App Engine template for [cookiecutter](https://github.com/audreyr/cookiecutter).

## Use it now

    $ pip install cookiecutter
    $ cookiecutter https://github.com/n8henrie/cookiecutter_gae_flask.git

You will be asked about your basic info (name, project name, app name, etc.).
This info will be used in your new project.

**NB:** GAE will choke if your app name (as defined in `app.yaml`) has certain
special characters. I recommend you stick with numbers, letters, and `-`.

Once you've made your new package,
I encourage you to make a new venv with a GAE-appropriate Python in the
directory, then test the basic setup:

    $ cd new_flask_app
    $ virtualenv -p $(command -v python2.7) venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt -t lib
    $ dev_appserver.py .

# Features
--------

# Screenshots
-----------

# License
-------

MIT

Changelog
---------

