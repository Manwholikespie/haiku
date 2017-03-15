import pprint
import wikipedia
from nltk import sent_tokenize
import hyphenation
import re, string

def scrapePage(topic):
    pageText = wikipedia.WikipediaPage(topic).content

    # regex magic courtesy of https://github.com/AndreiRegiani
    parenthesis_regex = re.compile('\(.+?\)')  # to remove parenthesis content
    citations_regex = re.compile('\[.+?\]')  # to remove citations, e.g. [1]
    header3_regex = re.compile('\===.+?\===')
    header2_regex = re.compile('\==.+?\==')
    pageText = pageText.strip()
    pageText = parenthesis_regex.sub('', pageText)
    pageText = citations_regex.sub('', pageText)
    pageText = header3_regex.sub('', pageText)
    pageText = header2_regex.sub('', pageText)

    # make some replacements to clean it up.
    pageText = pageText.replace(" ,",",")
    pageText = pageText.replace("  ,",",")
    pageText = pageText.replace("  "," ")
    pageText = pageText.replace("\n\n","")

    return pageText
