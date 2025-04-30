import random
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Chris", "Jessica", "Daniel", "Laura"]
surnames = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]
expanded_first_names = [random.choice(first_names) for i in range(25)]
expanded_surnames = [random.choice(surnames) for i in range(25)]

name = [[random.choice(expanded_first_names), random.choice(expanded_surnames)] for _ in range(1,249)]
score = [random.randint(1,100) for _ in range(1,249)]

YearSize = 249

for student in range(0, YearSize-1):
    Temp1 = score[i]#1D array
    Temp2 = name[i][0]#2D array ["William", "Smith"]
    Temp3 = name[i][1]
    Counter = student
    while Counter > 0 and score[Counter-1] < Temp1: 
        score[Counter] = score[Counter-1]
        name[Counter][0] = name[Counter-1][0]
        name[Counter][1] = name[Counter-1][1]
        Counter = Counter - 1
    score[Counter] = Temp1
    name[Counter][0] = Temp2
    name[Counter][1] = Temp3

# Print sorted scores and corresponding students
for i in range(YearSize-1):
    print(score[i], student[i])



my_list = [7,4,6,90,2,44,53,32]#out of order
#my_list = [90,53,44,32,7,6,4,2]
list_size = 8
#sort into decending order (Z->A) (big-small)
for i in range(0, list_size):
    
    Temp1 = my_list[i] #temp=7
    Counter = i #counter = 0
    
    while Counter > 0 and my_list[Counter-1] < Temp1: 
        my_list[Counter] = my_list[Counter-1]
        Counter = Counter - 1
        print(f"counter: {Counter} swap {my_list[Counter]} with {my_list[Counter-1]}")
    
    my_list[Counter] = Temp1
        
print(my_list)


