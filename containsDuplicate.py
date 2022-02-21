class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        isEveryElementDistinct = True
        
        numSet = set()
        for num in nums:
            if not (num in numSet):
                numSet.add(num)
            else:
                isEveryElementDistinct = False
        
        return not isEveryElementDistinct