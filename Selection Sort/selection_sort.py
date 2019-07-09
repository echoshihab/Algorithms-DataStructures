
unordered_list = [5, 9, 4, 10, 23, 1, 3, 2, 7]


# 1. selection sort function that modifies the original list

# modify the original list
def selection_sort_modify(list_to_sort):
    for index in range(len(list_to_sort)):
        lowest_num_index = index  # index of the initial number
        for index2 in range(index + 1, len(list_to_sort)):  # inner loop to check for index of a lower number
            if list_to_sort[index2] < list_to_sort[lowest_num_index]:
                lowest_num_index = index2
        list_to_sort[index], list_to_sort[lowest_num_index] = list_to_sort[lowest_num_index], list_to_sort[index]  # swap
    print(list_to_sort)


# 2. selection sort function that returns a new list without modifying the first one
selection_sort_modify(unordered_list)

# create a new sorted list (2 functions)

# first function to find a the smallest value
def find_lowest(list_to_sort):
    lowest_num = list_to_sort[0]
    lowest_index = 0
    for index in range(1, len(list_to_sort)):
        if list_to_sort[index] < lowest_num:
            lowest_num = list_to_sort[index]
            lowest_index = index
    return lowest_index

# second function to output a new list
def selection_sort_create_new(list_to_sort):
    ordered_list = []
    for index in range(len(list_to_sort)):
        lowest_num = find_lowest(list_to_sort)
        num_to_move = list_to_sort.pop(lowest_num)  # pop out the low number
        ordered_list.append(num_to_move)  # adds it to the end of the list
    print(ordered_list)


unordered_list2 = [5, 9, 4, 10, 23, 1, 3, 2, 7]
selection_sort_create_new(unordered_list2)
