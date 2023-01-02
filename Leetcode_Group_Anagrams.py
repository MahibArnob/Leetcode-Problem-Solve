class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a-z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)
        
        return result.values()
    
    
### Second Way ###

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            
            if sortedWord not in dict:
                dict[sortedWord] = [word]
            
            else:
                dict[sortedWord].append(word)
            
        result = []
        for item in dict.values():
            result.append(item)
        
        return result
