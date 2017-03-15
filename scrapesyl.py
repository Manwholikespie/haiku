import requests
from bs4 import BeautifulSoup

def nsylscrape(word):
    url = "http://www.dictionary.com/browse/"+word+"?s=t"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    syllable_tag = soup.select("span.syllable")
    print syllable_tag

nsylscrape("defences")
