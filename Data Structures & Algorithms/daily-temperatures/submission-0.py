class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        b=len(temperatures)
        a=[0]*b
        for x in range(b):
            days=0
            temp=x+1
            found = False
            while temp < b:
                if temperatures[temp] > temperatures[x]:
                    days += 1
                    found = True
                    break
                else:
                    days += 1
                    temp += 1

            if not found:
                days = 0
            a[x]=days
        return a  