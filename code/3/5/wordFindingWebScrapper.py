import requests, os, sys
from bs4 import BeautifulSoup, Tag

def crawl(url,word):
    URL = f"{url}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup.find_all(string=word):
        for file in soup.find_all(string=word):
            print("found {}".format(file))
    else:
        print("the {} is not there".format(word))

if __name__ == "__main__":
    crawl(input("link: "),input("word: "))