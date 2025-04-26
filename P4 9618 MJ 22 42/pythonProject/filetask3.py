# Part 1: Reading from a File
def read_grades(fname):
    grades = []
    with open(fname, "r") as file:
        #print(file.readlines())
        for line in file:
            name, subject, grade = line.strip().split(',')
            grades.append((name, subject, grade))
    return grades

#Part 2: Writing to a File
def write_grades(fname, name, subject, grade):
    with open(fname, "a") as file:
        file.write(f"{name},{subject},{grade}\n")
    file.close()

# Part 3: Calculating Average Grade
def calculate_average(grades):
    total = 0.0
    count = 0
    avg = []
    for i in range(len(grades)):
        total += float(grades[i][2])
        count += 1
        if i % 4 == 0:
            avg.append((grades[i][0],total/count))
            total, count = 0.0, 0
    return avg

# Part 4
def find_top_students(grades, subject, n):
    arr = []
    #sort the names using bubble sort
    for i in range(len(grades)):
        if grades[i][1] == subject:
            arr.append((grades[i][0],grades[i][2]))

    print(arr)
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[i][1] < arr[j+1][1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i] = temp

    return arr[:n]

def update_grade(grades, student_name, subject, new_grades):
    updated_grades=[]
    print("Starting update")
    for name, s, grade in grades:
        if student_name == name and s == subject:
            updated_grades.append((name, subject, new_grades))
        else:
            updated_grades.append((name, s, grade))

    return updated_grades
#main program
filename = "grades.txt"
#write a new student "Joe Bloggs" "Computer Science" "99"
# write_grades("grades.txt", "Joe Bloggs", "Computer Science", "99")
grades = read_grades(filename)
print(calculate_average(grades))

arr = find_top_students(grades, "Maths", 3)
print(arr)

print(update_grade(grades, "Bob Smith", "English" , 88))
print(update_grade(grades, "Charlie Brown", "English" , 98))
