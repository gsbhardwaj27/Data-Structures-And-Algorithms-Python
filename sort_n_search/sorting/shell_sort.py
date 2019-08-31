# Shell sort complexity O(N3/2)
# Actual complexity is still not known
# We use k-sorting in shell sort
# for shell sort insertion sort is used
# as insertion sort works well will
# partial sorted array
# this module is part of sort_n_search package
# small code and faster then insertion
# so used in many embedded systems
# values of h we will use is h=3*h+1 where
# which gives us 1, 4, 13, 40 ....


def sort(items):
    if items:
        N = len(items)
        h = 1
        while(3*h+1 < N):
            h = 3*h+1

        while(h >= 1):
            for i in range(1, N, h):
                for j in range(i, 0, -h):
                    if items[j] < items[j-h]:
                        items[j], items[j-h] = items[j-h], items[j]
                    else:
                        break
            h //= 3
    return items
