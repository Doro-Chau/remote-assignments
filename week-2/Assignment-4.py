def count(input):
    output_dict = {}
    for i in range(len(input)):
        if input[i] in output_dict.keys():
            output_dict[input[i]] += 1
        else:
            output_dict[input[i]] = 1
    return output_dict
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    output_dict = {}
    for i in range(len(input)):
        if input[i]['key'] in output_dict.keys():
            output_dict[input[i]['key']] += input[i]['value']
        else:
            output_dict[input[i]['key']] = input[i]['value']
    return output_dict
 # your code here
input2 = [
 {'key': 'a', 'value': 3},
 {'key': 'b', 'value': 1},
 {'key': 'c', 'value': 2},
 {'key': 'a', 'value': 3},
 {'key': 'c', 'value': 5}
]

print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}