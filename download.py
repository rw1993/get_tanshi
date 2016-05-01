# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import pickle
import requests
from bs4 import BeautifulSoup as bs
import re


def get_url(url):
    url = "http://so.gushiwen.org" + url
    return url


def download(url):
    print url
    html = requests.get(url).content
    soup = bs(html)
    main3 = soup.find_all("div", class_="main3")[0]
    son2 = main3.find_all("div", class_="son2")[0]
    son1 = main3.find_all("div", class_="son1")[0]
    d = {}
    d['title'] = son1.text.strip()
    d['content'] = u"".join(son2.text.split()[5:])
    pattern = re.compile(ur"\(.*\)", re.UNICODE)
    d['content'] = re.sub(pattern, "", d['content'])
    print d['title']
    print d['content']
    return d


def get_urls():
    with open("tanshi_url", "r") as f:
        urls = [url[:-1] for url in f.readlines()]
    return urls


if __name__ == "__main__":
    urls = get_urls()
    result = [download(get_url(url)) for url in urls]
    with open("result_tan","wb") as f:
        pickle.dump(result, f)
        

