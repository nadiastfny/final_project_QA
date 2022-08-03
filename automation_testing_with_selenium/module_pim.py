import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_PIM(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
    
    # test case : Cek fungsi search employee
    def test_success_search(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
        time.sleep(2)
        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys("admin") 
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[1]/td[3]/a").text
        self.assertEqual(response, 'Admin')
        self.driver.close()

    # test case : Cek fungsi tambah data employee
    def test_success_add_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
        time.sleep(2)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"firstName").send_keys("Nadia") 
        time.sleep(2)
        driver.find_element(By.ID,"middleName").send_keys("") 
        time.sleep(2)
        driver.find_element(By.ID,"lastName").send_keys("Stef") 
        time.sleep(2)
        driver.find_element(By.ID,"employeeId").send_keys("") 
        time.sleep(2)
        driver.find_element(By.ID,"chkLogin").click()
        time.sleep(2)
        driver.find_element(By.ID,"user_name").send_keys("nadstef") 
        time.sleep(2)
        driver.find_element(By.ID,"user_password").send_keys("123456789") 
        time.sleep(2)
        driver.find_element(By.ID,"re_password").send_keys("123456789") 
        time.sleep(2)
        driver.find_element(By.ID,"status").send_keys("Enabled") 
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__": 
    unittest.main()