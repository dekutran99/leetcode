class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of numbers and indices that we have traversed
        record = {}
        
        for i in range(len(nums)):
            # the number we want to look up in our record
            complement = target - nums[i]
            
            if record.get(complement) is None:
                record[nums[i]] = i
            else:
                return [record[complement], i]
        
        # empty if no match
        return []