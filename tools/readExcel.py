import traceback
from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd
 # class readexcel():
 # def open_excel(self,file):
 #        try:
 #                data = xlrd.open_workbook(file)
 #                return data
 #        except Exception as e:
 #                print (str(e))
 #        #根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
 # def excel_table_byindex(self ,file= 'file.xls',colnameindex=0,by_index=0):
 #        Rd=readexcel()
 #        data =Rd.open_excel(file)
 #        table = data.sheets()[by_index]
 #        nrows = table.nrows #行数
 #        colnames = table.row_values(colnameindex) #某一行数据
 #        list =[]
 #        for rownum in range(1,nrows):
 #                row = table.row_values(rownum)
 #                if row:
 #                        app = {}
 #                        for i in range(len(colnames)):
 #                                app[colnames[i]] = row[i]
 #                                list.append(app)
 #        return list
class excelHandle:
    def decode(self, filenam, sheetnam):
        try:
            filename = filenam.encode(encoding='utf8')
            sheetname = sheetnam.encode(encoding='utf8')
        except Exception:
            print( traceback.print_exc())
        return filenam, sheetnam
    def read_excel(self, filename, sheetname):
        filenam, sheetnam = self.decode(filename,sheetname)
        rbook = xlrd.open_workbook(filenam)
        sheet = rbook.sheet_by_name(sheetnam)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            all_content.append(row_content)
            print( '[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')
        return all_content
if __name__ == '__main__':
    eh = excelHandle()
    filenam = r'D:\\python27File\\newcrmtest\\dateresouce\\logincase.xlsx'
    sheetnam = 'Sheet1'
    re= eh.read_excel(filenam,sheetnam)
    for i in range(1,len(re)):
        res=re[i][0]
        pd=re[i][1]
        print(res)
        print(pd)


