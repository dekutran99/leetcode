class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort box types in descending order by number of units per box
        sortedBoxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        maxUnits = 0
        curTruckSize = truckSize
        for boxType in sortedBoxTypes:
            if curTruckSize == 0:
                break
            
            numberOfBoxes = boxType[0]
            numberOfUnitsPerBox = boxType[1]
            if numberOfBoxes <= curTruckSize:
                maxUnits += numberOfBoxes*numberOfUnitsPerBox
                curTruckSize -= numberOfBoxes
            else:
                maxUnits += curTruckSize*numberOfUnitsPerBox
                curTruckSize = 0
        
        return maxUnits