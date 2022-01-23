#!/usr/bin/env python3
from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup

payload={}

# Round ID is required
round_id = 'REFUSEW1THU'

req = Request(f'https://www.hinckley-bosworth.gov.uk/alldates?round={round_id}')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')

fp = urlopen(req).read()
page = fp.decode("utf8")

soup = BeautifulSoup(page, features="html.parser")
soup.prettify()

data = {"bins":[]}

for bins in soup.findAll("div", {"class" : 'monthlycaldates'}):

    binCollection = bins.find_all('div', { "class" : "first_date_bins"})

    if binCollection:
      for bin in binCollection:
        
        collectionDate = bin.find("h3", {"class" : 'collectiondate'}).contents[0]
        collectionDate = collectionDate[:-1]
        
        binTypes = bin.find_all('img', {"class": "collection"})

        if binTypes:
            for type in binTypes:
                dict_data = {
                    "CollectionDate": collectionDate,
                    "BinType": type.get('title')
                }

                data["bins"].append(dict_data)

json_data = json.dumps(data)

print(json_data)
