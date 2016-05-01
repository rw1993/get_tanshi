# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import requests
from bs4 import BeautifulSoup as bs


def get_page_url(i):
    print i
    url = "http://so.gushiwen.org/type.aspx?p={}&c=唐代"
    url = url.format(str(i))
    return url

def download(url):
    html = requests.get(url).content
    soup = bs(html)
    a_s = soup.find_all("a", title="查看全文")
    with open("tanshi_url", "a+") as f:
        for a in a_s:
            f.write(a["href"])
            f.write("\n")





if __name__ == "__main__":
    for i in range(300):
        download(get_page_url(i+1))

