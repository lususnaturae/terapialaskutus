Deploy
========================================
Deploying production environment into Heroku

Prequisities
------------
Python 3.5.1
PostgreSQL server
PyCharm

Clone project from github
-------------------------
git clone https://github.com/ylitormatech/therapyinvoicing
cd therapyinvoicing


Create virtualenv on Pycharm
----------------------------
Settings/Project Interpreter/Create virtualenv
Name e.g. therapy-prod
Note! Remember to select Python 3.5.1 as Base Interpreter


PostgreSQL Requirement for Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Installing PostgreSQL driver psycopg2 must be downloaded and installed manually on Windows
from http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg e.g. psycopg2-2.6.1-cp35-none-win_amd64.whl
pip install psycopg2-2.6.1-cp35-none-win_amd64.whl


PostgreSQL Requirement for non-Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pip install psycopg2

Load other requirements
-----------------------
pip install -r requirements\production.txt

Load bower requirements
-----------------------
python manage.py bower install

Create Heroku dyno from Python buildpack
----------------------------------------
heroku create titest --buildpack heroku/python

Set vars at Heroku
------------------
Note! First modify setenvs_prod_heroku.py to your own settings
python setenvs_prod_heroku.py
Add database
------------
heroku addons:create heroku-postgresql:hobby-dev

Set DATABASE_URL to point to database
-------------------------------------
heroku pg:promote DATABASE_URL

Deploy project to Heroku
------------------------
git push heroku master

Run migration
-------------
heroku run python manage.py migrate

Create superuser
----------------
heroku run python manage.py createsuperuser

Open app
--------
heroku open
