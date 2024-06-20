from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/user/login')
        self.driver.maximize_window()

    def login(self):
        name = 'user001'
        pwd = '123456'
        expected = '用户中心'
        self.driver.find_element(By.NAME,'user').send_keys(name)
        self.driver.find_element(By.NAME,'pwd').send_keys(pwd)
        self.driver.find_element(By.CLASS_NAME,'btn').click()
        sleep(2)
        print(self.driver.title)
        #断言
        assert self.driver.title == expected




if __name__ == '__main__':
    case = TestCase()
    case.login()