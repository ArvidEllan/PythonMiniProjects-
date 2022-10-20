def bubbleSort(numbers):
    # The outer loop loops i over all but the last number:
    for i in range(len(numbers) - 1):
        # The inner loop loops j starting at i to the last number:
        for j in range(i, len(numbers)):
            # If the number at i is greater than the number at j, swap them:
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    # Return the now-sorted list:
    return numbers

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]


import random
x = [random.randint(1, 10000) for x in range(100)]  
assert bubbleSort(x) == sorted(x)