def parse_txt(filename: str) -> str:
    with open(filename) as file:
        file_content = file.read()
    return file_content

data = parse_txt("input3.txt")

def first_filter(data: list[list[str]]) -> list[str]:
    data_length = len(data)
    output_list = []
    for i in range(data_length):
        #might be faulty logic
        if (i+6 < data_length and data[i] == "d" and data[i+1] == "o" and data[i+2] == "n" and data[i+3] == "'" and data[i+4] == "t" and data[i+5] == "(" and data[i+6] == ")"):
            output_list.append(data[i:i+7])
        if (i+3 < data_length and data[i] == "d" and data[i+1] == "o" and data[i+2] == "(" and data[i+3] == ")"):
            output_list.append(data[i:i+4])
        if (i+3 < data_length and data[i] == "m" and data[i+1] == "u" and data[i+2] == "l" and data[i+3] == "("):
            output_list.append(data[i:i+14])
    return output_list

first_filtered_list = first_filter(data)

elements_we_want = ["m","u","l","0","1","2","3","4","5","6","7","8","9","(",",",")"]

def second_filter(input_list: list[str]) -> list[str]:
    output_list = []
    for i in input_list:
        if i in ["do()","don't()"]:
            output_list.append(i)
            continue
        if "," not in i:
            continue
        skip_outer = False
        for char in i:
            if char == " " or (char not in elements_we_want):
                skip_outer = True
                break
            if char == ")":
                i = i[0:i.index(char)+1]
                output_list.append(i)
                break
        if skip_outer:
            continue
    return output_list

def mul(a: int,b: int) -> int:
    return (int(a)*int(b))

second_filtered_list = second_filter(first_filtered_list)

# def execute_text(lst: list) -> int:
#     ns = {"sum_total": 0, "mul": mul}
#     for expr in lst:
#         # expr should be something like 'mul(3,4)', 'mul(5,2)', etc.
#         exec("sum_total += " + expr, {}, ns)
#     return(ns["sum_total"])

def third_part(lst: list) -> int:
    skip_next = False
    ns = {"sum_total": 0, "mul": mul}
    for expr in lst:
        print(expr)
        if expr == "don't()":
            skip_next = True
            continue
        if skip_next:
            if expr == "do()":
                skip_next = False
                continue
            else:
                continue
        if expr[0] == "m":
            exec("sum_total += " + expr, {}, ns)
    return ns["sum_total"]

#part 2
print(third_part(second_filtered_list))
# def third_filter(input_list: list[int]f) -> list[int]: