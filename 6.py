from collections import defaultdict

def parse_txt(filename: str) -> list[str]:
    input_list = []
    with open(filename) as file:
        for line in file:
            input_list.append(line.rstrip('\n'))
    return input_list

input_list = parse_txt('input5.txt')

def process_list(arr):
    for i in arr:
        if i == '':
            arr=[arr[:arr.index(i)]]+[arr[arr.index(i)+1:]]
    for i in range(len(arr[0])):
        arr[0][i] = arr[0][i].split('|')
    for j in range(len(arr[1])):
        arr[1][j] = arr[1][j].split(',')
    return arr

input_list = process_list(input_list)

input_dict = defaultdict(list)

for first,second in input_list[0]:
    input_dict[first].append(second)
    
def is_valid_update(update, dict):
    for i in range(len(update)):
        current_page = update[i]
        pages_before = update[:i]
        
        for page in pages_before:
            if page in dict[current_page]:
                return False
    return True

def part_one(arr, dict):
    summation = 0
    no_of_reports = len(arr[1])
    for i in range(no_of_reports):
        if (is_valid_update(arr[1][i], dict)):
            current_update = arr[1][i]
            middle_index = len(current_update) // 2
            summation += int(current_update[middle_index])
    return summation

print(part_one(input_list, input_dict))