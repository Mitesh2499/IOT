import requests

from bs4 import BeautifulSoup
url = "https://www.flipkart.com/redmi-note-7-sapphire-blue-64-gb/p/itmfdzvf8tptnezu?pid=MOBFDXZ3HJJZH3GG&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_16&otracker1=AS_QueryStore_OrganicAutoSuggest_0_16&lid=LSTMOBFDXZ3HJJZH3GGXELUJI&fm=SEARCH&iid=8fd93143-beaa-4b86-8be6-e6d6308dd875.MOBFDXZ3HJJZH3GG.SEARCH&ppt=sp&ppn=sp&ssid=0m44h5gvbk0000001562492378069&qH=2d3777a8293355a9"

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

page = requests.get(url, headers=header)

soup = BeautifulSoup(page.content, "html.parser")


def checkprice():
    title = soup.find("span", {"class": "_35KyD6"}).get_text()

    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text().replace(",", "")

    convertprice = int(price[1:])

    if convertprice < 12000:
        sendmail()

    print(title)
    print(int(convertprice))
