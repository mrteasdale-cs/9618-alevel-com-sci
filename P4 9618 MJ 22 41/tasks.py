'''Car value problem:
1 point.
Write a program that illustrates the depreciation of the value of a car.
The program takes three parameters, the year, the value of the car and the
minimum resale value. The car depreciates by 30% in the first and second year,
and 20% in each subsequent year. The program should output the values from the
model until the resale value is reached. E.g.
Car is bought for £12500. Minimum resale value is £6000.
2022: £12500
2023: £8750
2024: £6125
Part exchange in 2024.
'''
def carValueProblem(year, value, resalePrice):
    yearBought = year
    while (value > resalePrice):
        print("{}: {}".format(year, value))
        if (year < (yearBought + 2)):
            value = value - (value * 0.3)
        else:
            value = value - (value * 0.2)
        year = year + 1

carValueProblem(2024, 12500, 3000)
'''Square root problem: 2 points.
Write a function called SqRoot that calculates the square root of a number, X using Newton’s
 method. Root = X at the start of the algorithm. Root is repeatedly recalculated as 
 0.5*(Root+(X/Root) until the value of Root does not change. 
64
32.5
17.234615384615385
10.474036101145005
8.292191785986859
8.00000000000017
8.0
8.0 – This value equals the previous value of Root.'''
def rootProblem(X):
    root = X
    i = 0
    while root != i:
        i = root
        root = 0.5 * (root + (X / root))
        print(root)

rootProblem(144)