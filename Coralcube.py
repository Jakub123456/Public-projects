
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] += r"C:/Applications/Users/jakubskopec/Documents/git/chromedriver_mac64"
driver = webdriver.Chrome()


driver.get("https://coralcube.io/explore")

time.sleep(5)

driver.maximize_window()
wait = WebDriverWait(driver, 30)
list_links = []
link = ""



j = 1
while True:
    #try:
    ele2 = wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class = 'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-24 MuiGrid-grid-sm-12 MuiGrid-grid-md-8 MuiGrid-grid-lg-6 MuiGrid-grid-xl-4 styles_item__W2Zof css-1evtoz3'])[{j}]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", ele2)
    time.sleep(3)
    #except:
    #    print(j)
    #    print("Error has accured")
    #    break
    
    for element in driver.find_elements(By.XPATH, '//a[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-24 MuiGrid-grid-sm-12 MuiGrid-grid-md-8 MuiGrid-grid-lg-6 MuiGrid-grid-xl-4 styles_item__W2Zof css-1evtoz3"]'):
        link = element.get_attribute('href')
        
        # checking if string contains list element
        res = any(ele in link for ele in list_links)
        #print(res)
        if res == False:
            list_links.append(link)
            #print("List appended")        
            
    print(len(list_links))    
    #print(list_links)
    
    
    #name = ele.find_element(By.XPATH, "//div[@class = 'profile-listings-card-v2__name']/a").get_attribute('href')
    #print(name)
    
    j = j + 6

    #below code is just in case you want to break from infinite loop
    if j > 300:
        break
    

    
#print(list_links)
#for i in list_links:
#    print(i)
#print(len(list_links))



with open('CoralTest.txt', 'w') as f:
    for line in list_links:
        f.write(f"{line}\n")

   
print("---- D O N E ----")
