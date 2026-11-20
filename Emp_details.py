
class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("------------------------")


employees = []

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        emp = Employee(emp_id, name, salary, department)
        employees.append(emp)

        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            for emp in employees:
                emp.display()

    elif choice == 3:
        search_id = int(input("Enter Employee ID to search: "))
        found = False

        for emp in employees:
            if emp.emp_id == search_id:
                print("Employee Found!")
                emp.display()
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
