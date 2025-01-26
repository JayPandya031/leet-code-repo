lst = [1, 3, 2, 6, 5, 4, 7, 3]

largest = second_largest = None

for num in lst:

    if largest is None or num > largest:
        second_largest = largest
        largest = num
    if largest != num and (second_largest is None or num > second_largest):
        second_largest = num
    
print(second_largest)