from selenium import webdriver

username = '' # fill in username
password = '' # fill in password

url = 'https://www.txu.com/login/' # electricity company

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Tyler Grayson\Downloads\chromedriver_win32\chromedriver.exe") # point to executable

driver.get(url)

# find elements in DOM and insert username and password
driver.find_element_by_id('ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_txtUsername').send_keys(username)
driver.find_element_by_id('ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_txtPassword').send_keys(password)
driver.find_element_by_id('ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_btnSubmit').click()
