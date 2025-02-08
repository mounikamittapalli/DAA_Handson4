import heapq
def mergeK(arr, k):
    res = []
    h = []
    # Inserting the first elements of each row
    for i in range(len(arr)):
        heapq.heappush(h, (arr[i][0], i, 0))
    # array_num stores index of the array from which this element came
    # idx_of_elem_in_array stores the  index of the element in array
    while h:
        value, array_num,idx_of_elem_in_array= heapq.heappop(h)
        res.append(value)
        if idx_of_elem_in_array + 1 < len(arr[array_num]):
            heapq.heappush(h, (arr[array_num][idx_of_elem_in_array + 1], array_num, idx_of_elem_in_array + 1))
    return res

# Driver code
if __name__ == '__main__':
# example1
    array1 = [1,3,5,7]
    array2 = [2,4,6,8]
    array3 = [0,9,10,11]
    arr = [array1, array2, array3]
    k = 3
    l1= mergeK(arr, k)
    print("Merged Array 1:",*l1)

#Example2
    array1 = [1, 3, 7]
    array2 = [2, 4, 8]
    array3 = [9, 10, 11, 23, 4, 7]
    arr = [array1, array2, array3]
    k = 3  # Number of arrays
    l2 = mergeK(arr, k)  # Call mergeK
    print("Merged Array 2:", *l2)  # Print result