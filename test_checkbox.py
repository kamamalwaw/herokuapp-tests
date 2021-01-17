# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCheckbox():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
    self.vars = {}
    self.driver.set_window_size(1050, 660)
    self.driver.get("http://the-internet.herokuapp.com/checkboxes")

  def teardown_method(self, method):
    self.driver.quit()
  
  def test_checkbox1(self):

    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    attr1 = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").is_enabled()
    assert attr1 is True

  def test_checkbox2(self):

    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    attr2 = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").is_selected()
    assert attr2 is True

  def test_checkbox3(self):

    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    attr3 = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").is_enabled()
    assert attr3 is True

  def test_checkbox4(self):
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    attr4 = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").is_selected()
    assert attr4 is not True
  