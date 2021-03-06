class Solution:
	# # brute force
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     record = {}
    #     lenOfSubStrWithoutRepeat = 0
    #     lenOfLongestSubStr = 0
        
    #     i = 0
    #     while i < len(s):
    #         repeatIdx = record.get(s[i])
    #         if repeatIdx == None:
    #             record[s[i]] = i
    #             lenOfSubStrWithoutRepeat += 1
    #             lenOfLongestSubStr = max(lenOfLongestSubStr, lenOfSubStrWithoutRepeat)
    #             i += 1
    #         else:
    #             lenOfSubStrWithoutRepeat = 0
    #             record.clear()
    #             i = repeatIdx + 1
        
    #     return lenOfLongestSubStr
              
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        curLenOfSubStrWithoutRepeat = 0
        lenOfLongestSubStrWihtoutRepeat = 0
        anchor = 0
        for i in range(len(s)):
            repeatedIdx = record.get(s[i])
            if repeatedIdx == None:
                record[s[i]]= i
            elif repeatedIdx < anchor:
                record[s[i]] = i
            else:
                anchor = repeatedIdx + 1
                record[s[i]] = i
            curLenOfSubStrWithoutRepeat = i - anchor + 1
            lenOfLongestSubStrWihtoutRepeat = max(lenOfLongestSubStrWihtoutRepeat, curLenOfSubStrWithoutRepeat)
        
        return lenOfLongestSubStrWihtoutRepeat