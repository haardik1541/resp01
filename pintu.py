class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employee_data(employees, key):
    if key == 1:
        employees.sort(key=lambda emp: emp.age)
    elif key == 2:
        employees.sort(key=lambda emp: emp.name)
    elif key == 3:
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return

    return employees

def print_employee_data(employees):
    for employee in employees:
        print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__pintu__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    while True:
        print("\nOptions for Sorting:")
        print("1. Sort by Age")
        print("2. Sort by Name")
        print("3. Sort by Salary")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        sorted_employees = sort_employee_data(employees.copy(), choice)
        if sorted_employees:
            print("\nSorted Employee Data:")
            print_employee_data(sorted_employees)