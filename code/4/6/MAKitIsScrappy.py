import requests, os, sys
from bs4 import BeautifulSoup, Tag

def crawl(url,Ite):
    if (url.find("https")== 0)&(url.find("http")== 0):
        URL = f"{url}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        if soup.find_all(string="MAKiT"):
            for file in soup.find_all(string="MAKiT"):
                print("{}.found {} in ".format(Ite,file,page.url))
        else:
            print("{}.the {} is not there".format(Ite,"MAKiT"))
        if Ite < 5:
            for file in soup.find_all("a"):
                fileGet = file.get('href')
                crawl(f"{fileGet}",Ite+1)

if __name__ == "__main__":
    crawl(input("link: "),1)