import collections
from functools import reduce


class Solution(object):
    def commonChars(self, words):

        common_char = []
        char_count = {}

        for char in words[0]:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for word in words[1:]:
            current_char_count = {} 
            for char in word:
                if char in current_char_count:
                    current_char_count[char] += 1
                else:
                    current_char_count[char] = 1

            for char in char_count:
                if char in current_char_count:
                    char_count[char] = min(char_count[char], current_char_count[char])
                else:
                    char_count[char] = 0 
        
        for char in char_count:
            for j in range(char_count[char]):
                common_char.append(char)

        return common_char

    def CommonChars1(self, words):
        str = reduce(lambda a, b: a & b, map(collections.Counter, words)).elements();

        return list(str)
        

class main():
    words = ["bella","label","roller"]
    sol = Solution()
    ans = sol.CommonChars1(words)

    print(ans)
    