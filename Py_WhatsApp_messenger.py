from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

def get_input_contact():

    contact_name=input('Enter name of contact (as stored in contact list): \n')       #asks for contact name to which message is to be sent.
    contact_name= "\"" + contact_name + "\""                                        #processing name to "name" for further convenience
    return contact_name
    
def get_input_msg():
    message=input('Enter the message to be sent(single line message only): \n')       #takes only messages without \n character.
    return message

def contact_selector(contact_name):                                             #this will select the contact to whom msg needs to be sent.
    
    contact_xpath='//span[@class="_1wjpf _3NFp9 _3FXB1"][@dir="auto"][@title={}]'.format(contact_name)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, contact_xpath)))

    except:                                                                     #except is needed in case of the errror that "Element can't be Scrolled into view"
        contact_search_box_path='//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="3"]'
        wait.until(EC.presence_of_element_located((By.XPATH, contact_search_box_path)))
        input_search_box=driver.find_element_by_xpath(contact_search_box_path)
        time.sleep(2)
        input_search_box.clear()
        input_search_box.send_keys(contact_name[1:(len(contact_name)-1)])       #searching for contact
        print('Contact Searched')                                               #can comment out this line if needed
        time.sleep(2)

    driver.find_element_by_xpath(contact_xpath).click()
    print('Contact Selected')                                                   #can comment out this line if needed


def msg_sender(message):                                                        #[IMPORTANT] this requires that contact is previously selected

    msg_box_xpath='//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="1"][@contenteditable="true"]'
    msg_box=wait.until(EC.presence_of_element_located((By.XPATH, msg_box_xpath)))

    time.sleep(2)

    msg_box.send_keys(message + Keys.ENTER) 
    time.sleep(1)
    msg_box.send_keys(Keys.ENTER)


#use the browser as per your choice

driver=webdriver.Firefox()
# driver=webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 15)                                                 #change wait time according to internet connection speed. Unit: sec

#QR code scanning

input('Scan QR code and press Enter')

continue_opt='y'
msg_opt='n'
contact_opt='n'

while(continue_opt=='y'):

    if contact_opt=='n':
        contact_name=get_input_contact()

    if msg_opt=='n':
        message=get_input_msg()

    contact_selector(contact_name)
    msg_sender(message)

    print('Message sent successfully to {} \n'.format(contact_name[1:(len(contact_name)-1)]))

    continue_opt=input('Do you want to send more messages? (y/n): \n').strip()
    
    if continue_opt=='y':
        contact_opt=input('Do you want to send to the same person? (y/n): \n').strip()
        msg_opt=input('Do you want to repeat the same message? (y/n): \n').strip()

    else:
        break

print('All messages sent successfully')
driver.close()
