#!/usr/bin/env python3

from validations import validate_user

#print(validate_user("", -1)) #Error
#print(validate_user("",1))  #False
#print(validate_user("myuser",1)) #True
#print(validate_user(88,1)) #object of type 'int' has no len()
#print(validate_user([], 1)) #False
#print(validate_user(["myuser"],1))  #'list' object has no attribute 'isalnum'
print(validate_user([3], 1))  #AssertionError: username must be a string. not run when 
