# Selection sort complexity O(nlogn)
# Comparison at most nlogn
# Array accesses 6nlogn
# Best case complexity is O(nlogn) but can
# be made O(n) by checking before merge whether
# last element of first array is lower then
# First element of second array
# This case optimization is being done
# to avoid array creation at each merge
# start with two array and keep sorting
# other and merging in other one
# this module is part of sort_n_search package


def merge(arr, aux, start, mid, end):
    j, k = start, mid+1
    for i in range(start, end+1):
        if j > mid:
            arr[i] = aux[k]
            k += 1
        elif k > end:
            arr[i] = aux[j]
            j += 1
        elif aux[j] < aux[k]:
            arr[i] = aux[j]
            j += 1
        else:
            arr[i] = aux[k]
            k += 1


def merge_sort(items, aux, start, end):
    if end > start:
        mid = start + (end - start)//2
        merge_sort(aux, items, start, mid)
        merge_sort(aux, items, mid+1, end)
        merge(items, aux, start, mid, end)


def sort(items):
    if items:
        aux = items[:]
        merge_sort(items, aux, 0, len(items)-1)
    return items
