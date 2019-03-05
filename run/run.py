import unittest
import  time
from newcrmtest.publicmodle import operdriver
from  newcrmtest.test.test_CrmLogin import logintestcase
from  newcrmtest.test.test_CrmAddcustomer import testAddcustomer
from  newcrmtest.filepath.filepath import fileposition
from  newcrmtest.tools.sendEmai import sendEmai
if __name__=="__main__":
    driver=operdriver.browes()
    driver.get("http://crm2.icvip.com/")
    from  HTMLTestRunner import HTMLTestRunner
    testsuit=unittest.TestSuite()
    testsuit.addTest(logintestcase("test_CrmLogin"))
    #testsuit.addTest(logintestcase("testevent_01"))
    testsuit.addTest(testAddcustomer("test_addcustomer"))
    test_report_dir = 'D:\\python27File\\newcrmtest\\result'
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = test_report_dir+'\\'+ now_time + 'result.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
    runner.run(testsuit)
    fp.close()
    newresult= fileposition.new_file(test_report_dir)
    emial=sendEmai()
    emial.Sendemail(newresult)