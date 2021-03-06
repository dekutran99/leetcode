class Solution:
    def mySqrt(self, x):
        out = 0
        low = 0
        high = x
        mid = int((low + high) / 2)
        while not low == high:
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                out = mid
                low = mid + 1
                if low ** 2 > x:
                    break
            else:
                high = mid - 1
            
            if low == high:
                out = low
            else:
                mid = int((low + high) / 2)
            
        return out
