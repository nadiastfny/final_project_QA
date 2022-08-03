import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_Leave(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
 

    # test case : Pilih tanggal awal dan akhir untuk filter
    def test_search_myleave(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_leave_Entitlements").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_leave_viewMyLeaveEntitlements").click() 
        time.sleep(2)
        driver.find_element(By.ID,"entitlements_leave_type").send_keys("CAN - Bereavement") 
        time.sleep(2)
        driver.find_element(By.ID,"period").send_keys("2020-01-01 - 2020-12-31") 
        time.sleep(3)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()
