#!/usr/bin/env python3
import re
import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=False, strict=True)
  employee_file = csv.DictReader(open(csv_file_location),  dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

employee_list = read_employees("home/pi/test_name.csv")
print(employee_list)

def rearrange_name(employee_list):
  future_employees = []
  for employer_data in employee_list:
    future_employees.append(employer_data['Name'])
  department_data = {}
  for department_name in set(future_employees):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", department_name)
    print("Testing Result {}".format(result))
    if result == None:
      department_data[department_name] = future_employees.count(department_name)
    else:
      department_data[department_name] = "{} {}".format(result[2], result[1])
  return department_data

dictionary = rearrange_name(employee_list)
print(dictionary)