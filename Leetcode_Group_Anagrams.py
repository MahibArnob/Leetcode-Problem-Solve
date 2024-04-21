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


### 3rd Way ###

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            sortedMap.setdefault(sortedWord, []).append(word)
        return list(sortedMap.values())


### 4th Way ###

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            sortedMap[sortedWord].append(word)
        return list(sortedMap.values())

# The last 3 ways are the same. If we use defaultdict(list) we can explicitly check if the key exists in the dictionary and create it if it doesn't.
# On the other hand, setdefault(sortedWord, []) checks if the key is already in the dict, if yes then append the value else create a new key and value pair with sortedWord and empty list.
