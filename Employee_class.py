class Employee:
    increment = 1.6

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def increment_salary(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(cls, percentage):
        cls.increment = percentage


n = int(input("Enter the number of employee: "))
name = []
id = []
salary = []
emp = []
for i in range(n):
    name.append(input(f"Enter the name employee{i+1}: "))
    id.append(input(f"id of {name[i]}: "))
    try :
       salary.append(int(input(f"salary of {name[i]}: ")))
    except ValueError as ve:
        print(ve)

    emp.append(Employee(name[i],id[i],salary[i]))
    print()
    
print("Salary before increment:")
print()

trb = 0
for i in range(len(emp)):
    print(emp[i].name + " -> salary: ", emp[i].salary)
    trb += emp[i].salary

print()
print(f"Total Amount spend on salary before increment: {trb}")
print()
print("Salary after increment:")

tra = 0
inc = int(input("Enter the percentage of increment: "))
Employee.change_increment(inc)
for i in range(len(emp)):
    emp[i].increment_salary()
    print(emp[i].name + " -> salary: ", emp[i].salary)
    tra += emp[i].salary

print()
print(f"Total Amount spend on salary after increment: {tra}")
print(f"\nincrease in amount: {tra - trb}")
