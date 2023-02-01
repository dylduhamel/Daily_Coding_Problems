# There is a better solution with a TRIE tree, so please look at that
def autocomplete(str, possStr):
    resultArr = []

    for i in possStr:
        if i[:len(str)] == str:
            resultArr.append(i)
    return resultArr

str = "de"
possStr = ["dog", "deer", "deal"]

print(autocomplete(str, possStr))