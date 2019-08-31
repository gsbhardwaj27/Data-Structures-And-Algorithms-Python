# Selection sort complexity O(N2) 
# Number of comparisons made are ~(N2)/2
# in all the cases even when input array
# is sorted
# Both best and worst case complexity
# are same
# Selection sort is inplace sort
# this module is part of sort_n_search package

def sort(items):
    if items:
        N = len(items)
        for i in range(N):
            mn = i
            for j in range(i+1, N):
                if items[j] < items[mn]:
                    mn = j
            items[i], items[mn] = items[mn], items[i]
    return items
