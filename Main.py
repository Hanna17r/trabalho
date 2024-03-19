from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\Users\\LabInfo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.netshoes.com.br/auth/login")
    driver.implicitly_wait(2) 
    print ('0')
    email_login = driver.find_element(By.XPATH, '//*[@id="user"]')
    email_login.send_keys("hanna.luzzi@hotmail.com")
    print ('1')

    senha_login = driver.find_element(By.XPATH, '//*[@id="password"]')
    senha_login.send_keys("182436")
    print ('2')

    btn_login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/section[1]/form/div[6]/div/div/button')
    print ('3')
    btn_login.click()
    
    email_login = driver.find_element(By.XPATH, '//*[@id="user"]')
    email_login.send_keys("hanna.luzzi@hotmail.com")
   
 
    

    
    print("Teste Passou! Comentário postado.")
except:
    print("Teste Falhou! Não foi possível postar o comentário.")

driver.quit()