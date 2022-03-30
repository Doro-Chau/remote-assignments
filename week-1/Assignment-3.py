def find_max(numbers):
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max

print(find_max([1, 2, 4, 5]) )
print(find_max([5, 2, 7, 1, 6]) )

def find_position(numbers,target):
    position = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            position = i
            break
    return position

print(find_position([5, 2, 7, 1, 6], 5))
print(find_position([5, 2, 7, 1, 6], 7))
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8)) 