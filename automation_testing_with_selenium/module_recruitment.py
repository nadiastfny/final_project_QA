import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_Recruitment(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
 
    # CANDIDATES
    # test case : Mencari daftar kandidat dengan filter
    def test_search_candidate(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "candidateSearch_jobTitle").send_keys("QA Lead")
        time.sleep(2)
        driver.find_element(By.ID,"btnSrch").click()
        time.sleep(2)
        self.driver.close()
        
    # test case : Mencari daftar kandidat dengan range tanggal
    def test_search_with_rangedate(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "candidateSearch_fromDate").click()
        time.sleep(2)
        driver.find_element(By.ID, "candidateSearch_fromDate").send_keys("2020-10-01")
        time.sleep(2)
        driver.find_element(By.ID, "candidateSearch_toDate").click()
        time.sleep(2)
        driver.find_element(By.ID, "candidateSearch_toDate").send_keys("2020-10-07")
        time.sleep(2)
        driver.find_element(By.ID,"btnSrch").click()
        time.sleep(2)
        self.driver.close()
    
    # test case : Menghapus data record pada table
    def test_delete_data_table(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "ohrmList_chkSelectRecord_23_5").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(2)
        driver.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)
        self.driver.close()
    

    # test case : Menambahkan data baru candidate 
    def test_add_data_candidate(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_firstName").send_keys("Putri")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_lastName").send_keys("narwati")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_email").send_keys("putri@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_vacancy").send_keys("Payroll Administrator")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_comment").send_keys("Testing untuk automation")
        time.sleep(2)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        self.driver.close()
    

    # test case : Menambahkan data baru candidate dengan tidak mengisi salah satu field required
    def test_add_data_candidate_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_firstName").send_keys("Ayu")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_email").send_keys("putri@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_vacancy").send_keys("Payroll Administrator")
        time.sleep(2)
        driver.find_element(By.ID, "addCandidate_comment").send_keys("Testing failed")
        time.sleep(2)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        
        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol[1]/li[1]/ol/li[3]/span").text
        self.assertEqual(response, "Required")
        self.driver.close()
    

    # SUB MODULE VACANCIES
    # test case : Mencari daftar vacancies dengan filter
    def test_search_vacancies(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_recruitment_viewJobVacancy").click()
        time.sleep(2)
        driver.find_element(By.ID,"vacancySearch_jobTitle").send_keys("QA Lead")
        time.sleep(2)
        driver.find_element(By.ID,"vacancySearch_jobVacancy").send_keys("Senior QA Lead")
        time.sleep(2)
        driver.find_element(By.ID,"btnSrch").click()
        time.sleep(2)

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertIsNotNone(response, msg="Data ditemukan")
        self.driver.close()


    # test case : Menambahkan data baru vacancies 
    def test_add_data_vacancies(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_recruitment_viewJobVacancy").click()
        time.sleep(2)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_jobTitle").send_keys("Automation Tester")
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_name").send_keys("QA Engineer")
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_hiringManager").send_keys("Anthony Nolan")
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_noOfPositions").send_keys("50")
        time.sleep(2)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        self.driver.close()
    
    # test case : Menambahkan data baru vacancies dengan tidak mengisi form required
    def test_add_data_vacancies_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_recruitment_viewJobVacancy").click()
        time.sleep(2)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_jobTitle").send_keys("Automation Tester")
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_hiringManager").send_keys("Anthony Nolan")
        time.sleep(2)
        driver.find_element(By.ID, "addJobVacancy_noOfPositions").send_keys("50")
        time.sleep(2)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(response, "Required")
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()