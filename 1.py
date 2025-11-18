def QuickSort(l1):
    if len(l1) <= 1:
        return l1
    pivot = l1[-1]
    l = [x for x in l1[:-1] if x < pivot]
    r = [x for x in l1[:-1] if x >= pivot]
    return QuickSort(l) + [pivot] + QuickSort(r)

numbers_list = []
with open("input.txt") as file:
    for line in file:
        numbers = map(int, line.split())
        numbers_list.extend(numbers)

sorted1 = QuickSort(numbers_list[::2])
sorted2 = QuickSort(numbers_list[1::2])

sum = 0
for i in range(1000):
    sum += (abs(sorted1[i]-sorted2[i]))
    print(i)

print(sum)