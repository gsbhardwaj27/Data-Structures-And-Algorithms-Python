# Heap sort
# No extra space
# O(nlogn) run time compexity

def swim(items, idx):
    while idx != 0 and items[(idx-1)//2] < items[idx]:
        items[idx], items[(idx-1)//2] = items[(idx-1)//2], items[idx]
        idx = (idx-1)//2

def sink(items, idx, last_index):
    while idx*2+1 <= last_index:
        mx_idx = idx*2+1
        if idx*2+2 <= last_index and items[idx*2+2] > items[idx*2+1]:
            mx_idx = idx*2+2
        if items[mx_idx] > items[idx]:
            items[mx_idx], items[idx] = items[idx], items[mx_idx]
            idx = mx_idx
        else:
            break

def heap_sort(items):
    for i in range(len(items)):
        swim(items, i)
    for i in range(len(items)-1, -1, -1):
        items[0], items[i] = items[i], items[0]
        sink(items, 0, i-1)


def sort(items):
    if items:
        heap_sort(items)
    return items
