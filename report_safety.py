def no_of_safe_reports(reports: list[list[int]]) -> int:
    count = 0
    for report in reports_list:
        if report_is_valid(report):
            count+=1
    return count

def unsafe_reports(reports: list[list[int]]) -> list[list[int]]:
    dirty_list = []
    for report in reports_list:
        if not report_is_valid(report):
            dirty_list.append(report)
    return dirty_list

def parse_txt(filename: str) -> list[list[int]]:
    reports_list = []
    with open(filename) as file:
        for line in file:
            numbers = list(map(int, line.split()))
            reports_list.append(numbers)
    return reports_list

def report_is_valid(report: list[int]) -> bool:
    initial_direction = report[0] < report[1]
    for i in range(len(report)-1):
        diff = abs(report[i]-report[i+1])
        if ((report[i] < report[i+1]) != initial_direction) or (diff < 1 or diff > 3):
            return False
    return True

#Part 1
reports_list = parse_txt("input2.txt")
print(no_of_safe_reports(reports_list))

#Part 2
def subreport_check(report: list[int]) -> bool:
    for i in range(len(report)):
        if(report_is_valid(report[0:i]+report[i+1:])):
            return True
    return False

dirty_list = unsafe_reports(reports_list)
remaining_safe_reports = 0

for report in dirty_list:
    if(subreport_check(report)):
        remaining_safe_reports += 1
print(remaining_safe_reports)