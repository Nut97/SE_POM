from selenium.webdriver.chrome import webdriver, service
from selenium import webdriver
from testcases import logging
from testcases.logging import TestCase


def go():
    wd = TestCase()
    wd.login_test1()
    logout = input('请输入任意键退出：')

if __name__ == '__main__':
    go()



