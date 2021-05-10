from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException





# Parameters
Mob_no = ""
# NameOFRegisteredCandidate = ""


stateName = "Maharashtra"
districtName = "Pune"
centers = ['New Jijamata Hospital-2(18-44)','Premlok Park Disp- 2(18-44)',' New Bhosari (18-44)']

# Code

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver_path = './chromedriver_linux64 _89/chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://selfregistration.cowin.gov.in/")

enterMobNo = driver.find_element_by_xpath('//input[@formcontrolname="mobile_number"]')
enterMobNo.clear()
enterMobNo.send_keys(Mob_no)
time.sleep(2)
enterMobNo.submit()

getOTP_btn = driver.find_element_by_xpath("//ion-button[@type='button']")
getOTP_btn.click()

print("Enter The OTP recieved in 25 seconds")
time.sleep(20)


verifyAndProceed_btn = driver.find_element_by_xpath("//ion-button[@type='button']")
verifyAndProceed_btn.click()
print("OTP Entered and button Clicked")
time.sleep(4)


scheduleApt_loc = "//h3[contains(text(),'{}')]/ancestor::ion-grid[@class='cardblockcls md hydrated']//span[contains(text(),'Schedule')]".format(NameOFRegisteredCandidate)
print(scheduleApt_loc)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, scheduleApt_loc))))


sch_now_loc = "//ion-button[contains(text(),'Schedule Now')]"
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sch_now_loc))))

# Toggle Btn
searchByDistrict = driver.find_element_by_xpath("//div[@data-checked='Search By District']")
searchByDistrict.click()


#State

drp_state = "//div[@class='mat-select-arrow-wrapper ng-tns-c84-4']"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, drp_state))).click()


state_loc = "//span[contains(text(),'{}')]".format(stateName)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, state_loc))).click()

# District

time.sleep(2)
drp_dist="//div[@class='mat-select-arrow-wrapper ng-tns-c84-6']"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, drp_dist))).click()


dist_loc = "//span[contains(text(),'{}')]".format(districtName)
print(dist_loc)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, dist_loc))).click()

print("Click on Search")
search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
search_button.click()

driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()

print("Click on Search")
search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
search_button.click()

T=1
while T==1:
    for i in centers:
        slot_var = "//h5[contains(text(),'{}')]/ancestor::div[@class='mat-list-text']//a".format(i)
        print(slot_var)
        try:
            event = driver.find_elements_by_xpath(slot_var)
            print("len(event)",len(event))
            values =[]
            for items in event:
                values.append(items.text)
            num_val =[]
            for j in values:
                if j.isdigit():
                    num_val.append(j)
                    if len(num_val)>0:
                        for j in num_val:
                            available_slot = slot_var+"[contains(text(),'{}')]".format(j)
                            print(available_slot)
                            driver.find_element_by_xpath(available_slot).click()
                    else: print("Nahi Mila")
                else:
                    print("Click on Search Again 1")
                    time.sleep(2)
                    search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
                    search_button.click()
                    driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
                    time.sleep(2)

            else:
                print("No Slots Available for center {}".format(i))
                print("Click on Searchhhhh")
                time.sleep(2)
                search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
                search_button.click()
                time.sleep(1)
                driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
                time.sleep(1)
        except:
            print("Specified Center : {} not available".format(i))
            print("Click on Search 2")
            search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
            search_button.click()
            driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
            time.sleep(2)

#         print(values)
        print('---------------------------------------')
