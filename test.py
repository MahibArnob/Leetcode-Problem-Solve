def dailyTemperatures(temperatures):
        count = 0
        arr = []
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:  # Check if current index is the last element
                arr.append(0)
                continue  # Skip inner loop for the last element
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    arr.append(count)
                    count = 0  # Reset count after finding a warmer day
                    break
                else:
                    count += 1
            if count > 0:  # Append 0 if no warmer day found for the current day
                arr.append(count)
                count = 0  # Reset count after the inner loop
        return arr


temperatures = [55,38,53,81,61,93,97,32,43,78]
print(dailyTemperatures(temperatures))