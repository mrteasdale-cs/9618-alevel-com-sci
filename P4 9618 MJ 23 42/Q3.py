class Employee():
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = float(HourlyPay)  # Convert to float
        self.__EmployeeNumber = EmployeeNumber
        self.__JobTitle = JobTitle
        self.__PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hoursworked):
        Pay = self.__HourlyPay * float(Hoursworked)
        self.__PayYear2022[WeekNumber - 1] = Pay

    def GetTotalPay(self):
        total = 0
        for i in range(len(self.__PayYear2022)):
            total += self.__PayYear2022[i]
        return total

class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, Bonus):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__Bonus = float(Bonus)

    def SetPay(self, WeekNumber, Hoursworked):
        # Add bonus as a percentage of hours worked
        Hoursworked = float(Hoursworked) + (float(Hoursworked) * self.__Bonus / 100)
        super().SetPay(WeekNumber, Hoursworked)

Pay = 0.00
ID = ""
Bonus = 0.00
Title = ""
Temp = ""
EmployeeArray = []

with open("Employees.txt" , "r") as file:
    for i in range(8):
        Pay = file.readline().strip("\n")
        ID = file.readline().strip("\n")
        Temp = file.readline().strip("\n")

        try:
            Bonus = float(Temp)
            Title = file.readline().strip("\n")
            EmployeeArray.append(Manager(Pay, ID, Title, Bonus))
        except ValueError:
            Title = Temp
            EmployeeArray.append(Employee(Pay, ID, Title))

def EnterHours():
    with open("HoursWeek1.txt" , "r") as weekFile:
        for i in range(8):
            ID = weekFile.readline().strip()
            Hours = weekFile.readline().strip()
            for emp in EmployeeArray:
                if emp.GetEmployeeNumber() == ID:
                    emp.SetPay(1, Hours)

EnterHours()
for i in range(8):
    print(EmployeeArray[i].GetEmployeeNumber(), " " , EmployeeArray[i].GetTotalPay())
