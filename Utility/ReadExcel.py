import openpyxl


def readExcel(file, coloumn_row):
    book = openpyxl.load_workbook(file)
    sheet = book.active
    data = sheet[coloumn_row]
    return  data.value