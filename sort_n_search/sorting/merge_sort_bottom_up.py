
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


def sort(items):
    if items:
        N = len(items)
        size = 1
        while size < N:
            for i in range(0, N, 2*size):
                merge(items, i, i+size-1, min(i+2*size-1, N-1))
            size = 2*size
    return items

