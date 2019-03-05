import  unittest
import time
from newcrmtest.tools.Log import loginmanger
from newcrmtest.tools.readExcel import excelHandle
from newcrmtest.uitil.loginMethod import login

class testAddcustomer(unittest.TestCase):
    def setUp(self):
      logman=loginmanger()
      logman.consel_out()
      print("测试开始")
    def test_addcustomer(self):
      rd=excelHandle()
      filenam = r'D:\\python27File\\newcrmtest\\dateresouce\\AddCustomerCase.xlsx'
      sheetnam = 'Sheet1'
      listdate = rd.read_excel(filenam,sheetnam)
      if (len(listdate)<=0):
          assert 0,u"excel数据异常"
      #要从1开始除去标题名
      for i in range(1,len(listdate)):
       test=login()
       # test.loginevent(username=listdate[i][0],password=listdate[i][1])
       test.addCustomer(Usernumbe=listdate[i][0],CompanyName=listdate[i][1],
                        CompanyNameC=listdate[i][2],CompanyNameE=listdate[i][3],
                        VendorCode=listdate[i][4],phoneNmber=listdate[i][5])
       time.sleep(3)
    def tearDown(self):
       test=login()
       test.closeBrowes()
       print("测试结束")
if __name__=="__main":
    unittest.main()



