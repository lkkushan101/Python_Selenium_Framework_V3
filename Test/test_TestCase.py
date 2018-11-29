from Pages.HomePage import Home
from Pages.RegistrationPage import Register
from Utility.ReadExcel import readExcel
import unittest
import json
from selenium import webdriver
import pytest
import allure

class RegistrationTest(unittest.TestCase):
    @allure.story('Test Automation Solution - Kushan Amarasiri')
    @allure.feature('Test - Auomation Framework in Python')
    @allure.testcase("Registration Test Case")
    def setUp(self):

       # with pytest.allure.step("Launch site"):
         self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):

        with open('./Data/data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        str1 = readExcel('./Data/data.xlsx','A2')

        driver.get(str1)
        driver.set_page_load_timeout(20)
        m = Home(driver)
        m.getRegister().click()
        r = Register(driver)
        r.setFirstName(readExcel('./Data/data.xlsx','B2'))
        r.setLastName(readExcel('./Data/data.xlsx','C2'))
        r.setPhone(readExcel('./Data/data.xlsx','G2'))
        r.setCountry(readExcel('./Data/data.xlsx','D2'))
        r.setEmail(readExcel('./Data/data.xlsx','H2'))
        r.setUserName(readExcel('./Data/data.xlsx','E2'))
        r.setPassword(readExcel('./Data/data.xlsx','I2'))
        r.setConfirmPassword(readExcel('./Data/data.xlsx','I2'))
        r.submit
        if __name__ == "__main__":
            unittest.main()

