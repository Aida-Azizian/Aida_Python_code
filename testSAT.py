import sys
from stringalignment import StringAlignmentTable as StringAlignmentTable

lev = StringAlignmentTable('impopulaires', 'popular')
lev.levenshtein()
print(lev)

def fileToList(file):
    with open(file) as f:
        dict = f.readlines()
    return [x.strip() for x in dict] 

dict1 = fileToList('dict1.txt')
afew = fileToList('afewwords.txt')

def mostSimilar(wrd,dict):
    bestMatch = ''
    bestDist = sys.maxsize # much larger than real values
    for dictEntry in dict:
        lev = StringAlignmentTable(wrd,dictEntry)
        dist = lev.levenshtein()
        if (dist < bestDist):
            bestMatch = dictEntry
            bestDist = dist
    return (bestMatch,bestDist)

for wrd in afew:
    print (wrd,mostSimilar(wrd,dict1))

