import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()

##chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--enable-javascript")


d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }


driver_path = '/opt/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path, desired_capabilities=d)


print("********** Opening Browser***************")
driver.get("https://www.ikea.com/se/sv/")

time.sleep(5.0)
##driver.execute_script("console.log(`Hello from Python`)")
driver.execute_script("return console.log(window.ikea.cookieConsent.hasConsent(2))")
driver.execute_script("return console.log(optimizely[0].isOptOut)")


print("********** Checking for  optimizelyOptOut cookies ***************")

##txt = driver.find_element_by_id('onetrust-accept-btn-handler').click()

print("*********** Accept the cookies  *****************")

print("*********** Refresh the Driver  *****************")



time.sleep(5.0)
# print messages
status_key = ['optimizely']
for entry in driver.get_log('browser'):
    print("--------------")
    ##print(entry)
    for key, value in entry.items():
        line_value=str(value)
        if 'console-api ' in line_value:
            print(key,value)
            status=(value[-5:]).strip()
            status_key.append(status)

    
print("*********** Checking for  optimizelyOptOut cookies *****************")

txt = driver.find_element_by_id('onetrust-accept-btn-handler').click()
driver.refresh()

driver.execute_script("return console.log(window.ikea.cookieConsent.hasConsent(2))")
##driver.execute_script("return console.log(optimizely[0].isOptOut)")

time.sleep(5.0)
# print messages

for entry in driver.get_log('browser'):
    print("--------------")
    ##print(entry)
    for key, value in entry.items():
        line_value=str(value)
        if 'console-api ' in line_value:
            print(key,value)
            status=(value[-5:]).strip()
            status_key.append(status)



##print("Optimizely: ", status_key +"hasConsent(2)"+ status_key)

for status_key in status_key:
    print(status_key)

##driver.quit()

print("********** Driver close ***************")


        
