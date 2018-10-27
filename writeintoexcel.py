import xlwt

writeCsvSheet = xlwt.Workbook()
sheet = writeCsvSheet.add_sheet('inital')
sheet.write(0, 0, 'abcd')
writeCsvSheet.save('C:\\Users\Yogesh\Desktop\ExcelInputFile.xls')