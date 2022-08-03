import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_Time(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
 
    # test case : Melihat  data project pada project reports
    def test_project_report(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_time_Reports").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_time_displayProjectReportCriteria").click()
        time.sleep(2)
        driver.find_element(By.ID,"time_project_name").send_keys("Internal - Training and Development") 
        time.sleep(2)
        driver.find_element(By.ID,"project_date_range_from_date").click()
        time.sleep(2)
        driver.find_element(By.ID,"project_date_range_from_date").send_keys("2022-01-01")
        time.sleep(2)
        driver.find_element(By.ID,"project_date_range_to_date").click()
        time.sleep(2)
        driver.find_element(By.ID,"project_date_range_to_date").send_keys("2022-06-09")
        time.sleep(2)
        driver.find_element(By.ID,"viewbutton").click()
        time.sleep(3)        
        self.driver.close()

    # test case : tambah data, Input data customer pada form
    def test_add_customer(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewCustomers").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addCustomer_customerName").send_keys("maruf") 
        time.sleep(2)
        driver.find_element(By.ID,"addCustomer_description").send_keys("testing automation")
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)       
        self.driver.close()


    # negative test case : Mengosongkan field required
    def test_add_customer_negative(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewCustomers").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addCustomer_customerName").send_keys(" ") 
        time.sleep(2)
        driver.find_element(By.ID,"addCustomer_description").send_keys("testing automation")
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)   

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual(response, 'Required')    
        self.driver.close()

    # test case : Menghapus data customer
    def test_delete_customer(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewCustomers").click()
        time.sleep(2)
        driver.find_element(By.ID,"ohrmList_chkSelectRecord_8").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(2)
        driver.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)   
        self.driver.close()

    # test case : Input data project pada form
    def test_add_project(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addProject_customerName").send_keys("Global Corp and Co")
        time.sleep(2)
        driver.find_element(By.ID,"addProject_projectName").send_keys("Dinaini")
        time.sleep(2)  
        driver.find_element(By.ID,"addProject_projectAdmin_1").send_keys("Admin A")
        time.sleep(2)
        driver.find_element(By.ID,"addProject_description").send_keys(" ")
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2) 
        self.driver.close()

    # test case : Mencari customer name dengan keyword tidak spesifik
    def test_search_tidak_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_customer").send_keys("fresh")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        # response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        # self.assertEqual(response, 'No Records Found')
        self.assertIsNotNone('Data dengan kata fresh ada pada records')
        self.driver.close()

    # test case : Mencari customer name dengan keyword spesifik
    def test_search_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_customer").send_keys("Fresh Books Software Ltd")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]").text
        self.assertEqual(response, 'Fresh Books Software Ltd')
        self.driver.close()

    # test case : Mencari project name dengan keyword spesifik
    def test_search_projectname_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_project").send_keys("Global Software phase - 1")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[3]/a").text
        self.assertEqual(response, 'Global Software phase - 1')
        self.driver.close()



    # test case : Mencari project name dengan keyword tidak spesifik
    def test_search_projectname_tidak_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_project").send_keys("global")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response, 'No Records Found')
        self.driver.close()



    # test case : Mencari project admin dengan keyword spesifik
    def test_search_projectadmin_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_projectAdmin").send_keys("adalwin")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertIsNotNone(response, msg='Data adalwin ada pada records table')
        self.driver.close()



    # test case : Mencari project admin dengan keyword tidak spesifik
    def test_search_projectadmin_tidak_spesifik(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_projectAdmin").send_keys("adalwin")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2) 

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertIsNotNone(response, msg='Data adalwin ada pada records table')
        self.driver.close()


    #  test case : Melakukan reset field kolom pencarian
    def test_reset_field(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_project").send_keys("global")
        time.sleep(2)
        driver.find_element(By.ID,"searchProject_projectAdmin").send_keys("adalwin")
        time.sleep(2)
        driver.find_element(By.ID,"btnReset").click()
        time.sleep(2) 
        self.driver.close()


if __name__ == "__main__": 
    unittest.main()
