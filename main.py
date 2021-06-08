from fetch_all import fetch_data

basic_query = "SELECT * FROM users"
title = ['Id', 'Name', 'Location', 'Age']
file_name = 'users.xlsx'


fetch_data(basic_query, title, file_name)

# a simple join query
# Get all users and their departments

simple_join = """SELECT u.*, d.department
                 FROM users u
                 JOIN departments d
                 ON u.id = d.student"""

simple_join_title = ['Id', 'Name', 'Location', 'Age', 'department']

file_name2 = 'simplejoin.xlsx'

fetch_data(simple_join, simple_join_title, file_name2)

# a filtered join query
# get users that are in the sociology department

filtered_join = """SELECT u.*, d.department
                   FROM users u
                   JOIN departments d
                   ON u.id = d.student
                   WHERE d.department = 'Sociology'"""

filter_join_title = ['Id', 'Name', 'Location', 'Age', 'department']

file_name3 = 'filteredjoin.xlsx'

fetch_data(filtered_join, filter_join_title, file_name3)

# A comparison join query
# get users that are less than 45 years old and live in lagos, in addition to their department

comparison_join = """SELECT u.*, d.department
                     FROM users u
                     JOIN departments d
                     ON u.id = d.student
                     WHERE u.location = 'Lagos' AND u.age < 45"""

comparison_join_title = ['Id', 'Name', 'Location', 'Age', 'department']

file_name4 = 'comparisonjoin.xlsx'

fetch_data(comparison_join, comparison_join_title, file_name4)