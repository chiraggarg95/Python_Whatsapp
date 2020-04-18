from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 


#use the browser as per your choice

driver=webdriver.Firefox()

# driver=webdriver.Chrome()


driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 120)         #change wait time according to internet connection speed. Unit: sec

#QR code scanning

input('Scan QR code and press Enter')

#data input

contact_name=input('Enter name of contact (as stored in contact list): ')       #asks for contact name to which message is to be sent.

contact_name= "\"" + contact_name + "\""    #processing name to "name" for further convenience

message=input('Enter the message to be sent(single line message only): ')       #takes only messages without \n character.

repetitions=input('Enter number of times you want to send the message: ')
repetitions=int(repetitions)    #converting to integer

contact_xpath='//span[@class="_1wjpf _3NFp9 _3FXB1"][@dir="auto"][@title={}]'.format(contact_name)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, contact_xpath)))

except:                     #except is needed in case of the errror that "Element can't be Scrolled into view"
    contact_search_box_path='//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="3"]'
    wait.until(EC.presence_of_element_located((By.XPATH, contact_search_box_path)))
    input_search_box=driver.find_element_by_xpath(contact_search_box_path)
    time.sleep(5)
    input_search_box.clear()
    input_search_box.send_keys(contact_name[1:(len(contact_name)-1)])     #searching for contact
    print('Contact Searched')       #can comment out this line if needed
    time.sleep(5)


driver.find_element_by_xpath(contact_xpath).click()
print('Contact Selected')           #can comment out this line if needed

time.sleep(2)

msg_box_xpath='//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="1"][@contenteditable="true"]'
msg_box=wait.until(EC.presence_of_element_located((By.XPATH, msg_box_xpath)))

time.sleep(2)

while(repetitions>0):
    msg_box.send_keys(message + Keys.ENTER) 
    time.sleep(2)
    msg_box.send_keys(Keys.ENTER)
    print('Message successfully sent to {}'.format(contact_name[1:(len(contact_name)-1)]))
    time.sleep(1)
    repetitions-=1
