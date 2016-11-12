# -- coding: utf-8 --

import os
import requests
from bs4 import BeautifulSoup

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

home_url = input("please input url of wordbook you want to download: ")
home_page = requests.get(home_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content
bsojt = BeautifulSoup(home_page, "html.parser")
wordbook = bsojt.find("div", class_="wordbook-title").a.string
units = bsojt.find_all("td", class_="wordbook-wordlist-name")

if not os.path.exists('wordbook'):
    os.makedirs('wordbook')

file_path = 'wordbook/' + str(wordbook) + '.txt'
if os.path.exists(file_path):
    os.remove(file_path)

fd = open(file_path, 'a')

for unit in units:
    unit_url = 'https://www.shanbay.com/' + unit.a['href']
    for i in range(1, 11):                            
        url = unit_url + "?page="+ str(i) 
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content            
        soup = BeautifulSoup(page, "html.parser")  
        print("reading page "+ str(i))
        for tag in soup.find_all("strong"):
            for word in tag:
                print(word.string)
                fd.write(word.string + "\n")

fd.close()
