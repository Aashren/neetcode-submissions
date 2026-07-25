class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join([char for char in s if char.isalnum()])
        text=cleaned_text.upper()
        reversed_text = text[::-1]
        if reversed_text == text:
            return True
        else:
            return False 