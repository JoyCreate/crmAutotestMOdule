#coding:utf-8
import unittest
import time
from  newcrmtest.uitil.loginMethod import login
from  newcrmtest.tools.Log import loginmanger
from newcrmtest.tools.readExcel import *
class logintestcase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #   logintestcase.login=login()
    # @classmethod
    # def tearDownClass(cls):
    #   print("测试结束")
    def setUp(self):
      logman=loginmanger()
      logman.consel_out()
      print("测试开始")
    def testevent(self):
      rd=excelHandle()
      filenam = r'D:\\python27File\\newcrmtest\\dateresouce\\logincase.xlsx'
      sheetnam = 'Sheet1'
      listdate = rd.read_excel(filenam,sheetnam)
      if (len(listdate)<=0):
          assert 0,u"excel数据异常"
      #要从1开始除去标题名
      for i in range(1,len(listdate)):
       test=login()
       test.loginevent(username=listdate[i][0],password=listdate[i][1])
       time.sleep(3)
    # def testevent_01(self):
    #   logman=loginmanger()
    #   logman.consel_out()
    #   test=login()
    #   test.loginevent(username="ra",password="1")
    #   time.sleep(3)
    #   test.closeBrowes()
    def tearDown(self):
       test=login()
       test.closeBrowes()
       print("测试结束")
if __name__=="__main__":
    unittest.main()


