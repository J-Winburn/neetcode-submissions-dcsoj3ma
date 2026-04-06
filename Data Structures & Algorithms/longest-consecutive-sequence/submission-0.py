class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet: #check if begining of sequence
                length = 0 #initilize a lenght counter
                while (num + length) in numSet: # while the current number is in the set
                    length += 1
                longest = max(length, longest) #return max value we found
        return longest
    