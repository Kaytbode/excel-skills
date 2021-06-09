# Excel-Skills

A python script that pulls data from an external postgres database to excel and powerpoint.

## Before Usage
- Fork and clone the repo `https://github.com/Kaytbode/excel-skills.git` on your local machine. You can also click on the *green code button*, to view options to download the **ZIP** file.

- I use [pyenv](https://github.com/pyenv/pyenv) to manage my python installations and [pipenv](https://pipenv.pypa.io/en/latest/) for my python virtual environment.

- You need to have python 3.6 or below installed on your machine.  
    > `python-pptx` package does not yet work with higher versions of python. Checkout the [docs](https://python-pptx.readthedocs.io/en/latest/user/install.html) for more information.

- I used [ElephantSQL](https://www.elephantsql.com/) to create the postgres database. You can use `postgres` database installed on your machine or from any other source. However, you will have to remove `lines 6 and 8` in the `db/db_config.py` file and substitute the values in the `pg.connect` parameters for your database values.

- If you decide to create your database from [ElephantSQL](https://www.elephantsql.com/),  
    1. Create a `.env` file.
    2. Copy the database *URL* from the *details tab*.
    3. Set the environment variable **DB_URL= the URL you copied**

- After creating your database,
    1. `CD` into the `db` directory.
    2. Run the command `python create_table.py` to create tables and insert values into the tables.

- Run `pipenv install` to install the packages.

## Usage
1. `CD` into your version of the repo directory on your machine.

2. Run `python main.py`

3. Look into the `excel` and `ppt` folders for the generated excel and powerpoint files.

## Packages Used
- [Psycopg2](https://pypi.org/project/psycopg2/) enables communication to PostgreSQL through python.

- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/), a python library to read/write excel.

- [python-pptx](https://python-pptx.readthedocs.io/en/latest/user/intro.html), a python library to create powerpoints.
