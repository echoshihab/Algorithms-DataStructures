unsorted_list = [3, 2, 1, 4, 5, 7, 9, 10, 6, 8]


def bubble_sort(list_to_sort):
    for index in range(0, len(list_to_sort) - 1):
        for index2 in range(0, len(list_to_sort) - index - 1):
            if list_to_sort[index2] > list_to_sort[index2 + 1]:
                list_to_sort[index2], list_to_sort[index2 + 1] = list_to_sort[index2 + 1], list_to_sort[index2]
    return list_to_sort


print(bubble_sort(unsorted_list))
