# coding=utf-8
import pymssql
class SQLServer:
     def __init__(self,server,user,password,database,charset):
     # 类的构造函数，初始化DBC连接信息
         self.server = server
         self.user = user
         self.password = password
         self.database = database
         self.charset= charset
     def GetConnect(self):
     # 得到数据库连接信息，返回conn.cursor()
         if not self.database:
             raise(NameError,"没有设置数据库信息")
         self.conn = pymssql.connect(server=self.server,
                                     user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     charset=self.charset)
         cur = self.conn.cursor()
         if not cur:
             raise(NameError,"连接数据库失败")  # 将DBC信息赋值给cur
         else:
             return cur
     #查询操作
     def ExecQuery(self,sql):
         '''
         执行查询语句
         返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
         cur = self.GetConnect()
         cur.execute(sql) # 执行查询语句
         result = cur.fetchall() # fetchall()获取查询结果
         # 查询完毕关闭数据库连接
         self.conn.close()
         return result
     #通过查询集合
     def ExecQuerylist(self,sql):
      cur=self.GetConnect()
      cur.execute(sql)
      resList = cur.fetchall()
      self.conn.close()
      return resList
     #待优化的数据库操作
     def insertEvent(self,sql):
       cur=self.GetConnect()
     def deleteEvent(self):
       cur=self.GetConnect()
     def updateEvent(self):
        cur=self.GetConnect()
def main():
     msg = SQLServer(server="192.168.18.130",user="sa",password="123456",database="login",charset="GBK")
     result = msg.ExecQuery("select * from userinfor")
     for Value in result:
         print(Value)
if __name__=="__main__":
  main()
