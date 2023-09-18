CREATING WHATSAPP BOT USING SELENIUM

import sys 
import time 
from selenium import webdriver

def user_chat(name_user):     
  chat_new = 
  browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')     
  chat_new.click()     
  
  user_chat = browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')     
  user_chat.send_keys(name_user)
  time.sleep(2) try:     
    
  user = browser.find_element_by_xpath('//span[@title="{}"]', 
  format(name_user)) user.click() 

except Exception as e:         
print(f"User {name_user} is not in the contacts") except Exception as e: browser.close() print(e) sys.exit() if __name__ == '__main__':     my_options = webdriver.ChromeOptions()     browser = webdriver.Chrome('chromedriver.exe', options=my_options)     browser.get('https://web.whatsapp.com')     time.sleep(20)     name_list = ['Shalini'] for name_user in name_list: try:     user =browser.find_element_by_xpath('//span[@title="{}"]'.format(name_user)) user.click() except Exception as e: print(e) Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited
        box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')         box_message.send_keys("Hi Shambhavi Here ... using the whatsapp bot")         time.sleep(10)         box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')         box_message.click()         time.sleep(20)     browser.close()
