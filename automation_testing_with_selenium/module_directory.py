import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_directory(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
  
    # test case : Mencari directory name dengan keyword spesifik
    def test_search_directory(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(2)
        driver.find_element(By.ID, "searchDirectory_emp_name_empName").send_keys("ananya dash")
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response = driver.find_element_by_css_selector("#resultTable > tbody > tr.odd > td:nth-child(2) > ul > li:nth-child(1) > b").text
        self.assertEqual(response, "Ananya Dash")
        self.driver.close()


    # test case : Mencari directory name dengan keyword tidak spesifik
    def test_search_directory_tidak_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(2)
        driver.find_element(By.ID, "searchDirectory_emp_name_empName").send_keys("becca")
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        self.driver.close()

    # test case : Mencari dengan select job title
    def test_search_jobtitle(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(2)
        driver.find_element(By.ID, "searchDirectory_job_title").send_keys("QA Engineer")
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()