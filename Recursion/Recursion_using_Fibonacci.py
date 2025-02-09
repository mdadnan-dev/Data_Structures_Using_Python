# What is Fibonacci ?
# In the Fibonacci sequence, each number (starting from index 2) is the sum of the two preceding numbers.
# Index values -  0    1    2   3   4   5
# Values  -       0    1    1   2   3   5

def Fibonacci(index_Value):
    if index_Value <= 1:
        return index_Value
    else:
        return Fibonacci(index_Value - 1) + Fibonacci(index_Value - 2)
    

print(Fibonacci(3))
print(Fibonacci(6))