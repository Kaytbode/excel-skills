from db_config import conn
from openpyxl import Workbook

# Pull data from database to excel

def fetch_data(query, title, file_name):
    try:
        cur = conn.cursor()

        cur.execute(query)

        records = cur.fetchall()


        wb = Workbook()

        ws = wb.active

        ws.title = 'Excel Skills'

        ws.append(title)

        for entry in records:
            ws.append(entry)

        wb.save(file_name)

    except:
        print('No connection to database')



