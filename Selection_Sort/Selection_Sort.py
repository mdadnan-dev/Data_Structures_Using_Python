def Finding_Min(My_List):
    smallest = My_List[0]
    smallest_index = 0

    for i in range(1, len(My_List)):
        if My_List[i] < smallest:
            smallest = My_List[i]
            smallest_index = i
    return smallest_index 

Final_List = [43, 44, 11, 14, 3, 13]

print("The Index of Minimum Value is ", Finding_Min(Final_List))


def Selection_Sort(My_List):
    New_List = []
    Original_List = list(My_List)
    
    for i in range(1, len(Original_List)):
        smallest = Finding_Min(Original_List)
        New_List.append(Original_List.pop(smallest))
    return New_List

Final_List = [43, 44, 11, 14, 3, 13]

print(Selection_Sort(Final_List))