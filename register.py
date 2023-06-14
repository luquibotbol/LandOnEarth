from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas

path = "chromedriver.exe"
driver = webdriver.Chrome()

# loop here
csv1 = "austinexp.csv"
df = pandas.read_csv(csv1)
# len(df.index)-3
for x in range(3):
    
    url = "https://landonearth.com/professional/signup"
    driver.get(url)

    time.sleep(1)
    ffname = df["FIRST NAME"][x]
    fname = driver.find_element("id", "pro-form_first_name")
    fname.send_keys(ffname)


    llname = df["LAST NAME"][x]
    lname = driver.find_element("id", "pro-form_last_name")
    lname.send_keys(llname)
    print(llname)

    # time.sleep(.5)

    pphone = df["PHONE"][x]
    phone = driver.find_element("id", "pro-form_phone_number")
    phone.send_keys(pphone)

    eemail = df["EMAIL"][x]
    email = driver.find_element("id", "pro-form_email")
    email.send_keys(eemail)

    ppassword = df["PASSWORD"][x]
    password = driver.find_element("id", "password-input")
    password.send_keys(ppassword)

    time.sleep(.5)
    element = driver.find_element(By.XPATH, "//button[@phx-click='next_step']")
    element.click()

    time.sleep(1)
    sstate = "Texas"
    state = driver.find_element("id", "pro-form_state")
    state.send_keys(sstate)
    

    llicense = df["LICENSE"][x]
    license1 = driver.find_element("id", "pro-form_state_license_number")
    license1.send_keys(str(llicense))
    print(llicense)
    

    # Select San Antonio with "SABOR"
    select = Select(driver.find_element("id", 'pro-form_mls'))
    select.select_by_value('SABOR')
    

    bbrokerName = df["BROKERAGE"][x]
    brokerName = driver.find_element("id", "pro-form_broker_name")
    brokerName.send_keys(bbrokerName)
    

    bbrokerRec = df["BROKER"][x]
    brokerRec = driver.find_element("id", "pro-form_broker_record")
    brokerRec.send_keys(bbrokerRec)
    
    time.sleep(1)


    
    element = driver.find_element(By.XPATH, "//button[@phx-click='next_step']")
    element.click()

    time.sleep(1)

    dismiss = driver.find_element(By.XPATH, "//button[@phx-click='go_to_home']")
    dismiss.click()

    time.sleep(1)

driver.quit()
