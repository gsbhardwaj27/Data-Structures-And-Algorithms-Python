# Selection sort complexity O(nlogn)
# Comparison at most nlogn
# Array accesses 6nlogn
# Best case complexity is O(nlogn) but can
# be made O(n) by checking before merge whether
# last element of first array is lower then
# First element of second array
# this module is part of sort_n_search package


def merge(arr, start, mid, end):
    aux = arr[start: end+1]
    j, k = 0, mid+1-start
    for i in range(start, end+1):
        if j > mid-start:
            arr[i] = aux[k]
            k += 1
        elif k > end-start:
            arr[i] = aux[j]
            j += 1
        elif aux[j] < aux[k]:
            arr[i] = aux[j]
            j += 1
        else:
            arr[i] = aux[k]
            k += 1


def merge_sort(items, start, end):
    if end > start:
        mid = start + (end - start)//2
        merge_sort(items, start, mid)
        merge_sort(items, mid+1, end)
        merge(items, start, mid, end)


def sort(items):
    if items:
        merge_sort(items, 0, len(items)-1)
    return items
