class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        mergedNums1AndNums2 = self.mergeTwoSortedArrays(nums1, nums2)
        
        if (m+n)%2 == 0:
            return (mergedNums1AndNums2[int((m+n)/2)-1] + mergedNums1AndNums2[int((m+n)/2)])/2
        else:
            return mergedNums1AndNums2[int((m+n)/2)]
        
        
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         print(nums1)
#         print(nums2)
#         print()
        
#         m = len(nums1)
#         n = len(nums2)
#         halfM = int(m/2)
#         halfN = int(n/2)
        
#         if m == 0:
#             if n%2 == 0:
#                 return (nums2[halfN-1]+nums2[halfN])/2
#             else:
#                 return nums2[halfN]
#         elif n == 0:
#             if m%2 == 0:
#                 return (nums1[halfM-1]+nums1[halfM])/2
#             else:
#                 return nums1[halfM]
#         elif m <= 2 and n <= 2:
#             mergedMid = self.mergeTwoSortedArrays(nums1, nums2)
            
#             halfMN = int((m+n)/2)
#             if (m+n)%2 == 0:
#                 return (mergedMid[halfMN-1]+mergedMid[halfMN])/2 
#             else:
#                 return mergedMid[halfMN]
#         else:
#             if m%2 == 0 and n%2 == 0:
#                 if nums1[halfM-1] <= nums2[halfN-1]:
#                     if nums1[halfM] <= nums2[halfN-1]:
#                         return self.findMedianSortedArrays(nums1[halfM:m], nums2[0:halfN])
#                     else:
#                         if nums1[halfM] <= nums2[halfN]:
#                             return (nums2[halfN-1]+nums1[halfM])/2
#                         else:
#                             return (nums2[halfN-1]+nums2[halfN])/2
#                 else:
#                     if nums2[halfN] <= nums1[halfM-1]:
#                         return findMedianSortedArrays(nums1[0:halfM], nums2[halfN:n])
#                     else:
#                         if nums2[halfN] <= nums1[halfM]:
#                             return (nums1[halfM-1]+nums2[halfN])/2
#                         else:
#                             return (nums1[halfM-1]+nums1[halfM])/2
#             elif m%2 == 0:
#                 if nums1[halfM-1] <= nums2[halfN]:
#                     if nums1[halfM] < nums2[halfN]:
#                         return self.findMedianSortedArrays(nums1[halfM:m], nums2[0:halfN])
#                     else:
#                         return nums2[halfN]
#                 else:
#                     return self.findMedianSortedArrays(nums1[0:HalfM-1], nums2[halfN:n])
#             elif n%2 == 0:
#                 if nums2[halfN-1] <= nums1[halfM]:
#                     if nums2[halfN] < nums1[halfM]:
#                         return self.findMedianSortedArrays(nums1[0:halfM], nums2[halfN:n])
#                     else:
#                         return nums1[halfM]
#                 else:
#                     return self.findMedianSortedArrays(nums1[halfM:m], nums2[0:halfN-1])
#             else:
#                 if nums1[halfM] == nums2[halfN]:
#                     return (nums1[halfM]+nums2[halfN])/2
#                 elif nums1[halfM] < nums2[halfN]:
#                     return self.findMedianSortedArrays(nums1[halfM:m], nums2[0:halfN+1])
#                 else:
#                     return self.findMedianSortedArrays(nums1[0:halfM+1], nums2[halfN,n])
                    
    
    def mergeTwoSortedArrays(self, nums1, nums2):
        result = []
        
        m = len(nums1)
        n = len(nums2)
        
        itr1 = 0
        itr2 = 0
        while itr1 != m or itr2 != n:
            if itr1 == m:
                result += nums2[itr2:n]
                break
            elif itr2 == n:
                result += nums1[itr1:m]
                break
                
            if nums1[itr1] <= nums2[itr2]:
                result.append(nums1[itr1])
                itr1 += 1
            elif nums2[itr2] < nums1[itr1]:
                result.append(nums2[itr2])
                itr2 += 1
        
        return result