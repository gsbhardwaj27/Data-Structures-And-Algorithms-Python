# Insertion sort complexity O(N2)
# Number of comparisons made are ~(N2)/4
# best case when input array
# is sorted its O(n)
# Selection sort is inplace sort
# this module is part of sort_n_search package


def sort(items):
    if items:
        N = len(items)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if items[j-1] > items[j]:
                    items[j], items[j-1] = items[j-1], items[j]
                else:
                    break
    return items
