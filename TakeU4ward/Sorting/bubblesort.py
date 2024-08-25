def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        did_swap = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True

        if not did_swap:
            break

    print("After bubble sort: ")
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort: ")
    print(" ".join(map(str, arr)))
    bubble_sort(arr)

