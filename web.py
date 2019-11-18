from bs4 import BeautifulSoup
import requests
import credentials
from lxml import html
from selenium import webdriver
def getToken():
    page = requests.get("https://www.ebay-kleinanzeigen.de/m-einloggen.html?targetUrl=/")
    soup = BeautifulSoup(page.content, 'html.parser')
    input = soup.findAll(type="hidden", attrs={"name": "_csrf"})
    # input is a list probably containing only one element
    csrf_value = input[0]['value']
    return csrf_value
def login():

    login_url="https://www.ebay-kleinanzeigen.de/m-einloggen.html?targetUrl=/"

    session_requests = requests.session()
    page = requests.get(login_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    input = soup.findAll(type="hidden", attrs={"name": "_csrf"})
    # input is a list probably containing only one element
    csrf_value = input[0]['value']

    print(csrf_value)
    #TODO: create a pythonfile e.g. credentials.py with your credentials to login:
    # loginMail="max.mustermann@gmail.com"
    # password="password123'
    payload={
    "loginMail":credentials.loginMail,
    "password":credentials.password,
    "_csrf":csrf_value
    }
    print(payload)
    result = session_requests.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url)
    )
    #TODO login to ebay-kleinanzeigen.de not working so far
    print(result)
    print("logged in?")
    print()
    url = 'https://www.ebay-kleinanzeigen.de'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    input = soup.findAll(attrs={"id": "user-mail"})
    print(input)

def main():
    login()



if __name__=="__main__":
    main()