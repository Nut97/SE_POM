from time import sleep, time, localtime, strftime
import PIL
import pytesseract
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestCase(object):
    def login_test(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.6.28:8080/user/login')
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.NAME,'user').send_keys('user001')
        sleep(2)
        self.driver.find_element(By.NAME,'pwd').send_keys('123456')
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # str = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        # filename = str + '.png'
        # file_path = "../screenshots/" + filename  # 设置文件路径
        # if self.driver.save_screenshot(file_path):
        #     print("保存成功")
        # else:
        #     print("保存失败")
        #
        # left = ce.location['x']                                                 #截图后，获取验证码位置，再次截图
        # top = ce.location['y']
        # right = ce.size['width'] + left
        # height = ce.size['height'] + top
        #
        # im = Image.open(file_path)
        # img = im.crop((left, top, right, height))                               #抠图
        #
        # t = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        # pic_name = t+'.png'
        # img.save(pic_name)
        # sleep(2)
        # print(pic_name)
        # # str = pytesseract.image_to_string(pic_name)                              #无法使用
        # elem = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/button')
        # rect = elem.rect
        # print(rect)
        # pyautogui.moveTo(rect['x']+170,rect['y']+160)                                #通过pyauto方法使用鼠标操作去进行点击
        # pyautogui.click()
        sleep(2)




if __name__ == '__main__':
   case = TestCase()
   case.login_test()

