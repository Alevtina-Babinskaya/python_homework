import pandas as pd
import numpy as np
# 1. creating dataframe
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
task1_data_frame = pd.DataFrame(data_dict)

# 2. adding new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

# 3. updating column values
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

# 4. saving to csv
task1_older.to_csv('employees.csv', index=False )

# Task 2
task2_employees = pd.read_csv('employees.csv')
task2_json = pd.read_json('additional_employees.json')
more_employees = pd.concat([task2_employees, task2_json], ignore_index = True)
print(more_employees)

# Task 3
first_three = more_employees.head(3)
print(first_three)
last_two = more_employees.tail(2)
print(last_two)
employee_shape = more_employees.shape
print(employee_shape)
print(more_employees.info())

# Task 4
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()