# XLSX Terminal interface
<p>Create, add data to, and remove XLSX files. All from the comfort of your terminal. Created for fun, not practicality.</p>

# Required Modules:
* openpyxl (`pip install openpyxl`)

# Usage:
in your terminal, go to the app's folder. then run `python3 xlsx_terminal.py [option]`

# Creating new files:
To create a new file, run: `python3 xlsx_terminal.py new [filename.xlsx]`

# Adding data to files:
To add data to an existing file, run: `python3 xlsx_terminal.py add [filename.xlsx] [row number] [data1] [data2] ...` 

<b>Note:</b> If your data contains spaces, the data in one cell must be surrounded by double quotes.
for example: "First Name"

# Removing a row:
In order to remove a row, run: `python3 xlsx_terminal.py remove [filename.xlsx] [row number]` <br>
Note that this will remove ALL the data in the specified row. 
