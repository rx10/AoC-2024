numbers_list = []

with open("input2.txt") as file:
    for line in file:
        numbers = list(map(int, line.split()))  # Convert each line to a list of ints
        numbers_list.append(numbers)

sum = 0
cleaned_list = []
for a in numbers_list:
    if (all(x<y for x, y in zip(a, a[1:])) or all(x>y for x, y in zip(a, a[1:]))):
        cleaned_list.append(a)

for z in cleaned_list:
    diffs = [abs(z[i+1] - z[i]) for i in range(len(z) - 1)]
    exception_count = 0
    for y in diffs:
        if y >= 1 and y <= 3:
            continue
        else:
            if exception_count == 0:
                exception_count += 1
            else:
                break
    else:  # This else corresponds to the for-loop, runs if no break
        sum += 1
print(sum)