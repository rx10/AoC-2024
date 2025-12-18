from collections import defaultdict
from functools import cmp_to_key

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

incorrect_updates = []

def part_one(arr, dict):
    summation = 0
    no_of_reports = len(arr[1])
    for i in range(no_of_reports):
        if (is_valid_update(arr[1][i], dict)):
            current_update = arr[1][i]
            middle_index = len(current_update) // 2
            summation += int(current_update[middle_index])
        else:
            incorrect_updates.append(arr[1][i])
    return summation

    
print("Part 1:" + f"{part_one(input_list, input_dict)}")

def part_two(incorrect_updates, dict):
    def comp_instructions(page_a, page_b):
        if page_b in dict[page_a]:
            return -1;
        if page_a in dict[page_b]:
            return 1;

    summation = 0;
    for arr in incorrect_updates:
        arr = sorted(arr, key=cmp_to_key(comp_instructions))
        mid = len(arr)//2
        summation+=int(arr[mid])
    return summation;

print("Part 2:" + f"{part_two(incorrect_updates,input_dict)}")