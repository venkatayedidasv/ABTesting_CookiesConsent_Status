import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--enable-javascript")
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
##driver_path = '/opt/chromedriver' executable_path=driver_path
driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)

##print("********** Opening Browser***************")
driver.get("https://www.ikea.com/se/sv/")


time.sleep(5.0)
##driver.execute_script("console.log(`Hello from Python`)")
##print("********** Checking for  optimizelyOptOut cookies ***************")

driver.execute_script("return console.log(window.ikea.cookieConsent.hasConsent(2))")
driver.execute_script("return console.log(optimizely.initialized === true)")


status_key = ['optimizely']

def optimizely_status():
    for entry in driver.get_log('browser'):
        ##print(entry)
        for key, value in entry.items():
            line_value=str(value)
            if 'console-api ' in line_value:
                ##print(key,value)
                status=(value[-5:]).strip()
                status_key.append(status)

optimizely_status()
print("Cookies_Status: ", status_key[1] +" " +"Optimizely_Status: "+ status_key[2])

##print("*********** Checking for  optimizelyOptOut cookies *****************")


##print("*********** Accept the cookies  *****************")

txt = driver.find_element_by_id('onetrust-accept-btn-handler').click()

##print("*********** Refresh the Driver  *****************")

driver.refresh()
driver.execute_script("return console.log(window.ikea.cookieConsent.hasConsent(2))")
driver.execute_script("return console.log(optimizely.initialized === true)")
time.sleep(5.0)
optimizely_status()
print("Cookies_Status: ", status_key[3] +"  "+"Optimizely_Status: "+ status_key[4])


optout_default_se = False
if optout_default_se != (status_key[2]=='false'):
    print("Optimizely compliant")
    Optimizely_compliance = '1'
else:
    Optimizely_compliance = '0'

myHeaders = {
  'Content-type': 'application/json',
  'X-SF-Token': '5-28fhToYek6HehbOr2YCg'
}
dsrPayload={"gauge": [{'metric': "se.Optimizely_status", 'value': Optimizely_compliance}]}
dsPayload = json.dumps(dsrPayload)
print(dsPayload)

response = requests.post('https://ingest.eu0.signalfx.com/v2/datapoint', data=dsPayload, headers=myHeaders)
print(response)
print("Status code: ", response.status_code)


driver.quit()

##print("********** Driver close ***************")






        
