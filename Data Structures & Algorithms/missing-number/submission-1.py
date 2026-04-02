class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numHash = set(nums)
        for num in range(len(nums)+1):
            if num not in numHash:
                return num
        

        
        