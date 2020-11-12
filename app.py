from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options = Options()
import os
from time import sleep
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

driver = webdriver.Chrome(options=chrome_options)

driver.get("chfi.com")

artist = driver.find_element_by_class_name("data-now-playing-artist")
artist = artist.text
desiredArtist = input("Which artist would you like for me to tell you is playing on the radio? ")
if (artist == desiredArtist):
    print(desiredArtist + " is playing on CHFI")
    message = Mail(from_email=os.environ.get("TEST_SEND_EMAIL"),to_emails=os.environ.get("TEST_REC_EMAIL"), html_content="<strong>Taylor Swift is on the CHFI radio</strong>")
    # Sends email and checks for errors(boilerplate taken from Sengrid)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
else:
    print(desiredArtist + " is not playing on the radio")
sleep(300)