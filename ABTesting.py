import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()

##chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--enable-javascript")


#d = DesiredCapabilities.CHROME
#d['goog:loggingPrefs'] = { 'browser':'ALL' }

caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['goog:loggingPrefs'] = { 'browser':'ALL' }

driver_path = '/opt/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path, desired_capabilities=caps)

print("********** Opening Browser***************")

driver.get("https://www.ikea.com/se/sv/")
time.sleep(5.0)
driver.execute_script("console.log(`Hello from Python`)")
driver.execute_script("console.log(`optimizely`)")
driver.execute_script("console.log(`window.ikea.cookieConsent.hasConsent(2)`)")

# print messages
#for entry in driver.get_log('browser'):
    #print("--------------")
    ##print(entry)

##pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

##cookies = pickle.load(open("cookies.pkl", "rb"))
##for cookie in cookies:
##    driver.add_cookie(cookie)

def cookies_status():
    Optimizely_cookie = 'NULL'
    status_key = 'NULL'
    status_value = 'NULL'
    for cookie in driver.get_cookies():
        if 'optimizelyOptOut' in  str(cookie):
            Optimizely_cookie=cookie
            print("Optimizely_cookie: ",Optimizely_cookie)
            print("--------status--------")
            for key, value in Optimizely_cookie.items():
                if 'value' in key:
                    status_key =value
                elif 'name' in key:
                        status_value = value
    print("status: ", status_value +"  "+ status_key)

print("********** Checking for  optimizelyOptOut cookies ***************")

cookies_status()

txt = driver.find_element_by_id('onetrust-accept-btn-handler').click()

print("*********** Accept the cookies  *****************")

print("*********** Refresh the Driver  *****************")




##driver.refresh()
#
time.sleep(5.0)

print("*********** Checking for  optimizelyOptOut cookies *****************")

for cookie in driver.get_cookies():
    if '_gid' in  str(cookie):
        print("**********",cookie)
    elif '_ga' in  str(cookie):
         print("**********",cookie)
         ##   print("status: ", status_value +"  "+ status_key)

##driver.quit()

print("********** Driver close ***************")


        