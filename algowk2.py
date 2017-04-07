
def mergesort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    halfway_index = len(unsorted_list)//2
    # mergesort(unsorted_list[0:halfway_index])
    # mergesort(unsorted_list[halfway_index:-1])

    # cursors. idk.
    #put stuff in order, like MAAGIC


def guts(a, b): #takes two sorted lists
    output = []
    cursor_a = 0
    cursor_b = 0
    for i in range(len(a) + len(b)):
        if cursor_a >= len(a):
            output.append(b[cursor_b])
            cursor_b += 1
        elif cursor_b >= len(b):
            output.append(a[cursor_a])
            cursor_a += 1
        elif a[cursor_a] < b[cursor_b]:
            output.append(a[cursor_a])
            cursor_a += 1
        else:
            output.append(b[cursor_b])
            cursor_b += 1

    return output


def binarysearch(sorted_list, target):

    if sorted_list == []:
        return False

    halfway_index = len(sorted_list)//2

    if target == sorted_list[halfway_index]:
        return halfway_index
    elif target < sorted_list[halfway_index]:
        binarysearch(sorted_list[0:halfway_index], target)
    elif target > sorted_list[halfway_index]:
        binarysearch(sorted_list[halfway_index:-1], target)
