from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


driver = webdriver.Firefox\
    (executable_path='E:\MySofts\geckodriver-v0.23.0-win64\geckodriver.exe')
driver.get('http://toolsqa.com/automation-practice-form/')