#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports:
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from csv import writer

#take user input:
destination = input("Enter your destination e.g Lahore,Karachi,etc:")
user_date = input("Enter your chaeck-in date in this form yyyy-mm-dd:")
check_out_user = input("Enter your chaeck-out date in this form yyyy-mm-dd:")
        
#code starts here
class drop_down_select():
    def drop_down_auto(self):
        #go to website
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.booking.com/index.html?aid=378266&label=bdot-Os1%2AaFx2GVFdW3rxGd0MYQS267778093357%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp1011084%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&sid=f4c8aaad619547284ad73c1ef32af6ab")
        
        #location input_automation
        depart_from = driver.find_element(By.XPATH,"//input[@id='ss']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys(destination)
        time.sleep(2)  
        
#check-in input_automation
        check_in = driver.find_element(By.XPATH,"//body/div[@id='indexsearch']/div[@class='hero-banner-searchbox']/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")
        check_in.click()
        time.sleep(2)
        all_dates= driver.find_elements(By.XPATH,"//table[@class='bui-calendar__dates']//tbody//td[@class!='bui-calendar__date bui-calendar__date--empty']")        
        for date in all_dates:
            if date.get_attribute("data-date") == user_date:
                date.click()
                time.sleep(4)
                check_in.click() 
        
        #check-out input_automation
        check_out =  driver.find_element(By.XPATH,"//div[contains(@data-mode,'checkout')]//span[contains(@class,'sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb')]")
        check_out.click()
        all_dates= driver.find_elements(By.XPATH,"//table[@class='bui-calendar__dates']//tbody//td[@class!='bui-calendar__date bui-calendar__date--empty']")        
        for date in all_dates:
            if date.get_attribute("data-date") == check_out_user:
                date.click()
                time.sleep(4)
        
#searches:
        search = driver.find_element(By.XPATH,"//button[@type='submit']")
        search.click()
        time.sleep(4)    
        with open('data.csv','a',newline='')as csvfile:
            thewriter=writer(csvfile)
            header=['name','url']
            thewriter.writerow(header)
        names = driver.find_elements(By.CLASS_NAME , 'a23c043802')
        link2= driver.find_elements(By.CLASS_NAME,'e13098a59f')
        name=[]
        urls=[]
        for i in names:
            name.append(i.text)
        #for i in name:
        #   name=(i.text)
        for i in link2:
            urls.append([(i.get_attribute('href'))])
            #print(urls)
        for i in range(len(name)):
            Data = [[name[i]],[urls[i]]]
            file = open('data.csv','a',newline ='')
            wr = csv.writer(file)
            wr.writerows(Data)
            file.close() 
                #print (names)
            
#            link2= driver.find_elements(By.CLASS_NAME,'e13098a59f')
#            for i in link2:
#                urls=[(i.get_attribute('href'))]
#                print(urls)
#                info=[urls]
#                thewriter.writerow(info)

            
deauto=drop_down_select()
deauto.drop_down_auto()










# In[ ]:




