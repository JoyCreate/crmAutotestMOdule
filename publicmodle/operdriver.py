from  selenium import  webdriver
def __init__(self,driver):
        self.driver = driver
#定义一个打开浏览的方法并使默认浏览器打开最大化
def browes():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver
    # def __init__(self,driver):
    #     self.driver=driver
    # browes_type="ie"
    # def get_openBrowes(self,driver):
    #        if self.browes_type =="Firefox":
    #         driver=webdriver.Firefox()
    #        elif self.browes_type == 'Chrome':
    #         driver = webdriver.Chrome()
    #        elif self.browes_type == 'IE':
    #         driver = webdriver.Ie()
    #        else: driver = webdriver.Chrome()
    #        driver.maximize_window()
    #        driver.implicitly_wait(10)
    #        return driver
    #

