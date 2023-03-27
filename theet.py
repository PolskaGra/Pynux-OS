import xlsxwriter
import var
import sys
import os
import openpyxl

os.system('cls')

workbook = xlsxwriter.Workbook(var.Default_Dir + "\\" + var.xlsfilename)
ws = workbook.add_worksheet()
workbook.close()

# nie rozumiem tego XDDDDDDD

xfile = openpyxl.load_workbook(var.Default_Dir + "\\" + var.xlsfilename)
sheet = xfile.get_sheet_by_name(var.Default_Dir + "\\" + var.xlsfilename)

while True:
    sheetcmd = input()
    if sheetcmd == "exit":
        sys.exit(0)
        os.remove(var.Default_Dir + "\\" + var.xlsfilename)
        xfile.save(var.Default_Dir + "\\" + var.xlsfilename)
    if " l: " in sheetcmd:
        codac = sheetcmd.split(" l: ")
        sheet[codac[0]] = codac[1]
