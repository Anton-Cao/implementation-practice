def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break
    return arr

if __name__ == "__main__":
    arr = insertion_sort([1, 8, 2, 3, 6, 3, 2, 9, 5])
    print(arr)
