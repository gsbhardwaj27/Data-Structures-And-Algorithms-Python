# Selection sort complexity O(nlogn)
# Comparison at most nlogn
# Best case complexity is O(nlogn) but can
# worst case O(n2) when array is sorted
# Quick sort
# space complexity log(n) for recursion


def quick_sort(items, start, end):
    if end > start:
        i = start+1
        j = end
        while True:
            while items[i] <= items[start]:
                i += 1
                if i > end:
                    break
            while items[j] > items[start]:
                j -= 1
            if i < j:
                items[i], items[j] = items[j], items[i]
            else:
                break
        items[start], items[j] = items[j], items[start]
        quick_sort(items, start, j-1)
        quick_sort(items, j+1, end)


def sort(items):
    # Do Random shuffle here to avoid worst case scenario
    if items:
        quick_sort(items, 0, len(items)-1)
    return items
