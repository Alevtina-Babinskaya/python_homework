import csv
import os
import custom_module
from datetime import datetime
# task 2
def read_employees():
    employees_dict = {}
    employees_list = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    employees_list.append(row)
            employees_dict["rows"] = employees_list
        return employees_dict
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
employees = read_employees()


# task 3
def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found in the fields.")
employee_id_column = column_index("employee_id")

# task 4
def first_name(employee_id):
    try:
        column_id = column_index("first_name")
        return employees["rows"][employee_id][column_id]
    except Exception as e:
        print(f"An error occurred: {e}")
first_name(2)

#task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches
employee_find(2)
    
#task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# task 7
def sort_by_last_name():
    try:
        column_id = column_index("last_name")
        employees['rows'].sort(key=lambda row: row[column_id])
        return employees['rows']
    except Exception as e:
        print(f"An error occurred: {e}")
sort_by_last_name()


# task 8
def employee_dict(row):
    try:
        employee_dictionary = {}
        for field, value in zip(employees["fields"], row):
            if field != "employee_id":
                employee_dictionary[field] = value
        return employee_dictionary
        # for i, field in enumerate(employees["fields"]):
        #     print(i, field)
        #     if field != "employee_id":
        #         employee_dictionary[field] = row[i]
        #         print("printing dictionary")
        #         print(employee_dictionary[field])
        # return employee_dictionary
    except Exception as e:
        print(f"An error occurred: {e}")
print(employee_dict(employees['rows'][0]))


# task 9
def all_employees_dict():
    try:
        employee_dicts = {}
        for row in employees["rows"]:
            employee_dicts[row[employee_id_column]] = employee_dict(row)
        return employee_dicts
    except Exception as e:
        print(f"An error occurred: {e}")
all_employees_dict()

# task 10
def get_this_value():
    value = os.environ.get("THISVALUE")
    return value    
print(get_this_value())

# task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    return custom_module.secret
set_that_secret("I have a secret!")
print(custom_module.secret)

# task 12
def read_minutes():
    minutes1 = {}
    minutes1_tuple = []
    minutes2 = {}
    minutes2_tuple = []
    try:
        with open('../csv/minutes1.csv', 'r') as file:
            reader1 = csv.reader(file)
            for i, row in enumerate(reader1):
                if i == 0:
                    minutes1["fields"] = row
                else:
                    minutes1_tuple.append(tuple(row))
            minutes1["rows"] = minutes1_tuple
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    try:
        with open('../csv/minutes2.csv', 'r') as file:
            reader2 = csv.reader(file)
            for i, row in enumerate(reader2):
                if i == 0:
                    minutes2["fields"] = row
                else:
                    minutes2_tuple.append(tuple(row))
            minutes2["rows"] = minutes2_tuple
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()

#task 13
def create_minutes_set():
    try:
        minutes_set = set(minutes1["rows"]).union(set(minutes2["rows"]))
        return minutes_set
    except Exception as e:
        print(f"An error occurred: {e}")
minutes_set = create_minutes_set()


# task 14
def create_minutes_list():
    try:
        minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
        return minutes_list
    except Exception as e:
        print(f"An error occurred: {e}")
minutes_list = create_minutes_list()

# task 15
def write_sorted_list():
    try:
        minutes_list.sort(key=lambda x: x[1]) 
        new_minutes_list= list(map(lambda x: (x[0], datetime.strftime(x[1],'%B %d, %Y')), minutes_list))
        with open('minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in new_minutes_list:
                writer.writerow(row)
        return new_minutes_list
    except Exception as e:
        print(f"An error occurred: {e}")
write_sorted_list()


