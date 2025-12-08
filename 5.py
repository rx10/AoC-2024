def parse_txt(filename: str) -> list[str]:
    reports_list = []
    with open(filename) as file:
        for line in file:
            reports_list.append(line.rstrip('\n'))
    return reports_list

reports_list = parse_txt("input4.txt")

data = parse_txt("input4.txt")

# def xmas_check(arr: list[str]) -> int:
#     if len(arr) <= 1:
#         return 0
#     count = 0
#     for i in range(len(arr)):
#         if (i+3 < (len(arr)) and arr[i] == "X" and arr[i+1] == "M" and arr[i+2] == "A" and arr[i+3] == "S"):
#             count += 1
#     return count

# def vertical_traversal(arr):
#     result = []
#     if len(arr) == 0:
#         return
#     m = len(arr)
#     n = len(arr[0])
#     for i in range(n):
#         row = []
#         for j in range(m):
#             row.append(arr[j][i])
#         result.append(row)
#     return result
    
# def horizontal_traversal(arr):
#     if len(arr) == 0:
#         return
#     m = len(arr)
#     n = len(arr[0])
#     result = []
#     for i in range(m):
#         column = []
#         for j in range(n):
#             column.append(arr[i][j])
#         result.append(column)
#     return result

def diagonal_traversal(grid: list[str]) -> list[str]:
    if (len(grid) == 0 or len(grid[0]) == 0):
        return []
    rows = len(grid)
    cols = len(grid[0])
    diagonals = []
    for k in range(-(rows - 1), cols):
        diag = []
        for r in range(rows):
            c = r + k
            if 0 <= c < cols:
                diag.append(grid[r][c])
        diagonals.append(diag)
    for k in range(rows + cols - 1):
        diag = []
        for r in range(rows):
            c = k - r
            if 0 <= c < cols:
                diag.append(grid[r][c])
        diagonals.append(diag)
    return diagonals

# vertical_elements = vertical_traversal(data)
# horizontal_elements = horizontal_traversal(data)
# diagonal_elements = diagonal_traversal(data)
# flip_vertical = [x[::-1] for x in vertical_elements]
# flip_horizontal = [x[::-1] for x in horizontal_elements]
# flip_diagonal = [x[::-1] for x in diagonal_elements]
# vertical_count = sum([xmas_check(item) for item in vertical_elements])
# vertical_count1 = sum([xmas_check(item) for item in flip_vertical])
# horizontal_count = sum([xmas_check(item) for item in horizontal_elements])
# horizontal_count1 = sum([xmas_check(item) for item in flip_horizontal])
# diagonal_count1 = sum([xmas_check(item) for item in diagonal_elements])
# diagonal_count2 = sum([xmas_check(item) for item in flip_diagonal])

# sum = vertical_count + horizontal_count + vertical_count1 + horizontal_count1 + diagonal_count1 + diagonal_count2
# print(sum)

#part 2
def part_two_indexes(data):
    #horizontal coordinates
    h_coords = []
    #vertical coordinates
    v_coords = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "A":
                h_coords.append(i)
                v_coords.append(j)
    return zip(h_coords,v_coords)

def probable_grids(data, coords):
    grids = []
    rows = len(data)
    cols = len(data[0])
    for i,j in coords:
        if 1 < rows - 1 and 1 <= j < cols - 1:
            subgrid = [row[j-1:j+2] for row in data[i-1:i+2]]
            grids.append(subgrid)
    return grids

coords = part_two_indexes(data)
grids = probable_grids(data, coords)

#modified xmas_check function
def mas_check(arr: list[str]) -> int:
    n = len(arr)
    check_vals = [["M", "A", "S"], ["S", "A", "M"]]
    if n <= 1:
        return 0
    diag1 = [arr[i][i] for i in range(n)]
    diag2 = [arr[i][n - 1 - i] for i in range(n)]

    if diag1 in check_vals and diag2 in check_vals:
        return 1
    else:
        return 0

#final statement
count = sum([mas_check(grid) for grid in grids])
print(count)