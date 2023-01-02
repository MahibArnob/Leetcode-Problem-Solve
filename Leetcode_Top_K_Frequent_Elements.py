class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an empty dictionary
        dict = {}

        # Iterate over the list of numbers
        for num in nums:
            # If the number is not a key in the dictionary yet, add it
            # and set its value to 1
            if num not in dict:
                dict[num] = 1
            # If the number is already a key in the dictionary, 
            # increment its   value by 1
            else:
                dict[num] += 1

        # Create a list of tuples, where each tuple is a key-value pair
        # in the dictionary
        items = list(dict.items())

        # Sort the list of tuples by the values (i.e. 
        # the frequencies of the keys) in descending order
        items.sort(key=lambda x: x[1], reverse=True)

        # Create a list of the k most frequent elements
        k_most_frequent = [item[0] for item in items[:k]]

        return k_most_frequent
