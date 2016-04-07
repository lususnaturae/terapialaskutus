Install development environment
===============================
Installing development environment on Windows and using PyCharm

Prequisities
------------
Python 3.5.1
PostgreSQL server local installation
Virtualenv (https://virtualenv.readthedocs.org/en/latest/)
PyCharm

Clone project from github
-------------------------
git clone https://github.com/ylitormatech/therapyinvoicing
cd therapyinvoicing


Create virtualenv on Pycharm
----------------------------
Settings/Project Interpreter/Create virtualenv
Name e.g. therapy-dev
Note! Remember to select Python 3.5.1 as Base Interpreter


Create PyCharm configurations to run app and tests
--------------------------------------------------
Run configuration
^^^^^^^^^^^^^^^^^
Create configuration Django Server on PyCharm
Run Server http://127.0.0.1:8000
Environment variables:
DJANGO_SETTINGS_MODULE=config.settings.local
DATABASE_URL=postgres://localhost/therapyinvoicing?user=yourusername&password=yourpassword

Test configuration
^^^^^^^^^^^^^^^^^^
Create configuration Django Tests on PyCharm
Target: therapyinvoicing
Environment variables:
DJANGO_SETTINGS_MODULE=config.settings.local
DATABASE_URL=postgres://localhost/therapyinvoicing?user=yourusername&password=yourpassword

Set terminal inside PyCharm automatically activate virtualenv
-------------------------------------------------------------
Note! This is global setting and not project specific
Terminal inside Pycharm does not start selected virtualenv as default, but you can configure it
Settings/Tools/Terminal
Set Shell Path "cmd.exe /K pathtoyourenv\Scripts\activate.bat"
e.g. "cmd.exe /K D:\envs\therapy-dev\Scripts\activate.bat"
Restart PyCharm

Load requirements
-----------------
pip install -r requirements\local.txt

PostgreSQL Requirement for Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Installing PostgreSQL driver psycopg2 must be downloaded and installed manually on Windows
from http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg e.g. psycopg2-2.6.1-cp35-none-win_amd64.whl
pip install psycopg2-2.6.1-cp35-none-win_amd64.whl

PostgreSQL Requirement for non-Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pip install psycopg2

Create db to PostgreSQL
-----------------------
createdb therapyinvoicing

Make migration
--------------
python manage.py migrate
python manage.py createsuperuser

Load testdata
-------------
python manage.py loaddata testdata2015_customers.json
python manage.py loaddata testdata2015_customerinvoicing.json
python manage.py loaddata testdata2015_kelainvoicing.json

Run application
---------------
python manage.py runserver 8000

