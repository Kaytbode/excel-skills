import sys
from excel.create_sheet import create_excel
from ppt.create_ppt import slide
from db.fetch_all import fetch_data

# excel files should be saved in the excel directory
excel_path = sys.path[0] + '/excel/'
# powerpoint files should be saved in the ppt directory
ppt_path = sys.path[0] + '/ppt/'

# A comparison join query
# get users that are less than 45 years old and live in lagos, in addition to their department

query = """SELECT u.*, d.department
           FROM users u
           JOIN departments d
           ON u.id = d.student
           WHERE u.location = 'Lagos' AND u.age < 45"""

headings = ['Id', 'Name', 'Location', 'Age', 'department']

excel_file = excel_path + 'join.xlsx'

ppt_file = ppt_path + 'join.pptx'

# Pull data from Postgres database
records = fetch_data(query)

# creates an excel file in the excel folder
create_excel(records, headings, excel_file)

# creates a powerpoint file in the ppt folder
slide(records, headings, ppt_file)