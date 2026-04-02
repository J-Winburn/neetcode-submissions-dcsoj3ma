class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        if len(nums) > len(myset):
            return True
        return False
          



        