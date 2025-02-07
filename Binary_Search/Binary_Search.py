def Binary_Search(My_list, find):

    low = 0
    high = len(My_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        data = My_list[mid]
        if data == find:
            return mid
        elif data > find:
            high = mid - 1
        else:   # data < find 
            low = mid + 1 
    return None

my_list = [0,3,6,9,12,15,18,21,24,27,30]

print(Binary_Search(my_list, 18))

