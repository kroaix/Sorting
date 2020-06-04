# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code) 
        # loop through the right of the current index         
        for j in range(i + 1, len(arr)):
            # if array at the index of j is smaller we update smallest_index to that number
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # we figured out the smallest index, so now we must swap smallest index with current index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through arr and compare each item to the next
    # if the next item is smaller than the current, swap
    # if a swap was made we need to go back and iterate again

    # creating a variable to keep track of whether a swap was made
    # defaulting to False
    swap_made = False

    for i in range(0, len(arr) - 1):
        # if number at current index is smaller than the next, swap
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # change the value of swap_made to True since a swap was made
            swap_made = True
    # as mentioned above, if a swap was made we must iterate again
    # because we still need to sort the rest of the array
    if swap_made:
        bubble_sort(arr)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr