
import requests
from bs4 import BeautifulSoup

print("loading........")

response = requests.get("https://www.amazon.in/s?k=dell+laptop+under+40000&crid=ESD1S34FPS2G&sprefix=dell+la%2Caps%2C434&ref=nb_sb_ss_ts-doa-p_2_7")

if response.status_code >= 200 and response.status_code < 300:

    html_string = response.text

    bs = BeautifulSoup(html_string,'html.parser')

    result = bs.find_all("span",{'class':'a-size-medium a-color-base a-text-normal'})

    for data in result:
        print(data.text)
else:
    print("Sorry something went Wrong !")

print("finished.")