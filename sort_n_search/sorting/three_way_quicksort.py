# Probablistic guarantee of O(nlog(n)) 
# Best case complexity is O(nlogn) but can
# Quick sort 3-way for cases when lots of
# duplicate keys are present
# space complexity log(n) for recursion


def three_way_quick_sort(items, start, end):
    if end > start:
        i = lt = start
        gt = end
        while i <= gt:
            if items[i] == items[lt]:
                i += 1
            elif items[i] < items[lt]:
                items[lt], items[i] = items[i], items[lt]
                i += 1
                lt += 1
            else:
                items[gt], items[i] = items[i], items[gt]
                gt -= 1
        
        three_way_quick_sort(items, start, lt-1)
        three_way_quick_sort(items, gt+1, end)


def sort(items):
    # Do Random shuffle here to avoid worst case scenario
    if items:
        three_way_quick_sort(items, 0, len(items)-1)
    return items
