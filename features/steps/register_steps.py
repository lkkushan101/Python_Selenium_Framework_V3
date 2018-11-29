from Pages.HomePage import Home
from Pages.RegistrationPage import Register
from Pages.ConfirmationPage import Confirmation
from Utility.ReadExcel import readExcel
import unittest
import json
from selenium import webdriver
from behave import given, when, then, step

driver = webdriver.Chrome()
@given('that user is in New Tours Register Page')
def step_impl(context):


    driver.get(readExcel('./Data/data.xlsx', 'A2'))
    driver.set_page_load_timeout(20)
    m = Home(driver)
    m.getRegister().click()

@when('user types enter new data')
def step_impl(context):
    r = Register(driver)
    r.setFirstName(readExcel('./Data/data.xlsx', 'B2'))
    r.setLastName(readExcel('./Data/data.xlsx', 'C2'))
    r.setPhone(readExcel('./Data/data.xlsx', 'G2'))
    r.setCountry(readExcel('./Data/data.xlsx', 'D2'))
    r.setEmail(readExcel('./Data/data.xlsx', 'H2'))
    r.setUserName(readExcel('./Data/data.xlsx', 'E2'))
    r.setPassword(readExcel('./Data/data.xlsx', 'I2'))
    r.setConfirmPassword(readExcel('./Data/data.xlsx', 'I2'))
    r.submit
    r.submit

@then ('system should accept new user creation')
def step_impl(context):
    print('test')