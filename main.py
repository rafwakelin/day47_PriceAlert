import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import config


PRODUCT_URL = "https://www.amazon.ae/Taste-Wild-Lowland-Feline-Recipe/dp/B07SFRP4DQ/ref=sr_1_7?keywords=taste+of+the+wild+cat&qid=1673724102&sprefix=taste+o%2Caps%2C217&sr=8-7"
product_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
}

response = requests.get(url=PRODUCT_URL, headers=product_headers)
soup = BeautifulSoup(response.text, "lxml")
raw_price = soup.find(name="span", class_="a-price-whole")
price = float(raw_price.text)

if price <= 250:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=config.EMAIL, password=config.PASSWORD)
        connection.sendmail(from_addr=config.EMAIL,
                            to_addrs="raf.wakelin@yahoo.co.nz",
                            msg=f"Subject: Amazon Price Alert\n\n"
                                f"Taste of the Wild is at {price} on Amazon\n\n"
                                f"Hurry, here is the link {PRODUCT_URL}")
