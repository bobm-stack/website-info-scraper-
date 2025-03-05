import requesrs 
from bs4 import BeautifulSoup
from urllib import * 
import json

already_seen = set ()

def urls(url, keyword):
  try:
    res = requests.get(url)
  except:
    pass
if response.status_code == 200 :
  soup = BeautifulSoup(res.content,"html.parser")
  atag = soup.find_all("a")
  url_found = []
  for tag in atag:
    href = tag.get("href")
    if href is not None and href != "":
      url_found.append(href)
  print(url_found)
    


url = input(" enter the url u want to search for: ")
keyword = ("teh keyword u want to find: ")

urls(url,keyword)
