class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join([char for char in s if char.isalnum()])
        reversed_text = cleaned_text[::-1]
        if reversed_text.upper() == cleaned_text.upper():
            return True
        else:
            return False 