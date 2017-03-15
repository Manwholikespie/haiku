"""
    When searching a word (ex: "small"), the synonyms are grouped into three
    categories, differing in presentation by a change in the background color
    of their <span> object.

    The categories are as follows:
        relevant-1
        relevant-2
        relevant-3

    The higher the integer suffix, clearly, the more relevant it is.

    As for the antonyms, they are grouped similarly- however they are of value:
        relevant--1
        relevant--2
        relevant--3

    ...wherein (-3) is the best matching antonym.
"""
# external libraries
import requests
from bs4 import BeautifulSoup

def findRankedSynonyms(inputWord,rank):
    """Find the synonyms of a word according to a certain relevance level.

    @param inputWord: The word you wish to search for
    @param rank: An integer (1-3) referencing the relevance rank of the word,
        where 3 is the most relevant and 1 is somewhat fitting.
    @return: A list of synonyms that fit the relevance you searched for.
    @rtype: List
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the synonyms
        wordDict = {}
        wordDict['syn3'] = []
        wordDict['syn2'] = []
        wordDict['syn1'] = []
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant-3":
                wordDict['syn3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant-2":
                wordDict['syn2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant-1":
                wordDict['syn1'].append(str(word.text))
                # print(word.text)
            else:
                break

        return wordDict['syn' + str(rank)]

def findRankedAntonyms(inputWord,rank):
    """Find the antonyms of a word according to a certain relevance level.

    @param inputWord: The word you wish to search for
    @param rank: An integer (1-3) referencing the relevance rank of the word,
        where 3 is the most relevant and 1 is somewhat fitting.
    @return: A list of synonyms that fit the relevance you searched for.
    @rtype: List
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the antonyms
        wordDict = {}
        wordDict['ant3'] = []
        wordDict['ant2'] = []
        wordDict['ant1'] = []
        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant--3":
                wordDict['ant3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant--2":
                wordDict['ant2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant--1":
                wordDict['ant1'].append(str(word.text))
                # print(word.text)

        return wordDict['ant' + str(rank)]

def findSynonyms(inputWord):
    """Find all synonyms of a word.

    @note: The returned list of synonyms is not sorted in any way, and is also
        according to the first definition that thesaurus.com has set for the
        word.
    @param inputWord: The word you wish to search for
    @return: A list of all synonyms for a given word.
    @rtype: List
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a list to hold all the synonyms
        synonyms = []

        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            # if relevanceLevel == "relevant-1":
            #     print("***** - " + word.text + " " + str(relevanceLevel))
            # else:
            #     print(word.text + " " + str(relevanceLevel))
            if (relevanceLevel == "relevant-3"):
                # print(word.text)
                synonyms.append(str(word.text)) # using str() to remove unicode u''
            elif (relevanceLevel == "relevant-2"):
                # print(word.text)
                synonyms.append(str(word.text))
            elif (relevanceLevel == "relevant-1"):
                # print(word.text)
                synonyms.append(str(word.text))
            else:
                """
                Thanks to thesaurus.com's developers, there are sometimes up to
                11 copies of given words. (Ex: search for /browse/baby on the
                page for the word "big"). In order to combat this, I am stopping
                the loop before it reaches the antonyms, as it repeats afterwards.

                I may eventually change this to only select elements with background
                colors or font weights, as the hidden words do not have any styles.
                """
                break

        return synonyms

def findAntonyms(inputWord):
    """Find all antonyms of a word.

    @note: The returned list of antonyms is not sorted in any way, and is also
        according to the first definition that thesaurus.com has set for the
        word.
    @param inputWord: The word you wish to search for
    @return: A list of all antonyms for a given word.
    @rtype: List
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a list to hold all the antonyms
        antonyms = []

        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            # print(relevanceLevel + word.text)
            if relevanceLevel == "relevant--3" or "relevant--2" or "relevant--1":
                antonyms.append(str(word.text)) # using str() to remove unicode u''

        return antonyms\

def findWord(inputWord):
    """Combine both synonyms and antonyms into a large dictionary of multiple itemtypes.

    @note: Now, I was considering having this just call the findRankedAntonyms and
    findRankedSynonyms and building the dictionary this way... However that
    is much slower. Here are the times as comparison:
    # individual function calls
            2.39 real         0.93 user         0.06 sys
            2.24 real         0.94 user         0.05 sys
            1.86 real         0.98 user         0.06 sys
            average : 2.1633333333
    # normal function
            0.55 real         0.25 user         0.04 sys
            0.37 real         0.24 user         0.03 sys
            0.37 real         0.24 user         0.03 sys
            average: 0.4033333333

    as you can see, it is much faster to use the current html document than
    calling a function that has to reload it each time.

    @param inputWord: the word you wish to search for.
    @return: A dict containing the synonyms and antonyms of a word's first
        definition. Total elements:
            Dict = {
                # lists of synonyms according to rank
                'syn1' = []
                'syn2' = []
                'syn3' = []

                # lists of antonyms according to rank
                'ant1' = []
                'ant2' = []
                'ant3' = []
            }
    @rtype: Dict
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the antonyms
        wordDict = {}

        # synonyms
        wordDict['syn3'] = []
        wordDict['syn2'] = []
        wordDict['syn1'] = []

        #antonyms
        wordDict['ant3'] = []
        wordDict['ant2'] = []
        wordDict['ant1'] = []
        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant--3":
                wordDict['ant3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant--2":
                wordDict['ant2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant--1":
                wordDict['ant1'].append(str(word.text))
                # print(word.text)

        wordTags = soup.select("div#synonyms-0 div#filters-0 div.relevancy-block div.relevancy-list ul li a span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant-3":
                wordDict['syn3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant-2":
                wordDict['syn2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant-1":
                wordDict['syn1'].append(str(word.text))
                # print(word.text)

        return wordDict

def findWordType(inputWord,type):
    """Same as findAntonyms or findSynonyms, however it returns them in a dictionary organized by relevance.

    @param inputWord: the word you wish to search for.
    @param type: synonym or antonym - represented by 'syn' or 'ant'.
    @return: a dictionary either of synonyms or antonyms. The output depends on
        the type parameter...
        If type is 'syn', there are elements: ['syn1'],['syn2'],['syn3'].
        If type is 'ant', there are elements: ['ant1'],['ant2'],['ant3'].
    @rtype: Dict.
    """
    type = cleanInput(type)

    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the antonyms
        wordDict = {}
        if type == 'syn':
            # synonyms
            wordDict['syn3'] = []
            wordDict['syn2'] = []
            wordDict['syn1'] = []

            wordTags = soup.select("div#synonyms-0 div#filters-0 div.relevancy-block div.relevancy-list ul li a span.text")

            for word in wordTags:
                relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
                if relevanceLevel == "relevant-3":
                    wordDict['syn3'].append(str(word.text)) # using str() to remove unicode u''
                    # print(word.text)
                elif relevanceLevel == "relevant-2":
                    wordDict['syn2'].append(str(word.text))
                    # print(word.text)
                elif relevanceLevel == "relevant-1":
                    wordDict['syn1'].append(str(word.text))
                    # print(word.text)
        elif type == 'ant':
            #antonyms
            wordDict['ant3'] = []
            wordDict['ant2'] = []
            wordDict['ant1'] = []

            wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

            for word in wordTags:
                relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
                if relevanceLevel == "relevant--3":
                    wordDict['ant3'].append(str(word.text)) # using str() to remove unicode u''
                    # print(word.text)
                elif relevanceLevel == "relevant--2":
                    wordDict['ant2'].append(str(word.text))
                    # print(word.text)
                elif relevanceLevel == "relevant--1":
                    wordDict['ant1'].append(str(word.text))
                    # print(word.text)
        elif type == "all":
            wordDict = findWord(inputWord)
        else:
            print("ERROR: Not 'ant', 'syn', or 'all'.")
            return {}

        return wordDict

def cleanInput(inputString):
    """makes strings lowercase and cleans them up for searching thesaurus.com

    @note: Users shouldn't need to use this. This is mainly used within other
        existing functions
    @return: A cleaned up version of the inputted string.
    @rtype: string
    """
    inputString = inputString.lower()

    return inputString

def findWordTotal(inputWord):
    """Find all synonyms and antonyms for all of a given word's definitions.

    @note: Usually thesaurus.com's default definition for a word contains
        enough data to work with, however- in the offchance that you wish to use
        other definitions of the word, you can use this to acquire said data.
    @param inputWord: the word you wish to search for.
    @return: A large dictionary whose top hierarchical elements are dictionaries
        of named with integers from 0 to n-1, where n is the total amount of
        definitions. Ex: findWordTotal(inputWord) returns a dict of:
            {
                '0' = {
                    ['syn3'] = []
                    ['syn2'] = []
                    ['syn1'] = []
                    ['ant3'] = []
                    ['ant2'] = []
                    ['ant1'] = []
                    ['partOfSpeech'] = []
                    ['meaning'] = []
                }
                '1' = {...} # the following are of similar content, save for
                '2' = {...} # their meaning (and sometimes partOfSpeech)
                '3' = {...}
                '4' = {...}
            }
        Thus, there are 5 definitions for the word, each with their respective
        meaning, partOfSpeech, synonyms, and antonyms- each of different relevance
        rank of course.
    @rtype: dict
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        wordDict = {}
        wordDict['partOfSpeech'] = []
        wordDict['meaning'] = []

        tabTags = soup.select("div.mask ul li")
        for item in tabTags:
            wordDict['partOfSpeech'].append(str(item.select("em.txt")[0].text)) # adj, adv, noun, etc.
            wordDict['meaning'].append(str(item.select("strong.ttl")[0].text)) # word meaning

        for x in xrange(0,len(wordDict['meaning'])):
            # print wordDict['partOfSpeech'][x] + ": " + wordDict['meaning'][x]

            # MAKE THE DICT!
            wordDict[str(x)] = {}
            wordDict[str(x)]['partOfSpeech'] = wordDict['partOfSpeech'][x]
            wordDict[str(x)]['meaning'] = wordDict['meaning'][x]
            wordDict[str(x)]['syn3'] = []
            wordDict[str(x)]['syn2'] = []
            wordDict[str(x)]['syn1'] = []
            wordDict[str(x)]['ant3'] = []
            wordDict[str(x)]['ant2'] = []
            wordDict[str(x)]['ant1'] = []

            # GET THE DATA!
            # antonyms
            wordTags = soup.select("div#synonyms-" + str(x) + " section.container-info.antonyms div.list-holder ul.list li a span.text")
            for word in wordTags:
                relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
                if relevanceLevel == "relevant--3":
                    wordDict[str(x)]['ant3'].append(str(word.text)) # using str() to remove unicode u''
                    # print(word.text)
                elif relevanceLevel == "relevant--2":
                    wordDict[str(x)]['ant2'].append(str(word.text))
                    # print(word.text)
                elif relevanceLevel == "relevant--1":
                    wordDict[str(x)]['ant1'].append(str(word.text))
                    # print(word.text)



            #synonyms
            wordTags = soup.select("div#synonyms-" + str(x) + " div#filters-0 div.relevancy-block div.relevancy-list ul li a span.text")
            for word in wordTags:
                relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
                if relevanceLevel == "relevant-3":
                    wordDict[str(x)]['syn3'].append(str(word.text)) # using str() to remove unicode u''
                    # print(word.text)
                elif relevanceLevel == "relevant-2":
                    wordDict[str(x)]['syn2'].append(str(word.text))
                    # print(word.text)
                elif relevanceLevel == "relevant-1":
                    wordDict[str(x)]['syn1'].append(str(word.text))
                    # print(word.text)

        del wordDict['partOfSpeech']
        del wordDict['meaning']

        # ===========================   BEGIN DEBUGGING   ======================
        # for x in xrange(0,len(wordDict)):
        #     print("\n" + str(x) + ":")
        #     print wordDict[str(x)]
        # ============================   END DEBUGGING   =======================

        return wordDict

def findExamples(inputWord):
    """Find example sentences for a word.

    @param inputWord: the word you wish to search for
    @return: a list of example sentences for the inputted word.
    @rtype: list
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        examples = []

        exampleTag = soup.select("div#example-sentences div p")
        for item in exampleTag:
            examples.append(str(item.text.replace("\n","").replace("\r","").replace("        ","").replace("    ","")))

        return examples

def findOrigin(inputWord):
    """Find the origin of a word.

    @param inputWord: the word you wish to search for.
    @return: a long string containing the origin entry for the word-origin
    @rtype: a long string.
    """
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        originTag = soup.select("div#word-origin div p")
        origin = [str(item.text.replace("\n","").replace("\r","").replace("        ","").replace("    ","")) for item in originTag][0]
        # origin = []
        # for item in exampleTag:
        #     examples.append(str(item.text.replace("\n","").replace("\r","").replace("        ","").replace("    ","")))
        return origin

def getWord(inputWord):
    """Grab all data, across all definitions and parts of speech for a word.
    A current downside is that the data isn't all that organized.
    """
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
        return {}
    else:
        # No errors. Let the show go on.
        pass

    # initialize a dictionary to hold all the antonyms
    wordDict = {}

    # find the different parts of speech, and their meanings.
    posTags = soup.select("div.mask a.pos-tab")
    definitionCount =  len(posTags)
    for item in posTags:
        """The number of the item is stored in its data-id.
        Its POS is in the <em.txt> below it.
        Its meaning is in the <strong.ttl> also below it.
        """
        definitionNumber = str(item['data-id'])  # 0, 1, 2, etc.
        wordDict[definitionNumber] = {}
        wordDict[definitionNumber]['partOfSpeech'] = [
            word.text for word in item.select('em')][0]
        wordDict[definitionNumber]['meaning'] = [
            word.text for word in item.select('strong')][0]

    # Find the synonyms and antonyms for each definition.
    for x in xrange(0,definitionCount):
        # x corresponds to the current number of the definition.
        for y in xrange(-3,3+1):
            if y < 0:
                wordDict[str(x)]['ant'+str(abs(y))] = []
            elif y > 0:
                wordDict[str(x)]['syn'+str(y)] = []

        # synonyms
        wordTags = soup.select("div#synonyms-"+str(x)+" div#filters-"+str(x)+" div.relevancy-block div.relevancy-list ul li a span.text")
        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            relevanceNumber = relevanceLevel[len(relevanceLevel)-1] # end char is the number
            wordDict[str(x)]['syn'+relevanceNumber].append(str(word.text))

        # antonyms
        wordTags = soup.select("div#synonyms-"+str(x)+" section.container-info.antonyms div.list-holder ul.list li a span.text")
        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            relevanceNumber = relevanceLevel[len(relevanceLevel)-1] # end char is the number
            wordDict[str(x)]['ant'+relevanceNumber].append(str(word.text))

    return wordDict

"""
It has come to my attention that I have a lot of functions in this library,
all with names that bear little resemblence to their functionality. In other
words-- I need to rename them, possibly also re-work them in a way that makes
it easier on people using this library.
"""

"""
Let's think about what I want people to be able to do-- and thus which functions
can stay the way they are...

People need to:
- get all the synonyms AND antonyms of a word.
- get all the synonyms/antonyms of a word.
- get synonyms/antonyms of a certain quality (relevance)
- search a word in a specific grammatical function (noun, adverb, etc.)
- search a word in a specific meaning (def1, def2, etc.)
- get a word's origin and history.
- get example sentences for a word.

This should be good for now.
"""

"""
The functions I need:
Get ALL the data for a specific word (no matter how many requests).
    - word complexity, relevancy, length
"""






























#
