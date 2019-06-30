import random

list_to_search = [i for i in range(1, 101)]
item_to_find = random.randint(1, 101)
print('This is a test to see how many guesses it takes to find a random number between 1 and 100 using iterative binary search')
print(f'Random number generated: {item_to_find}')


def iterative_binary_search(data, value):
    low = 0
    high = len(data) - 1
    guessCounter = 0

    while low <= high:
        mid = (low + high) // 2
        if value == data[mid]:
            guessCounter += 1
            print(f'Match found in {guessCounter} guess using iterative binary search')
            return True
        elif value < data[mid]:
            high = mid - 1
            guessCounter += 1
        else:
            low = mid + 1
            guessCounter += 1
    return False


iterative_binary_search(list_to_search, item_to_find)
