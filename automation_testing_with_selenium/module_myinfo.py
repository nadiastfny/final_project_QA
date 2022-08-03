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
  
    # test case : Ubah data pada form
    def test_edit_data(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/ul/li[1]/a").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)
        driver.find_element(By.ID,"personal_optGender_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"personal_txtEmpNickName").send_keys(" Nama Panggilanku")
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2) 
        self.driver.close()


    # test case : Tambah data work experience
    def test_add_data(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/ul/li[10]/a").click()
        time.sleep(2)
        driver.find_element(By.ID,"addWorkExperience").click()
        time.sleep(2)
        driver.find_element(By.ID,"experience_employer").send_keys("PT. Perkasa Jaya")
        time.sleep(2)
        driver.find_element(By.ID,"experience_jobtitle").send_keys("AS")
        time.sleep(2)
        driver.find_element(By.ID,"experience_from_date").click()
        time.sleep(2)
        driver.find_element(By.ID,"experience_from_date").send_keys("2020-09-07")
        time.sleep(2)
        driver.find_element(By.ID,"experience_comments").send_keys("Terlibat dalam 2 proyek")
        time.sleep(2)
        driver.find_element(By.ID,"btnWorkExpSave").click()
        time.sleep(2) 
        self.driver.close()


    # test case : Tambah data work experience dengan mengosongkan field required
    def test_add_data_kosongkan_required(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/ul/li[10]/a").click()
        time.sleep(2)
        driver.find_element(By.ID,"addWorkExperience").click()
        time.sleep(2)
        driver.find_element(By.ID,"experience_jobtitle").send_keys("HR")
        time.sleep(2)
        driver.find_element(By.ID,"experience_from_date").click()
        time.sleep(2)
        driver.find_element(By.ID,"experience_from_date").send_keys("2021-09-07")
        time.sleep(2)
        driver.find_element(By.ID,"experience_comments").send_keys("Terlibat dalam 2 proyek")
        time.sleep(2)
        driver.find_element(By.ID,"btnWorkExpSave").click()
        time.sleep(2) 
        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual(response, "Required")
        self.driver.close()


if __name__ == "__main__": 
    unittest.main()