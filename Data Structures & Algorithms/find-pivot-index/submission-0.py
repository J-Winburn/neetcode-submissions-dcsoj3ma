class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for index, number in enumerate(nums):
            rightsum = total - nums[index] - leftsum
            if leftsum == rightsum:
                return index
            leftsum += nums[index]
        return -1
            
        



        