import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Employee ID", "Name", "Basic Salary",
                         "Allowance", "Deduction", "Net Salary"])

        for i in range(n):
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([emp_id, name, basic, allowance,
                             deduction, net_salary])

    print("\nPayroll Records:")

    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except ValueError:
    print("Please enter valid numbers.")