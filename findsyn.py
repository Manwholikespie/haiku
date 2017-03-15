from nltk import tokenize
from nltk.corpus import stopwords
import thesaurus as thes
import pprint
import math

# sent = ['It', 'possessed', 'a', 'proconsul', 'rather', 'than', 'an', 'urban',
# 'prefect']
tsent = [("It", 1),
("possessed", 2),
("a", 1),
("proconsul", 3),
("rather", 2),
("than", 1),
("an", 1),
("urban", 2),
("prefect", 2)]

sylCount = sum([item[1] for item in tsent])

# calculate the number of syllables we need to achieve haiku status.
neededSyl = 17 - sylCount
if neededSyl == 0:
    print("This sentence is already a haiku.")
    exit()

wordData = [('urban',
  [('downtown', 2),
   ('civil', 2),
   ('metropolitan', 5),
   ('civic', 2),
   ('central', 2),
   ('municipal', 4),
   ('popular', 3),
   ('public', 2),
   ('town', 1),
   ('village', 2),
   ('burghal', 2),
   ('citified', 3),
   ('inner-city', 4),
   ('nonrural', 3),
   ('oppidan', 3)]),
 ('rather',
  [('fairly', 2),
   ('pretty', 2),
   ('kind of', 2),
   ('comparatively', 5),
   ('quite', 1),
   ('somewhat', 2),
   ('slightly', 2),
   ('relatively', 4),
   ('enough', 2),
   ('more or less', 3),
   ('reasonably', 4),
   ('so-so', 2),
   ('some', 1),
   ('something', 2),
   ('sort of', 1),
   ('a bit', 2),
   ('a little', 3),
   ('averagely', 4),
   ('in a certain degree', 4),
   ('passably', 3),
   ('ratherish', 3),
   ('to some degree', 3),
   ('to some extent', 3),
   ('tolerably', 4)]),
 ('possessed',
  [('enchanted', 3),
   ('haunted', 2),
   ('gone', 1),
   ('obsessed', 2),
   ('hooked', 1),
   ('cursed', 1),
   ('crazed', 1),
   ('raving', 2),
   ('berserk', 2),
   ('demented', 3),
   ('fiendish', 2),
   ('frenetic', 3),
   ('frenzied', 2),
   ('insane', 2),
   ('into', 2),
   ('mad', 1),
   ('violent', 3),
   ('consumed', 2),
   ('enthralled', 2),
   ('bedeviled', 3),
   ('taken over', 2)])]

def findSentRange(tsent,wordData):
    """Will find the max and min sentence length that it can construct with a
    given corpus of syllables.

    :output: a tuple wherein the data is formatted: (min,max).
    """
    # the words in the sentence that are available to replace
    editableWords = [item[0] for item in wordData]

    """
    First, it would be nice to make sure that we are even able to make a sentence
    that is made of 17 syllables. To do this, we shall calculate the syl range.
    """
    # add up the max number of syllables in the sentence, starting with the
    # longest synonyms for the words that can be replaced.
    sylSum = sum([max(item[1], key=lambda x:x[1])[1] for item in wordData])
    for word in tsent:
        if word not in editableWords:
            sylSum += word[1]
    sentMax = sylSum

    # now, we are going to find the minimum number of syllables, however this has
    # to be done with repsect to both the synonyms that we collected for the
    # replaceable words, and also the syllable count of the original words.
    sylSum = sum([min(item[1], key=lambda x:x[1])[1] for item in wordData])
    for word in tsent:
        if word[0] not in editableWords:
            sylSum += word[1]
        else:
             for item in wordData:
                 if item[0] == word:
                    if min(item[1], key=lambda x:x[1])[1] <= word[1]:
                        sylSum += min(item[1], key=lambda x:x[1])[1]
                    else:
                        sylSum += word[1]
    sentMin = sylSum

    return (sentMin,sentMax)

print findSentRange(tsent,wordData)

# calculate the average number of syllables for each possible synonym, so that
# we can keep a word's syllable count somewhat consistent.
meanSyllables = {}
for word in wordData:
    sylCountList = [syl[1] for syl in word[1]]
    meanSynSyl = float(sum(sylCountList))/float(len(sylCountList))
    # print('sum',sum(sylCountList))
    # print('count',len(sylCountList))
    meanSyllables[word[0]] = meanSynSyl
print meanSyllables

# calculate the number of syllables we have to create with the words we have
# synonyms for.
# count the number of syllables for non-wordData words
badWordSylCount = 0
for word in tsent:
    if word[0] not in [item[0] for item in wordData]:
        badWordSylCount+=word[1]
goodWordNeededSyl = 17 - badWordSylCount
print ('badWordSylCount',badWordSylCount)
print ('goodWordNeededSyl',goodWordNeededSyl)

if neededSyl > 0:
    # We need to pick lengthier synonyms.
    """goodWordNeededSyl is the amount of synonyms we need to make 17.
    This number, divided by the length of wordData, is (on average) the
    number of syllables that each synonym needs to have.
    However, because not ever word will (on average) have available synonyms
    compareable to this number, we need to calculate the difference between
    the average of both the synonyms we need, and the synonyms we have."""
    # Choose which synonym we are going to use for each word in wordData
    remainingSyllables = goodWordNeededSyl
    for item in wordData:




if neededSyl < 0:
    """We need to pick shorter synonyms.
    """



















#
