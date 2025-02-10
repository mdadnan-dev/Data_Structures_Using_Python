def quicksort(sequence):
    
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    Greater_values = []
    Lower_values = []

    for item in sequence:
        if item >= pivot:
            Greater_values.append(item)
        else:
            Lower_values.append(item)
    
    return quicksort(Lower_values) + [pivot] + quicksort(Greater_values)


print(quicksort([1,14,2,18,12,14,3,8]))