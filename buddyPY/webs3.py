
import requests as req
from bs4 import BeautifulSoup

try:
    response = req.get("https://www.flipkart.com/search?q=i%20phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    if response.status_code >= 200 and response.status_code < 300:
        html_string = response.text
        bs = BeautifulSoup(html_string,'html.parser')

        result = bs.find_all("div",{'class':'_4rR01T'})

        for data in result:
            print(data.text)


    else:
        print("Sorry something went Wrong !")

except req.exceptions.ConnectionError:
    print("Sorry We are unable to connect to given URL")