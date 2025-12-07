def parse_txt(filename: str) -> list[str]:
    reports_list = []
    with open(filename) as file:
        for line in file:
            reports_list.append(line.rstrip('\n'))
    return reports_list

reports_list = parse_txt("input4.txt")

data = parse_txt("input4.txt")

def xmas_check(arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i] == "X" and arr[i+1] == "M" and arr[i+2] == "A" and arr[i+3] == "S"):
            count += 1
    return count

def vertical_traversal(arr):
    result = []
    if len(arr) == 0:
        return
    m = len(arr)
    n = len(arr[0])
    for i in range(n):
        for j in range(m):
            result.append(arr[i][j])
    return result
    
def horizontal_traversal(arr):
    if len(arr) == 0:
        return
    m = len(arr)
    n = len(arr[0])
    result = []
    for i in range(m):
        for j in range(n):
            result.append(arr[i][j])
    return result

def diagonal_traversal(arr):
    m = len(arr)
    n = len(arr[0])
    row, col, direction = 0, 0, 1
    diags = []
    current_diag = []
    while row < m and col < n:
        current_diag.append(arr[row][col])
        new_row = row + (-1 if direction == 1 else 1)
        new_col = col + (1 if direction == 1 else -1)
        # boundary check
        if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
            # finish current diagonal
            diags.append(current_diag)
            current_diag = []
            if direction == 1:
                row += (col == n - 1)
                col += (col < n - 1)
            else:
                col += (row == m - 1)
                row += (row < m - 1)
            direction = 1 - direction
        else:
            row, col = new_row, new_col
    # append the last diagonal
    if current_diag:
        diags.append(current_diag)
    return diags
    
vertical_elements = vertical_traversal(data)
horizontal_elements = horizontal_traversal(data)
diagonal_elements = diagonal_traversal(data)
flip_vertical = [x[::-1] for x in vertical_elements]
flip_horizontal = [x[::-1] for x in horizontal_elements]
flip_diagonal = [x[::-1] if i % 2 == 0 else x for i, x in enumerate(diagonal_elements)]
vertical_count = xmas_check(vertical_elements)
vertical_count1 = xmas_check(flip_vertical)
horizontal_count = xmas_check(horizontal_elements)
horizontal_count1 = xmas_check(flip_horizontal)
diagonal_count1 = xmas_check(diagonal_elements)
diagonal_count2 = xmas_check(flip_diagonal)

sum = vertical_count + horizontal_count + diagonal_count1 + diagonal_count2
print(sum)