class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i , n in enumerate(nums):
            diff = target - n #finding if it's in the hash map
            if diff in map:
                return [map[diff],i]
            map[n] = i
        return 
        
    

