import re
import csv

#!/usr/bin/env python3

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location),  dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

employee_list = read_employees("home/pi/test_name.csv")
print(employee_list)

# Note: Following code should be fixed so it works.  
# The original purpose behind code is lost.

def rearrange_name(employee_list):
  future_employees = []
  for employer_data in employee_list:
    future_employees.append(employee_list['Name'])
  department_data = {} 
  for department_name in future_employees:
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", employer_data)
    if result == None:
      return department_name
    return department_data["{} {}".format(result[2], result[1])]

#dictionary = rearrange_name(employee_list)
#print(dictionary)
