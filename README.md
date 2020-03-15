# XLSX Terminal interface
<p>Create, add data to, and remove XLSX files. All from the comfort of your terminal.</p>

# Usage:
in your terminal, go to the app's folder. then run `python3 xlsx_terminal.py [option]`

<h3>Creating new files:</h3>
To create a new file, run: <br>
`python3 xlsx_terminal.py new [filename.xlsx]`

<h3>Adding data to files:</h3>
To add data to an existing file, run: <br>
`python3 xlsx_terminal.py add [filename.xlsx] [row number] [data1] [data2]` <br><br>
For example: <br>
`python3 xlsx_terminal.py example.xlsx 1 Name Address Phone` <br> 
Would add "Name", "Address", "Phone" in order to the first cell in row 1 <br> <br>

<b>Note:</b> If your data contains spaces, the data in one cell must be surrounded by double quotes.
for example: "First Name"

<h3>Removing a row:</h3>
In order to remove a row, run: <br>
`python3 xlsx_terminal.py [filename.xlsx] [row number]` <br><br>
Note that this will remove ALL the data in the specified row.