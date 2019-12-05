from selenium import webdriver

chrome_browser=webdriver.Chrome()

#print(chrome_browser)

chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title