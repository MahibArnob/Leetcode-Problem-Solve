class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsdict = {}
        for word in words:
            if word not in wordsdict.keys():
                wordsdict[word] = 1
            else:
                wordsdict[word] += 1
        
        wordsdictsort = dict(sorted(wordsdict.items(), key=lambda item: item[1], reverse=True))

        lexico = {}
        for key, value in wordsdictsort.items():
            if value not in lexico.keys():
                lexico[value] = [key]
            else:
                lexico[value].append(key)
                lexico[value].sort()

        ans = []
        for value in lexico.values():
            ans.extend(value)

        return ans[:k]
