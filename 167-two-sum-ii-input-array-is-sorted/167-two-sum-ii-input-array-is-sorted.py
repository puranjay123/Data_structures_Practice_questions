class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr =[]
        low,high=0,len(numbers)-1
        
        while low<high:
            s=numbers[low]+numbers[high]
            if s==target:
                
                return [low+1,high+1]
            elif s<target:
                low=low+1
            else:
                high=high-1
        
        