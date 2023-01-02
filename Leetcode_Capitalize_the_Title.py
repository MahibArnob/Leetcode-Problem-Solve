class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = []
        for word in title.split(' '):
            word = word.lower()
            if len(word) > 2:
                word = word[0].upper() + word[1:]
            s.append(word)
        return " ".join(s)
    
## Solution 2, Does the same thing as the previous solution but in one line ###
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([word.capitalize() if len(word)>2 else word for word in title.lower().split(' ')])
