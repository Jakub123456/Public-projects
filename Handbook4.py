import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


text_file = open("Test.txt", "r")
url_list = text_file.readlines()
#print(url_list)
text_file.close()


os.environ['PATH'] += r"C:/Applications/Users/jakubskopec/Documents/git/chromedriver_mac64"
driver = webdriver.Chrome()

driver.get("https://www.thehandbook.com/login/")

new_list = []
final_list = []

time.sleep(20)
for url in url_list:
    #print(url)
    driver.get(url)
    time.sleep(3)
    print("Final list:")
    print(final_list)
    new_list.clear()
    print("Final list:")
    print(final_list)
    name = driver.find_element(By.XPATH, '//span[@class="m-profile-header__title"]')
    #print(name.text)
    new_list.append(name.text)
    new_list.append(url)
    print("Final list:")
    print(final_list)
    for element in driver.find_elements(By.XPATH, '//ul[@class="profile-contact-card__contact-details"]'):
        ele = element.text
        #print(element.text)
        new_list.append(ele)
        print("New list: ")
        print(new_list)
    
    print("Final list:")
    print(final_list)
    print(new_list)
    final_list.append(new_list)
    print("Final list:")
    print(final_list)

with open('Test_Output.txt', 'w') as f:
    for line in final_list:
        f.write(f"{line}\n")   

    
