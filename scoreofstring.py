class solution:
    def scoreofstring(self, s: str) -> int:
        if len(s) < 2: 
            return 0
        
        score = 0
        for i in range(0, len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))

        return score
    

class main():
    s = "zaz"
    obj = solution()
    print(obj.scoreofstring(s))
    
    
