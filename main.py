import re
import string

from nltk.corpus import cmudict
from nltk import tokenize, word_tokenize, sent_tokenize, pos_tag
from nltk.corpus import stopwords

from bs4 import BeautifulSoup
import requests
import wikipedia

from wikiscrape import *
from thesaurus import *
from hyphenation import *

# f = open("haikus.txt","w") # as we find haikus, we are going to write them
                           # to this file.

d = cmudict.dict()

def nsyl(word):
    """Return the number of syllables in a given word.
    """
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

def nsylScrape(word):
    """In the case that a word isn't in cmudict for us to find the amount of
    syllables, this can scrape the number of syllables from howmanysyllables.com

    Returns an integer amounting to the number of syllables in the word.
    """
    # set up beautifulsoup
    url = "https://www.howmanysyllables.com/words/"+word.lower()
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")

    # generates a random CSS id name for the proper syllable number,
    # hiding fake ones with hidden styles. The real one has display:inline;
    style_tag = soup.select("style")
    if len(style_tag) > 1:
        style = [item.text for item in soup.select("style")][len(style_tag)-1]
    else:
        style = [item.text for item in soup.select("style")][0]
    span_id = style.rsplit("{display:inline;}",1)[0]

    # Use the randomized id we found to search for the relevant <span>.
    return [int(item.text) for item in soup.select("span"+span_id)][0]

def tokenPara(bodyString):
    """Use nltk to tokenize a paragraph, returning a sentence-- that is, if it
    contains only ASCII characters.

    :param bodyString: the paragraph we wish to tokenize.
    :output: a list of sentences that are all ASCII in nature.
    """
    sentences = sent_tokenize(bodyString)
    for item in sentences:
        try:
            str(item)
        except:
            print(item+u"didn't work.")
            sentences.remove(item)
            break
        if len(item) < 27:
            sentences.remove(item)
    return sentences

def printSent(tSent):
    """Return a non-tokenized sentence with spaces and everything.

    :param tSent: the tokenized sentence you wish to print
    :output: a string, that is the original* sentence.
        * - somewhat original. It's not perfect yet.
    """
    sent = u""
    for word in tSent:
        sent += word + " "
    return sent

def tokenSent(sentenceString):
    """Perform a word tokenization on a sentence, raeturning everything but
    punctuation.

    :param sentenceString: the sentence you wish to tokenize.
    :output: a list containing the elements of a tokenized sentence, save for
        its punctuation.
    """
    words = word_tokenize(sentenceString)
    punctuation = ['.',',']

    words = filter(lambda x: x not in punctuation, words)

    return words

def getSyl(tSent):
    """Counts the number of syllables each word in a tokenized sentence. Returns
    a list of tuples, wherein item[0] is the word from the original sentence,
    and item[1] is the number of syllables the word it has.

    :param tSent: the tokenized sentence to examine the syllable count for.
    :output: a list of tuples, containing syllable data for individual words.
    """
    wordData = []
    for word in tSent:
        try:
            wordData.append(nsylCMU(word))
        except:
            print("cmudict is missing: "+word)
            try:
                wordData.append((word,nsylScrape(word)))
            except:
                print("hms is missing: "+word)
                try:
                    wordData.append((word,len(hyphenate_word(word))))
                except:
                    print("Error for: "+word)
                    wordData.append((word,0))

    return wordData

def getWordSyl(word):
    """Counts the number of sylables in a word.

    :param word: the word you wish to count the syllables of
    :output: an integer that signifies the number of syllables a word has.
    """
    if (word == ",") or (word == "."):
        return 0

    if ' ' in word:
        syl = 0
        word = word.split(' ')
        for item in word:
            try:
                syl += nsylCMU(item)
            except:
                print("cmudict is missing: "+item)
                try:
                    syl += nsylScrape(item)
                except:
                    print("hms is missing: "+item)
                    try:
                        syl += len(hyphenate_word(item))
                        return syl
                    except:
                        print("Error for: "+item)
                        return 0
        return syl

    else:
        try:
            syl = nsyl(word)
            return syl
        except:
            print("cmudict is missing: "+word)
            try:
                syl = nsylScrape(word)
                return syl
            except:
                print("hms is missing: "+word)
                try:
                    syl = len(hyphenate_word(word))
                    return syl
                except:
                    print("Error for: "+word)
                    return 0

def countSentSyl(markedSent):
    """A list of tuples, wherein item[1] is the syl count for word (item[0]),
    return the total number of syllables for the sentence (aka the list).

    :param markedSent: the marked sentence you already have syllable data for.
    :output: an integer that is the sum of syllables for the marked sentence.
    """
    return sum([item[1] for item in markedSent])

def sentPrint(markedSent):
    """Print out the syllable count each word in a marked sentence has.

    :param markedSent: list of tuples containing syllable data for a sentence.
    :output: nothing is returned. Words and their syllable counts are printed.
    """
    for item in markedSent:
        print(unicode(item[1])+" "+unicode(item[0]))

def tupleListToList(listName,tupleIndex):
    """Takes a list of tuples (listName), and returns a list of the tuples'
    content being stored at a given Index (tupleIndex)
    """
    # Note: this is a shoddy, and poorly optimized way of doing this, however
    # if I read up on maps and lambda, I can change it later.
    tempList = []
    for item in listName:
        tempList.append(item[tupleIndex])

    return tempList

def removeStopWords(tSent):
    english_stops = set(stopwords.words('english'))

    if type(tSent[0]) == str:
        words = set([item for item in tSent])
        goodWords = [word for word in words if word.lower() not in english_stops]
        return goodWords
    elif type(tSent[0]) == tuple:
        tempSent = [item for item in tSent if item[0].lower() not in english_stops]

        # remove the duplicates.
        return list(set(tempSent))

def isStopWord(word):
    english_stops = set(stopwords.words('english'))
    return word.lower() not in english_stops


def isHaiku(sentenceString):
    # tokenize the sentence, make ascii, remove punctuation.
    tSent = tokenSent(sentenceString)
    print(tSent)

    # create a list of tupled data for words and their syl count for the sent.
    sentData = getSyl(tSent)
    sentPrint(sentData) # for debugging.

    goodWords = removeStopWords(tSent)
    print(goodWords)
    gSentData = getSyl(goodWords)
    sentPrint(gSentData)

    # sum up the total number of syl for the sentence using item[1] in tuples
    totalSylCount = countSentSyl(sentData)
    print(totalSylCount)
    if totalSylCount == 17:
        print("Sentence could be a haiku.")
        f.write(unicode(printSent(tSent)).encode("UTF-8"))
    elif (7 < totalSylCount < 27):
        # If it's fairly close, save it anyway so we can examine it later.
        f.write((unicode(totalSylCount)+u"\n").encode("UTF-8"))
        f.write((unicode(printSent(tSent))).encode("UTF-8"))
        f.write((u"\n\n").encode("UTF-8"))
    else:
        print(str(totalSylCount)+" != 17.")

# ==============================   MAIN TEST   =================================
# text = scrapePage("constantinople")
# good_sent = tokenPara(text)
# for sent in good_sent:
#     isHaiku(sent)
# f.close()
# ============================   END MAIN TEST   ===============================
# ===========================   REFERENCE TESTS   ==============================

# sent = "It possessed a proconsul rather than an urban prefect."
# isHaiku(sent)

# # sent = ['It', 'possessed', 'a', 'proconsul', 'rather', 'than', 'an', 'urban', 'prefect']
# tsent = [("It", 1),
# ("possessed", 2),
# ("a", 1),
# ("proconsul", 3),
# ("rather", 2),
# ("than", 1),
# ("an", 1),
# ("urban", 2),
# ("prefect", 2)]
#
# sylCount = sum([item[1] for item in tsent])
#
# """
# Now, we need to not only scrape every single synonym for the words, but also
# find the syllable count for all of the synonyms. However, we need to make sure
# that we optimize it by filtering out duplicate synonyms first.
# """
# english_stops = set(stopwords.words('english'))
# words = set([item[0] for item in tsent])
# goodWords = [word for word in words if word.lower() not in english_stops]
#
# wordData = []
# for item in goodWords:
#     print("Finding "+item)
#     syn = findSynonyms(item)
#     if syn:
#         synonymSyllables = []
#         for synitem in syn:
#             synonymSyllables.append((synitem,getWordSyl(synitem)))
#         wordData.append((item,synonymSyllables))
#
# pprint.pprint(wordData)
# =========================   END REFERENCE TESTS   ============================














#
