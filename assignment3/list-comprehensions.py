import csv
employees = []
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)
employees_comp_list = [f'{row[1]} {row[2]}' for row in employees[1:]]
employees_list_sorted = [x for x in employees_comp_list if 'e' in x]
print (employees_comp_list)
print (employees_list_sorted)