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

number_freq = {}
for i in sorted1:
    number_freq[i] = sorted2.count(i)

new_freq = number_freq.copy()
for key, value in number_freq.items():
    if value == 0:
        new_freq.pop(key)

sum = 0
for key, value in new_freq.items():
    sum+= key*value
print(sum)