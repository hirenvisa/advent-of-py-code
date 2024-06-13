class Solution(object):
    def minMovesToSeat(self, seats, students):
        return sum(abs(a-b)
        for a,b in zip(
            sorted(students),
            sorted(seats)
        ))
    
    def minMovesToSeat1(self, seats, students):
        
        n = len(seats)
        freqSeats = [0] * 100
        freqStudents = [0] * 100
        for i in range(0, n):
            freqSeats[seats[i]] += 1
        for j in range(0,n):
            freqStudents[students[j]] += 1


        # <TODO: PENDING> 

        
class main():
    seats = [3,1,5]
    students = [2,7,4]

    s = Solution()

    ans = s.minMovesToSeat(seats, students)
    print(ans)