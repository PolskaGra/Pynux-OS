import xlsxwriter
import var
import sys
import os

os.system('cls')

workbook = xlsxwriter.Workbook(var.Default_Dir + "\\" + var.xlsfilename)
ws = workbook.add_worksheet()

while True:
    sheetcmd = input()
    if sheetcmd == "exit":
        workbook.close()
        sys.exit(0)
    if " l: " in sheetcmd:
        codac = sheetcmd.split(" l: ")
        ws.write(codac[0], codac[1])
