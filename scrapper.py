# impporting required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the user and header string

URL = 'https://www.amazon.in/boAt-Display-Multiple-Monitoring-Charcoal/dp/B09MQSCJQ1/ref=sr_1_3?keywords=boat+smart+watch&qid=1656610000&sprefix=boat+%2Caps%2C311&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# function to check if the price has dropped

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="title").get_text()
    price = soup.find('span', "a-price-whole").get_text().replace(',', '').replace('.', '').replace(' ', '').strip()
    actual_price = float(price[0:5])

    if(actual_price < 2500):
        send_mail()

    print(actual_price)
    print(title.strip())
    
# function that sends an email if the prices fell down

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'PASSWORD')
    subject = 'Price fell down!'
    body = 'Go buy from the link https://www.amazon.in/boAt-Display-Multiple-Monitoring-Charcoal/dp/B09MQSCJQ1/ref=sr_1_3?keywords=boat+smart+watch&qid=1656610000&sprefix=boat+%2Caps%2C311&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender@gmail.com',
        'receiver@gmail.com',
        msg
    )
# print a message to check if the email has been sent

    print('Hey EMAIL has been sent!')

    server.quit()

# loop that allows the program to regularly check for prices 

while(True):
    check_price()
    time.sleep(60 * 60 * 24)







