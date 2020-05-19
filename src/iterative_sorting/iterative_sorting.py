# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
       smallest_index = i
       for j in range(i, len(arr)):
           if arr[smallest_index] > arr[j]:
            smallest_index = j


        # TO-DO: swap
       arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(1, len(arr)):
        curr_pos = arr[i]
        j = i
        while j > 0 and curr_pos < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    

    return arr


# STRETCH: implement the Count Sort function below
#def count_sort(arr, maximum=-1):
    # Your code here


 #   return arr
