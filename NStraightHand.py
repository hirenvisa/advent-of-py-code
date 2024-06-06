import heapq
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        dict = {}
        for h in hand:
            dict[h] = 1 + dict.get(h,0)
        
        minHeap = list(dict.keys())
        heapq.heapify(minHeap)

        while(minHeap):
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in minHeap:
                    return False
                dict[i] -= 1

                if(dict[i] == 0):
                    if(minHeap[0] != i):
                        return False
                    heapq.heappop(minHeap)
        return True
        


class main():
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    s = Solution()
    print(s.isNStraightHand(hand, groupSize))