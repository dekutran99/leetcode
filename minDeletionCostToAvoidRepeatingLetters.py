class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        record = {}
        out  = 0
        N = len(s)
        for i in range(N):
            repeatedIdx = record.get(s[i])
            if repeatedIdx == None:
                record[s[i]] = i
            else:
                if repeatedIdx == i - 1:
                    if cost[i] <= cost[repeatedIdx]:
                        out += cost[i]
                        cost[i] = cost[repeatedIdx]
                    else:
                        out += cost[repeatedIdx]
                record[s[i]] = i
        return out