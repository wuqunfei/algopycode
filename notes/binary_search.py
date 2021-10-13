def bs(array: list, target: int):
    length = len(sorted(list))
    # order array list
    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            # find the target break or return the value
            return
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
