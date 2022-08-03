import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_Admin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
      
    # test case : Memasukkan keyword dengan spesifik
    def test_success_search(self):
        driver = self.driver
        # self.test_success_login
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_UserManagement").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_viewSystemUsers").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("Garry.White") 
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_userType").send_keys("All") 
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys(" ") 
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_status").send_keys("All") 
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        self.driver.close()

    # test case : Memasukkan keyword tidak spesifik
    def test_failed_search(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_UserManagement").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_viewSystemUsers").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("garry") 
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_userType").send_keys("All") 
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys(" ") 
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_status").send_keys("All") 
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)
        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response, 'No Records Found')
        self.driver.close()

    # test case : Menambahkan user baru dengan password kategori better
    def test_success_add_user(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(1)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_userType").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys("David Morris") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_userName").send_keys("iuty12345") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_status").send_keys("Enabled") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_password").send_keys("Via12345@") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("Via12345@") 
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        self.driver.close()

    # test case : Menambahkan user baru dengan password kurang dari 8 karakter
    def test_failed_add_user(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(1)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_userType").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys("David Morris") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_userName").send_keys("budi") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_status").send_keys("Enabled") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_password").send_keys("123") 
        time.sleep(1)
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("123") 
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        self.driver.close()

    # test case : Menambahkan data skill
    def test_add_data_skill(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(1)  
        driver.find_element(By.ID, "menu_admin_Qualifications").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu_admin_viewSkills").click()
        time.sleep(1)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(1)      
        driver.find_element(By.ID,"skill_name").send_keys("Microsoft Word") 
        time.sleep(1)
        driver.find_element(By.ID,"skill_description").send_keys("Testing untuk automation") 
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()