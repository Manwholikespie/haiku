import nltk
from main import *
import thesaurus
from pprint import pprint  # for pretty debugging and stuff.

sent = "It possessed a proconsul rather than an urban prefect."

# tokenize the origin sentence, and analyze its stop words to find the
# important elements within it.
tsent = tokenSent(sent)
nsWords = removeStopWords(tsent)

# identify the words in the sentence as noun, verb, adjective, etc.
tagSent = nltk.pos_tag(tsent)

# count the syllables for the words in the sentence, and check if they are
# a stop word.
for x in xrange(0, len(tagSent)):
    tagSent[x] += (getWordSyl(tagSent[x][0]),)
    if tagSent[x][0] in nsWords:
        tagSent[x] += (True,)
    else:
        tagSent[x] += (False,)
pprint(tagSent)

# get the syllables for the words that aren't stop words.
for x in xrange(0, len(tagSent)):
    item = tagSent[x]

    if item[3] != True:
        tagSent[x] += ({},)
        print(tagSent[x])
    elif item[3] == True:
        print('\n\n')
        word = item[0]
        partOfSpeech = item[1]

        if 'JJ' in partOfSpeech:
            thesPOS = 'adj'
        elif 'NN' in partOfSpeech:
            thesPOS = 'noun'
        elif 'RB' in partOfSpeech:
            thesPOS = 'adv'
        elif 'VB' in partOfSpeech:
            thesPOS = 'verb'
        else:
            # If it isn't something specific, it is going to be vague. Just use
            # the first one that pops up.
            thesPOS = 'first'

        print(word + ' (' + thesPOS + ')')

        # grab the synonyms from thesaurus.com
        currentWordData = thesaurus.getWord(word)

        if not currentWordData:
            # If there aren't any definitions for the word, go on to the next
            # iteration. There isn't anything here.
            tagSent[x] += ({},)  # add a blank synonyms dictionary.
            print(tagSent[x])
            continue

        correctPOSIndexes = []
        for x in xrange(0, len(currentWordData)):
            currentSylData = currentWordData[str(x)]
            # print(currentSylData['partOfSpeech'])
            # print(currentSylData['meaning'])

            if currentSylData['partOfSpeech'] == thesPOS:
                # This is the correct part of speech for the word we are using.
                # There is a possibliity it isn't the right definition, though.
                correctPOSIndexes.append((x, currentSylData['meaning']))

        # confirm correctness of word definition.
        if len(correctPOSIndexes) > 1:
            # There are more than one possibly correct word, based on POS.
            # Ask the user which definition is the best fit.
            print('Your sentence is:\n\t' + sent)
            print('For the word "' + word + '", the best definition is:')

            for x in xrange(0, len(correctPOSIndexes)):
                """correctPOSIndexes[x][0] is its index in currentWordData{}.
                correctPOSIndexes[x][1] is its definition.
                """
                print(str(x) + ' ' + correctPOSIndexes[x][1])

            useNumber = int(raw_input(' > '))
            tagSent[
                x] += (currentWordData[str(correctPOSIndexes[useNumber][0])],)
            print(tagSent[x])
            print('Using: ' + correctPOSIndexes[useNumber][1])

        elif len(correctPOSIndexes) < 1:
            print('No correct POS available.')
            print('Possible error on nltk\'s end. Available definitions:')
            for x in xrange(0, len(currentWordData)):
                currentSylData = currentWordData[str(x)]
                print(str(x) + ': ' + currentSylData['meaning'])

            useNumber = int(
                raw_input('\nI would like to use number: (Ex: 0, 1, 2)\n > '))
            tagSent[x] += (currentWordData[str(useNumber)],)
            print(tagSent[x])
            print('Using: ' + currentWordData[str(useNumber)]['meaning'])

        else:
            tagSent[x] += (currentWordData[str(correctPOSIndexes[0][0])],)
            print(tagSent[x])
            print('Using: ' + correctPOSIndexes[0][1])

pprint(tagSent)
#
