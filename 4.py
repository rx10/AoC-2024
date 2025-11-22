def parse_txt(filename: str) -> str:
    with open(filename) as file:
        file_content = file.read()
    return file_content

data = parse_txt("input3.txt")

first_filtered_list = []
def first_filter(lst):
    for i in range(len(data)):
        if (i+3 < len(data) and data[i] == "m" and data[i+1] == "u" and data[i+2] == "l" and data[i+3] == "("):
            lst.append(data[i:i+14])

first_filter(first_filtered_list)

second_filtered_list = []

elements_we_want = ["m","u","l","0","1","2","3","4","5","6","7","8","9","(",",",")"]

def second_filter(second_filtered_list):
    for i in first_filtered_list:
        if "," not in i:
            continue
        skip_outer = False
        for char in i:
            if char == " " or (char not in elements_we_want):
                skip_outer = True
                break
            if char == ")":
                i = i[0:i.index(char)+1]
                second_filtered_list.append(i)
                break
        if skip_outer:
            continue

def mul(a,b):
    return (int(a)*int(b))

second_filter(second_filtered_list)

def execute_text(lst):
    ns = {"sum": 0, "mul": mul}
    for expr in lst:
        # expr should be something like 'mul(3,4)', 'mul(5,2)', etc.
        exec("sum += " + expr, {}, ns)
    print(ns["sum"])

execute_text(second_filtered_list)