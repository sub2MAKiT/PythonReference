import requests, os, sys
from bs4 import BeautifulSoup, Tag

foundURL = []

def crawl(url):
    URL = f"{url}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    for file in soup.find_all('a'):
        fileGet = file.get('href')
        r = requests.get(f"{fileGet}")
        open(f"./{fileGet}" , 'wb').write(r.content)
        testing = True
        for x in foundURL:
            if x == fileGet:
                testing = False
        if testing:
            foundURL.append(fileGet)
            crawl(fileGet)
        


        # if isinstance(file.contents[0], Tag):
        #     f = file.contents[0].get("data-sort")
            
    #         if f != None:
    #             print(f)

    #             if f.startswith("*"):
    #                 dr = f"{url}/{f[1:]}"

    #                 if not os.path.exists(dr): os.makedirs(dr)
    #                 crawl(dr)
    #             else:
    #                 try:
    #                     r = requests.get(f"{URL}/{f}")
    #                     open(f"{url}/{f}" , 'wb').write(r.content)
    #                 except(OSError): 
    #                     print(f"error: {url}/{f}")
    #                     pass
                
if __name__ == "__main__":
    # folder = sys.argv[1]

    # if folder != "":
    # print(f"crawling: {folder}")
    crawl("https://makit.wtf")
    # else:
    #     print("missing arguments")