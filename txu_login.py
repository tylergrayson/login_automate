from selenium import webdriver

username = 'grayson311'
password = 'whati5love'

url = 'https://www.txu.com/login/'

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Tyler Grayson\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(url)

driver.find_element_by_id(
    'ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_txtUsername').send_keys(username)
driver.find_element_by_id(
    'ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_txtPassword').send_keys(password)
driver.find_element_by_id(
    'ContentPlaceHolderMain_ctl01_ctl00_txuLoginModule_btnSubmit').click()
