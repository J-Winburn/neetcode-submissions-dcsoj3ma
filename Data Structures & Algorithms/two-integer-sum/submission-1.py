class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MyMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in MyMap:
                return [MyMap[diff], i]
            MyMap[n] = i
            

        