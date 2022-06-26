import requests, os, sys
from bs4 import BeautifulSoup, Tag

foundURL = []

def crawl(url):
    URL = f"{url}"
    page = requests.get("https:{}".format(URL))

    soup = BeautifulSoup(page.content, "html.parser")

    for file in soup.find_all('a'):
        fileGet = file.get('href')
        r = requests.get(f"https:{fileGet}")
        fileToSave = fileGet.replace('/','_')
        open(f"./{fileToSave}" , 'wb').write(r.content)
        testing = True
        for x in foundURL:
            if x == fileGet:
                testing = False
        if testing:
            foundURL.append(fileGet)
            crawl(fileGet)
                
if __name__ == "__main__":
    crawl("//vkguide.dev")