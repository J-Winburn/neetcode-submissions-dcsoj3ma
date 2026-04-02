class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = {} #map each char to its index
        l = 0 # init left index to 0
        max_len = 0 # initilize max length to 0

        for right in range(len(s)):  # for every char in the string we use a right pointer
            char = s[right] # each char can be accesed using index
            if s[right] in count: # aka if we have already seen the char 
                l = max(count[char] + 1, l) # move the left pointer to the next index
            count[char] = right # update the index of that character 
            max_len = max(max_len, right - l + 1) # max length result 
        return max_len

            

                      
    
