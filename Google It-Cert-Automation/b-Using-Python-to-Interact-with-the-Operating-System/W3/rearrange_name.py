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

employee_list = read_employee("home/pi/test_name.csv")
print(employee_list)

def rearrange_name(employee_list):
  future_employees = []
  for employer_data in employee_list:
    future_employee.append(employee_list['Name'])
  department_data = {} 
  for department_name in furturet:
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", employee_data)
    if result == None:
      return name
    return department_data[department_data"{} {}".format(result[2], result[1]) 

#dictionary = rearrange_name(employee_list)
#print(dictionary)
