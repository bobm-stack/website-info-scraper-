import requesrs 
from bs4 import BeautifulSoup
from urllib import * 
import json

already_seen = set ()

def urls(url, keyword):
  try:
    res = requests.get(url)
  except:
    print(f"the request failed at {url}")
    return
if response.status_code == 200 :
  soup = BeautifulSoup(res.content,"html.parser")
  atag = soup.find_all("a")
  url_found = []
  for tag in atag:
    href = tag.get("href")
    if href is not None and href != "":
      url_found.append(href)


for urls2 in url_found:  
  if urls2 not in already_seen():
    already_seen.add(url)
    url_join  = urljoin(url,urls2)
    if keyword in url_join:
      print(url_join)
      urls(url_join,keyword)
    else:
      pass
    

url = input(" enter the url u want to search for: ")
keyword = ("teh keyword u want to find: ")

urls(url,keyword)
