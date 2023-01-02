class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Create an empty dictionary
        counts = {}
        # Iterate over the list of words
        for word in words:
            # If the word is not a key in the dictionary yet, add it
            # and set its value to 1
            if word not in counts:
                counts[word] = 1
            # If the word is already a key in the dictionary, 
            # increment its value by 1
            else:
                counts[word] += 1

        # Create a list of tuples, where each tuple is a 
        # key-value pair in the dictionary
        items = list(counts.items())

        # Sort the list of tuples by the values (i.e., the 
        # frequencies of the keys) in descending order
        items.sort(key=lambda x: x[1], reverse=True)

        # Create a list of the k most frequent elements
        k_most_frequent = [item[0] for item in items[:k]]

        return k_most_frequent
