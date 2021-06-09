from openpyxl import Workbook

def create_excel(records, headings, file_name):
    wb = Workbook()

    ws = wb.active

    ws.title = 'Excel Skills'

    ws.append(headings)

    for entry in records:
        ws.append(entry)

    wb.save(file_name)