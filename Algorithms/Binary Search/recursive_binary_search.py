import random

list_to_search = [i for i in range(1, 101)]
item_to_find = random.randint(1, 101)
print('This is a test to see how many guesses it takes to find a random number between 1 and 100 using iterative binary search')
print(f'Random number generated: {item_to_find}')


def recursive_binary_search(data, value, low, high, guessCounter=0):
    if low > high:
        print('Item is not in the list')
    else:
        mid = (low + high) // 2
        if value == data[mid]:
            guessCounter += 1
            print(f'Match found in {guessCounter} guess using recursive binary search')
            return True
        elif value < data[mid]:
            guessCounter += 1
            return recursive_binary_search(data, value, low, mid - 1, guessCounter)
        else:
            guessCounter += 1
            return recursive_binary_search(data, value, mid + 1, high, guessCounter)
    return False


def linear_search(data, value):
    guessCounter = 0
    for item in data:
        guessCounter += 1
        if item == value:
            print(f'Match found in {guessCounter} guess using linear search')


linear_search(list_to_search, item_to_find)
recursive_binary_search(list_to_search, item_to_find, 0, len(list_to_search) - 1)
