class Solution:
    def isPalindrome(self, s: str) -> bool:
        sol = ''

        for char in s:
            if char.isalnum():
                sol += char.lower()
        return sol == sol[::-1]