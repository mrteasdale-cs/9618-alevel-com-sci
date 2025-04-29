def read_employees(fn):
    employees = []
    with open(fn, "r") as file:
        for line in file:
            name, dept, salary = line.strip().split(',')
            print(f"Name: {name} / Dept: {dept} / Salary: {salary}")
            employees.append([name, dept, salary])
    return employees

def calculate_average(employees):
    total = 0.0 # float/real
    avg = 0.0 # float/real
    count = 0 #integer
    for emp in employees:
        total += float(emp[2])
        count += 1
    avg = total / count

    return f"Average salary for {count} employees = ${avg:.2f}"

def bubble_sort_by_salary(employees):
    for i in range(len(employees)):
        for j in range(len(employees) - 1):
            if employees[j][2] < employees[j + 1][2]:
                temp = employees[j]
                employees[j] = employees[j + 1]
                employees[j + 1] = temp

def search_employee(employees, name):
    bubble_sort_by_salary(employees)
    min = 0
    max = len(employees) - 1
    while min <= max:
        mid = (min + max) // 2
        print (employees[mid])
        if employees[mid][0] == name:
            return f"Found: {employees[mid][0]}"
        elif employees[mid][0] < name:
            min = mid + 1
        else:
            max = mid - 1
    return f"{name} not found"

filename = "../../P4 9618 MJ 23 42/employees.txt"
emps = read_employees(filename)
print(calculate_average(emps))
print(search_employee(emps, "Diana Miller"))