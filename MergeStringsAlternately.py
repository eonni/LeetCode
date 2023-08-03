def mergeAlternately(self, word1, word2):
    finalword = []
    for i in range(len(word1)):
        finalword.append(word1[i])
        finalword.append(word2[i])
