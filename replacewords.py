class Solution():
    def findRoot(self, word, dictSet):
        for i in range(1, len(word)):
            if word[:i] in dictSet:
                return word[:i]            
        return word
    
    def replaceWord(self, dict, sentence):
        dictSet = set(dict)
        words = sentence.split(' ')

        returnList = [self.findRoot(w, dictSet) for w in words]
        return ' '.join(returnList)

class main():
    dict = ["cat","bat","rat"]
    sentence =  "the cattle was rattled by the battery"

    sol = Solution()
    print(sol.replaceWord(dict, sentence))
