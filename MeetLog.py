from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import os
import keyboard
import pandas as pd
import urllib.request




class meet_bot:
    def __init__(self):
        
        # To give permission to chrome pop-up
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 2, 
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.geolocation": 2, 
        "profile.default_content_setting_values.notifications": 2 
        })
        self.bot = webdriver.Chrome(chrome_options=opt,executable_path = "C:\Program Files (x86)\chromedriver.exe")
        
        
    
    def login(self, email, passw, link):
        

        
        bot = self.bot
        # This is for the google meet sign in page
        bot.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        
        
        try:
            # This is for the Email address block
            email_in = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
                    )
            email_in.send_keys(email)
            
            
            time.sleep(1)
            
            
            # To click the 'next' button
            next_btn = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"))
                    )
            next_btn.click()
            
            
            time.sleep(5)
            
            
            # Password block
            passwo = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))
                    )
            passwo.send_keys(passw)
            
            
            time.sleep(1)
            
            
            # To click the 'next' button
            next_btn = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]'))
                    )
            next_btn.click()
            
            
            time.sleep(1)
            
            
            # To input the google meet link
            link_var = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/label/input'))
                    )
            link_var.send_keys(link)
            
            
            time.sleep(1)
            
            
            # To click 'Join' button
            join = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]'))
                    )
            join.click()
            
            
            time.sleep(1)
            
            
            # To dismiss
            dismiss = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div[2]/div[3]/div/span/span'))
                    )
            dismiss.click()
            
            
            time.sleep(1)
            
            
            # To click 'Join Now' button
            join_Now = WebDriverWait(bot, 15).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span"))
                    )
            join_Now.click()
            
            
            # To click on the participants section
            parti = WebDriverWait(bot, 30).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span'))
                    )
            parti.click()
            
            
        except:
            pass
            

        

            
            
            
            
        
        # This section makes a 5 second interval with adjusted sleep based on runtime of the loop    
        
#         master_d = {}
#         timestamp = 0
#         while(timestamp <= 2400):
#             start = time.time()
#             namelist = bot.find_elements_by_class_name("ZjFb7c")            
#             for name in namelist:
#                 try:
#                     n = name.get_attribute('innerHTML')   
#                 except Exception as e:
#                     pass
                    
#                 if n in master_d:
#                     master_d[n] += 5
#                 else:
#                     master_d[n] = 0
#             end = time.time()
# #             print(end, start, end-start)
                
#             time.sleep(5 - (end-start))
            
#             timestamp += 5
            
# #             print(master_d)
        
        
        
        
        
        
        # This section makes a 5 second interval with adjusted sleep based on runtime of the loop 
        # Solved unique name issue.....more or less the same runtime....
#         nset = set()
#         master_d = {}
#         timestamp = 0
#         while(timestamp <= 2400):
#             start = time.time()
#             namelist = bot.find_elements_by_class_name("ZjFb7c")            
            
            
#             for name in namelist:
#                 try:
#                     n = name.get_attribute('innerHTML')
#                     nset.add(n)
#                 except Exception as e:
#                     pass
#             for i in nset:        
#                 if i in master_d:
#                     master_d[i] += 5
#                 else:
#                     master_d[i] = 0
#             nset.clear()
#             end = time.time()
            
#             print(end, start, end-start)
#             print(master_d)
#             print('\n\n')
#             time.sleep(5 - (end-start))
#             timestamp += 5
        
        
        
        # This section makes a 5 second interval with adjusted sleep based on runtime of the loop 
        # Solved unique name issue.....more or less the same runtime....
        # Modified code to run as long as the page exists...
        nset = set()
        master_d = {}
        while(urllib.request.urlopen("https://meet.google.com/emv-hhvp-war").getcode()==200):
            start = time.time()
            try:
                namelist = bot.find_elements_by_class_name("ZjFb7c")  
            except Exception as e:
                break
            
            
            for name in namelist:
                try:
                    n = name.get_attribute('innerHTML')
                    nset.add(n)
                except Exception as e:
                    pass
                
            for i in nset:        
                if i in master_d:
                    master_d[i] += 5
                else:
                    master_d[i] = 0
            nset.clear()
            end = time.time()
            
            print(end, start, end-start)
            print(master_d)
            print('\n\n')
            time.sleep(5 - (end-start))
            
        
        
        
        
        
        
        
        
        # This section creates a dataframe
        
        df = {"Name":[],
             "IN_Seconds":[]}
                        

        for key, val in master_d.items():
            df["Name"].append(key)
            df["IN_Seconds"].append(val)
    
    
        
        print("\n\n\n\n\n")
        df = pd.DataFrame(data = df)
        df["IN_Minutes"] = round(df["IN_Seconds"]/60, 2)
        
        print(df.sort_values(by=['IN_Minutes'], ascending = False))







        
obj = meet_bot()
obj.login("Enter email ID","Password", 'Enter the gmeet link')




