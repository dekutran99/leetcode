
class Solution:
    def minCost(self, s: str, neededTime: List[int]) -> int:
        result  = 0

        record = {}
        for i in range(len(s)):
            repeatedIdx = record.get(s[i])
            if repeatedIdx == None:
                record[s[i]] = i
            else:
                if repeatedIdx == i - 1:
                    if neededTime[i] <= neededTime[repeatedIdx]:
                        result += neededTime[i]
                        neededTime[i] = neededTime[repeatedIdx]
                    else:
                        result += neededTime[repeatedIdx]
                record[s[i]] = i
                
        return result