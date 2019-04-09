import time

from appium import webdriver
import unittest
import random



class MyPhone(unittest.TestCase):
    dr_configuration = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:21503',
        'platformVersion': '5.1.1',
        'appPackage': 'com.juddata.dragon',
        'appActivity': 'com.juddata.dragon.activity.LauncherActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'autoLaunch': True,
        'noReset': True

    }
    dr_phone = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dr_configuration)
    dr_phone.implicitly_wait(30)


    @classmethod
    def setUpClass(cls):
        print('开始启动')





    def test_1login(self):
        # print('TEST===============================登陆================================TEST')
        time.sleep(10)

        self.dr_phone.find_element_by_id('com.juddata.dragon:id/login_sms').click()

        self.dr_phone.find_element_by_id('com.juddata.dragon:id/phone_et').send_keys('17780508427')
        self.dr_phone.find_element_by_id('com.juddata.dragon:id/msg_btn').click()
        time.sleep(3)
        self.dr_phone.find_element_by_id('com.juddata.dragon:id/auth_et').send_keys('1111')
        time.sleep(3)
        self.dr_phone.find_element_by_id('com.juddata.dragon:id/login_btn').click()
        time.sleep(10)






    @classmethod
    def tearDownClass(cls):


        time.sleep(3)


if __name__ == '__main__':
    unittest.main()