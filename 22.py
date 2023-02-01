# IMPORTANT DICT METHOD
def sentenceReconstruct(string, dictionary):
    wordDict = dict.fromkeys(dictionary, True)
    stringReconstruct = ""
    foundWords = []
    
    for char in string:
        stringReconstruct += char

        try:
            wordDict[stringReconstruct]
            foundWords.append(stringReconstruct)
            stringReconstruct = ""
        except KeyError as error:
            pass

    if foundWords:
        return foundWords
    else:
        return None

# Better solution
# Think recursively, I mean look at the sentence?!
# But 2^N time complexity
# There is a dynamic programming solution on website
def find_sentence(dictionary, s):
    sentence, valid = find_sentence_helper(dictionary, s)
    if valid:
        return sentence

def find_sentence_helper(dictionary, s):
    if len(s) == 0:
        return [], True

    result = []
    for i in range(len(s) + 1):
        prefix, suffix = s[:i], s[i:]
        if prefix in dictionary:
            rest, valid = find_sentence_helper(dictionary, suffix)
            if valid:
                return [prefix] + rest, True
    return [], False
testString = "bedbathandbeyond"
dictionary = ['bed', 'bath', 'bedbath', 'and', 'beyond']

print(sentenceReconstruct(testString, dictionary))