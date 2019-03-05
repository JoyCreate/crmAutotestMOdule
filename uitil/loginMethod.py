from  selenium import  webdriver
import  logging
import  time
from selenium.webdriver import ActionChains
from newcrmtest.publicmodle import operdriver
#定义一个类封装登录方法  期望:单个操作被封装直接调用
class login():
    driver=operdriver.browes()
    driver.get("http://crmdev.icvip.com/")
    def loginevent(self,username,password):
        self.driver.find_element_by_xpath('//*[@id="guidePage"]/header/div/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/div[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/div[2]/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/button').click()
        #添加一个断言并判断是否获取到预期的值
        try:
              link =self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div[1]/div[1]/a').text
              assert link=='首页'
              self.driver.get_screenshot_as_file("D:\\python27File\\newcrmtest\\screenFile\\loginSuccess.jpg")
              print("访问成功")
        except Exception as e:
              print('访问失败')
        else:
            print("没有错误发生")
        finally:
            print("测试结束")
        # try:
        #       loginerror=self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div/ul/li').text
        #       assert loginerror=='用户不存在'
        #       self.driver.get_screenshot_as_file("D:\\python27File\\newcrmtest\\screenFile\\fail.jpg")
        #       print("断言成功！！")
        # except Exception as e:
        #      logging.exception(e)
        #      print("断言失败！")
    def mycustomer(self):
        time.sleep(6)
        mavencstomer=self.driver.find_element_by_xpath('//*[@id="left-menu-list"]/div[2]/div[2]/div/span')
        ActionChains(self.driver).move_to_element(mavencstomer).perform()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath("//a[contains(text(),'我的客户')]").click()
        time.sleep(6)
    def  sercherCustomer(self,sercherValue):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/input').send_keys(sercherValue)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/i').click()
        time.sleep(5)
        assertaimtxt=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[4]/span').text
        try:
              assert assertaimtxt==sercherValue
              self.driver.get_screenshot_as_file("D:\\python27File\\newcrmtest\\screenFile\\seachSucces.jpg")
              print('搜索成功')
        except Exception as e:
           print('搜索失败')
    def clearSercherValue(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/input').clear()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/i').click()
        time.sleep(4)
    def coinselect(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div/i').click()
        time.sleep(3)
        oop= self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/ul')
        # oopvalue=oop.find_elements_by_tag_name('option')
        oop.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/ul/li[4]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div/i').click()
        oop1=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/ul')
        oop1.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/ul/li[1]').click()
        time.sleep(8)
        # oop.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/ul/li[1]').click()
    def customerState(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/i').click()
        time.sleep(3)
        state=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul')
        state.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul/li[3]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/i').click()
        state1=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul')
        state1.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul/li[1]').click()
        self.driver.implicitly_wait(6)
    def hightsercher(self):
         self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/span').click()
         self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[1]/div/div[1]/div/div[2]/div/input').clear()
         self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[1]/div/div[1]/div/div[2]/div/input').send_keys("CH001D8")
         self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/button[1]').click()
         self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/i')
    def addCustomer(self,Usernumbe,CompanyName,CompanyNameC,CompanyNameE,VendorCode,phoneNmber):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div/div').click()
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/input').send_keys(Usernumbe)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/input').send_keys(CompanyName)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/input').send_keys(CompanyNameC)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/input').send_keys(CompanyNameE)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[5]/div/div[2]/div/input').send_keys(VendorCode)
        # 应用领域
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[6]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[6]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[6]/div/div[2]/div/ul/li[5]').click()
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/label/input').send_keys('application')
        # 电话
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[7]/div/div[2]/div/input').send_keys(phoneNmber)
        # 资方背景
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[12]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[12]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[12]/div/div[2]/div/ul/li[3]').click()
        # 行业
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[13]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[13]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[13]/div/div[2]/div/ul/li[3]').click()
        # 产品
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[14]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[14]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[14]/div/div[2]/div/ul/li[4]').click()
        # 客户类型
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[15]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[15]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[15]/div/div[2]/div/ul/li[4]').click()
        # 账期
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[20]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[20]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[20]/div/div[2]/div/ul/li[9]').click()
        # 交易币种
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[21]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[21]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[21]/div/div[2]/div/ul/li[3]').click()
        # 交易方式
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[22]/div/div[2]/div/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[22]/div/div[2]/div/ul')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[22]/div/div[2]/div/ul/li[6]').click()
        # js = 'document.querySelectorAll("class")[21].style.display="block" '
        # self.driver.execute_script(js)
        # js1 = "document.getElementsByClassName('options')[21].style.display='block'" #编写JS语句
        # self.driver.execute_script(js1) #执行JS
        # js = "document.getElementsByClassName('options').style.display='block'" #编写JS语句
        # self.driver.execute_script(js) #执行JS
        # js = "window.scrollTo(0,260)"
        # self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/button[1]').click()
        time.sleep(3) 
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[11]/div/label/input').send_keys('')
        # self.driver.find_element_by_xpath('').send_keys()
        #
        # contactPosition=self.driver.find_element_by_xpath('//*[@id="PositionValue"]')
        # AllPositin=contactPosition.find_elements_by_tag_name('option')
        # for optionvalues  in oopvalue:
        #    print ("Value is: " + optionvalues.get_attribute("value"))
        #    print ("Text is:" + optionvalues.text)
        #    if "USD"  in optionvalues.text:
        #       optionvalues.click()
        #       break
        self.driver.implicitly_wait(3)
    def clickalonedate(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[2]/div/div[1]').click()
    def closeBrowes(self):
        self.driver.close()
if __name__=="__main__":
    logclass=login()
    # logclass.openBrowes()
    logclass.loginevent(username="micro",password="1")
    logclass.mycustomer(sercherValue='CH00G3Z')
    logclass.coinselect()
    time.sleep(3)
    logclass.customerState()
    time.sleep(3)
    logclass.addCustomer(Usernumbe='20181030',CompanyName='数据核对',CompanyNameC='数据',CompanyNameE='DataCheck',VendorCode='20181245',phoneNmber='1234545878')
    # logclass.closeBrowes()