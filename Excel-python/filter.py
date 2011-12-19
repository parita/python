import xlrd
import xlwt

DOCS_PATH='/home/parita/Documents/'

wb=xlrd.open_workbook(DOCS_PATH+'Robocon.xls')
sh=wb.sheet_by_index(0)

wb_wt=xlwt.Workbook()
ws=wb_wt.add_sheet('Sheet1')
rownum=0
company_name=sh.cell_value(rownum,0)
i=0
while company_name:
	for colnum in range(0,sh.ncols):
		ws.write(i,colnum,sh.cell_value(rownum,colnum))
	i=i+1 		
	while(company_name==sh.cell_value(rownum,0)):
		rownum=rownum+1
	company_name=sh.cell_value(rownum,0)
wb_wt.save('Robocon(1).xls')
