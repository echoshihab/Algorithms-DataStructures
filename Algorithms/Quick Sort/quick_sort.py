unordered_list = [5, 7, 3, 1, 9, 2, 4, 8, 6]


# w/ pivot always the first item of the list

def quick_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        pivot = list_to_sort[0]  # picking the first item
        lesser = [num for num in list_to_sort[1:] if num <= pivot]  # partition with lower numbers
        greater = [num for num in list_to_sort[1:] if num > pivot]  # partition with greater numbers
        return quick_sort(lesser) + [pivot] + quick_sort(greater)  # recursive calls on greater and lesser


print(quick_sort(unordered_list))


# pivot being median of three: I found a good explanation here - https://www.youtube.com/watch?v=CB_NCoxzQnk (Author:Joe James)
def get_pivot(list_to_sort, low_index, high_index):
    mid = (high_index + low_index) // 2
    pivot = high_index
    if list_to_sort[low_index] < list_to_sort[mid]:
        if list_to_sort[mid] < list_to_sort[high_index]:
            pivot = mid
    elif list_to_sort[low_index] < list_to_sort[high_index]:
        pivot = low_index
    return pivot


def quick_sort_md3(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        pivot_index = get_pivot(list_to_sort, 0, len(list_to_sort) - 1)
        pivot = list_to_sort.pop(pivot_index)
        lesser = [num for num in list_to_sort if num <= pivot]  # partition with lower numbers
        greater = [num for num in list_to_sort if num > pivot]  # partition with greater numbers
        return quick_sort_md3(lesser) + [pivot] + quick_sort_md3(greater)


unordered_list2 = [5, 7, 3, 1, 9, 2, 4, 8, 6]

print(quick_sort_md3(unordered_list2))
