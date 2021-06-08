import sys
from create_ppt import slide

path = sys.path[0] + '/ppt/'

basic_query = "SELECT * FROM users"
headings = ['Id', 'Name', 'Location', 'Age']
file_name = path + 'users.pptx'

slide(basic_query, headings, file_name)

# a simple join query
# Get all users and their departments

simple_join = """SELECT u.*, d.department
                 FROM users u
                 JOIN departments d
                 ON u.id = d.student"""

simple_join_headings = ['Id', 'Name', 'Location', 'Age', 'department']

file_name2 = path + 'simplejoin.pptx'

slide(simple_join, simple_join_headings, file_name2)

# a filtered join query
# get users that are in the sociology department

filtered_join = """SELECT u.*, d.department
                   FROM users u
                   JOIN departments d
                   ON u.id = d.student
                   WHERE d.department = 'Sociology'"""

filter_join_headings = ['Id', 'Name', 'Location', 'Age', 'department']

file_name3 = path + 'filteredjoin.pptx'

slide(filtered_join, filter_join_headings, file_name3)

# A comparison join query
# get users that are less than 45 years old and live in lagos, in addition to their department

comparison_join = """SELECT u.*, d.department
                     FROM users u
                     JOIN departments d
                     ON u.id = d.student
                     WHERE u.location = 'Lagos' AND u.age < 45"""

comparison_join_headings = ['Id', 'Name', 'Location', 'Age', 'department']

file_name4 = path + 'comparisonjoin.pptx'

slide(comparison_join, comparison_join_headings, file_name4)