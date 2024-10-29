import logging
import selenium.webdriver
from selenium import webdriver
import selenium.webdriver.firefox.service
import tempfile
tempfile.tempdir = "/snap/firefox/current/usr/lib/firefox/firefox"

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)

firefox_bin = "/usr/bin/firefox"
firefoxdriver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.binary_location = firefox_bin

service = webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)

browser = webdriver.Firefox(options=options)
browser = webdriver.Firefox(service=service, options=options)
browser.get("https://www.facebook.com")
#import logging
#import selenium.webdriver
#import selenium.webdriver.firefox.service
#from selenium.webdriver.firefox.service import Service


#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#logger = logging.getLogger('selenium')

#firefox_bin = "home/krarktel/firefox-esr"
#firefoxdriver_bin = "/usr/bin/firefox/geckodriver"

#options = selenium.webdriver.firefox.options.Options()
#options.add_argument('--headless')
#options.browser_version = 'esr'
#options.binary_location = firefox_bin
#Firefox = "firefox-esr"

#service = selenium.webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)

#browser = selenium.webdriver.Firefox(options=options)

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#logger = logging.getLogger('selenium')
