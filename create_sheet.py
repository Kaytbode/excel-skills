from openpyxl import Workbook
from db.fetch_all import fetch_data

def create_excel(query, headings, file_name):
    records = fetch_data(query)

    wb = Workbook()

    ws = wb.active

    ws.title = 'Excel Skills'

    ws.append(headings)

    for entry in records:
        ws.append(entry)

    wb.save(file_name)