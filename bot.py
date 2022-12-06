import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver/stable/chromedriver',chrome_options=chrome_options)
driver.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')

# width = driver.execute_script("return document.documentElement.scrollWidth")
# height = driver.execute_script("return document.documentElement.scrollHeight")
# driver.set_window_size(width, height)

# date
today = date.today()
mdy = today.strftime("%m/%d/%Y")
print(mdy)
# get field that need to fill
q0 = driver.find_element_by_xpath('//*[@id="97301341_751278109_label"]/span[1]')
q1 = driver.find_element_by_xpath('//*[@id="97301339"]')
q2 = driver.find_element_by_xpath('//*[@id="97301346_751278156_label"]/span[1]')
q3 = driver.find_element_by_xpath('//*[@id="97301347_751278143_label"]/span[1]')
q4 = driver.find_element_by_xpath('//*[@id="97301348_751278146_DMY"]')
q5 = driver.find_element_by_xpath('//*[@id="97301340_751278108_label"]/span[1]')
submit = driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')
# fill
q0.click()
q1.send_keys('') # Employee Id
q2.click()
q3.click()
q4.send_keys(mdy)
q5.click()
submit.click()

time.sleep(3)
driver.close()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
logfile = open("logfile.txt", "a")
logfile.write(mdy + " " + current_time + " : fill a temperture form\n")
logfile.close()