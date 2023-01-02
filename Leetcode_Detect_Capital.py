# Check if word is either all uppercase or all lowercase or titlecase. Then return True otherwise False
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower or word.istitle()
   
