class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}"

    def work(self):
        return f"{self.name} is working."

class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def display_department(self):
        return f"Department: {self.department}"

    def manage(self):
        return f"{self.name} is managing the {self.department} department."

manager = Manager("John", "E123", "HR")
print(manager.greet())
print(manager.get_employee_info())
print(manager.display_department())
print(manager.work())
print(manager.manage())
