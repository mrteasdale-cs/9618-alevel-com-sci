#genetic algorithm to solve an expression for unknown variables
import random

def solve(a,x,y,z):
    return (5*7*a - 12*x**4 + 7*y**2 + 78*z) - 99

def fitnessAlgorithm(a,x,y,z):
    ans = solve(a,x,y,z)

    if ans == 0:
        return 9999
    else:
        return abs(1/ans)

#generate some solutions randomly
def generateSolutions(num):
    solutions = []
    for s in range(num):
        solutions.append((
            random.uniform(0,1000),
            random.uniform(0,1000),
            random.uniform(0,1000),
            random.uniform(0,1000),))
    return solutions

def runGA(solutionsList):
    for i in range(10000):
        rankedSolutions = []
        for s in solutionsList:
            rankedSolutions.append( (fitnessAlgorithm(s[0],s[1],s[2],s[3]),s) )
            rankedSolutions.sort()
            rankedSolutions.reverse()

        print(f"=== Generation {i} best solutions ===")
        print(rankedSolutions[0])

        if rankedSolutions[0][0] > 99999:
            break

        #take 100 best solutions and add ot new bestsolutions list
        bestSolutions = rankedSolutions[:100]
        elem = []
        for s in bestSolutions:
            elem.append(s[1][0])
            elem.append(s[1][1])
            elem.append(s[1][2])
            elem.append(s[1][3])

        #create new generation
        newGen = []
        for _ in range(1000):
            e1 = random.choice(elem) * random.uniform(0.99,1.01)
            e2 = random.choice(elem) * random.uniform(0.99,1.01)
            e3 = random.choice(elem) * random.uniform(0.99,1.01)
            e4 = random.choice(elem) * random.uniform(0.99,1.01)

            newGen.append((e1,e2,e3,e4))
        solutionsList = newGen

def main():
    solutions = generateSolutions(10000)
    runGA(solutions)

main()