# -*- coding: utf-8 -*-
# ligin: gmasillogin123
# pass: gmasillogin123gmasillogin123
# export PATH=$PATH:/home/myroslav/gmail_login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep

class Gm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://accounts.google.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gm(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("gmasillogin123")
        driver.find_element_by_id("next").click()
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("gmasillogin123gmasillogin123")
        driver.find_element_by_id("signIn").click()
	sleep(5)
	driver.get('https://mail.google.com/mail/u/1/#inbox')
	sleep(15)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
