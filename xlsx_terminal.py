import sys
from openpyxl import Workbook, load_workbook

if len(sys.argv) > 1:
    if sys.argv[1] == "new":
        wb = Workbook()
        ws = wb.active
        wb.save(sys.argv[2])
    if sys.argv[1] == "add":
        wb = load_workbook(sys.argv[2])
        ws = wb.active
        active_row = int(sys.argv[3])
        for i in range(4, len(sys.argv)):
            ws.cell(active_row, i-3, str(sys.argv[i]))
        wb.save(sys.argv[2])
    if sys.argv[1] == "remove":
        wb = load_workbook(sys.argv[2])
        ws = wb.active
        active_row = int(sys.argv[3])
        ws.delete_rows(active_row)
        wb.save(sys.argv[2])