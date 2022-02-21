class Solution:
    '''with converting to string'''
    # def isPalindrome(self, x: int) -> bool:
    #     strInt = str(x)
        
    #     i = 0
    #     j = len(strInt) - 1
    #     while not (i > j):
    #         if strInt[i] != strInt[j]:
    #             return False
            
    #         i += 1
    #         j -= 1
            
    #     return True
    
    
    '''without converting to string'''
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reversedX = 0
        while temp > 0:
            digit = temp % 10
            reversedX = reversedX*10 + digit
            temp = int(temp/10)
        
        return reversedX == x
        
