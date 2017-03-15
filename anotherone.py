from main import *
from pprint import pprint
import numpy as np

debugMode = True
def dprint(inputItem):
    # debugMode is a global.
    if debugMode == True:
        pprint(inputItem)

# =================================   MAIN   ===================================
sent = "It possessed a proconsul rather than an urban prefect."

# tokenize the origin sentence.
tsent = tokenSent(sent)
dprint(tsent)

# identify the words in the sentence as noun, verb, adjective, etc.
tagSent = pos_tag(tsent)
dprint(tagSent)

# find the syllable count for all of the words
    # check if cmudict has data on this already
    # check the pickle file to see if we have already scraped syllable data for this word
        # if not, scrape it.
        # if we can't find syllable data for it on the internet, use the hyphenation algorithm

# Go through the words for the sentence, and highlight the important words that we might be able to find useful synonyms for (we're going to call them "non-stop words")
# (basically, ignore "the", "and", "if", etc.)

# Find the synonyms for the nonStopWords.

# Find the syllables for the synonyms of the nonStopWords.
# ===============================   END MAIN   =================================
























#
# sentData = getSentSyl(tsent) # count syllables for the words.
#
# # find the words to focus on. We shall call these non-stop (NS) words.
# nsWords = removeStopWords(sentData)
# dprint(nsWords)
#
# # For the non-stop words, go through and find their synonyms. We shall be using
# # these to lengthen or shorten the syllable count for a sentence. Store the data
# # in a dictionary.
#
#
# ### SYNONYMS
# nsDict = {}
# for item in nsWords:
#     # search for the word's synonyms.
#     word = item[0]
#     print('\n**Searching '+word+'**')
#
#     # in the dictionary, each nsWord is going to have its own list of synonyms,
#     # wherein each synonym will be stored in a tuple along with its syl count.
#
#     # store the synonyms for the word
#     currentWordSyns = findSynonyms(word)
#
#     # go through the synonyms we have, finding their syllable count.
#     currentWordSynSyls = []
#     try:
#         for synonym in currentWordSyns:
#             currentWordSynSyls.append((synonym,getWordSyl(synonym)))
#             nsDict[word] = currentWordSynSyls
#     except TypeError:
#         print('No synonyms for '+str(word))
#         # If there are no synonyms, don't add it to nsDict. Doing otherwise
#         # confuses the analysis portion of this.
# # =============================   END SYNONYMS   ===============================
#
#
# # ===============================   ANALYSIS   =================================
# # I need to look through the origin sentence, and the amount of syllables it has
# # Find the number of syllables in the original sentence.
# totalSyl = sum([item[1] for item in sentData])
# dprint(totalSyl)
# # Find the number of sylables in the non-stop words in the sentence.
# nsSyl = sum([item[1] for item in nsWords])
# dprint(nsSyl)
#
# # I need to compare this number to 17, what a haiku is, thus calculating the
# # required change in syllables.
# neededSyl = 17 - totalSyl # positive if I need more syllables, negative if opp.
# finalNSSyl = nsSyl + neededSyl
#
# # Given the number of syllables I need to meet, and the number of words
# # available for me to change, I need to figure out how many syllables per word
# # I need to change.
# """I can't just measure the length of NSwords, as I removed
# the duplicates in this, so I have to check for how many times the words in the
# original sentence show up in here."""
# # the number of words in the original sentence that can be manipulated in order
# # to meet neededSyl and finalNSSyl.
# goodWordsCount = len(
#     [word for word in tsent if word in nsDict])
#
# neededSylPerWord = float(neededSyl) / float(goodWordsCount)
#
# # Some words are more flexible than others, as they either have more synonyms,
# # or synonyms covering a larger range of syllables.
# # Pick the best (easiest) words to change, and their syllables.
# """
# I can use tupleListToList() to single out the syllable counts in nsDict for a
# given goodWord, and then analyse these numbers."""
# nsDictAnalysis = {}
# for item in nsWords:
#     word = item[0]
#     dprint(word)
#     syllableData = tupleListToList(nsDict[word],1)
#     dprint(syllableData)
#     nsDictAnalysis[word] = {
#         'syl' : list(set(syllableData)),
#         'mean' : np.mean(syllableData),
#         'min' : min(syllableData),
#         'max' : max(syllableData)
#     }
#
# dprint(nsDictAnalysis)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # =============================   END ANALYSIS   ===============================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
