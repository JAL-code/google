group_list = ['management', 'everyone', 'everyone', 'service', 'service', 'marketing', 'everyone', 'everyone', 'marketing', 'everyone', 'everyone', 'service', 'management', 'marketing', 'everyone', 'everyone', 'service', 'marketing', 'engineering', 'engineering', 'service', 'service', 'service', 'everyone', 'engineering', 'engineering', 'service', 'service', 'service', 'service', 'engineering', 'service', 'everyone', 'everyone', 'everyone', 'service', 'everyone', 'sales', 'everyone', 'marketing', 'marketing', 'service', 'marketing', 'sales', 'marketing', 'everyone', 'sales', 'engineering', 'marketing', 'service', 'management', 'everyone', 'service', 'service', 'engineering', 'marketing', 'everyone', 'management', 'marketing', 'engineering', 'service', 'service', 'management', 'service', 'everyone']
member_list = ['everyone', 'engineering', 'sales']



def print_prime_factors(number):  #Prints out all prime numbers divisible to a number
    factor = 2
    while factor <= number:
      if number % factor == 0:
        print(factor)
        number = number // factor
      else:
        factor += 1
    return "Done"

def is_power_of_two(n):
    while n % 2 == 0 and n !=0:
        n = n /2
    if n == 1:
        return True
    return False

def sum_divisors(n):
    sum = 0
    test_n = n-1
    if n > 0:
        while test_n > 0:
          if n % test_n == 0:
              sum = sum + test_n
          test_n -= 1
    elif n == 0:
        return 0
    return sum

def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result

def votes(params):
    for vote in params:
        print("Possible option: " + vote)

#print(votes(['yes','no','maybe']))

def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")

def is_power_of(number, base):
    if number < base:
        return number == 1
    return is_power_of(number/base, base)

def is_group(testGroupMember):
    found = False
    for validItem in member_list:
        #print("For test")
        if testGroupMember == validItem:
            #print(testGroupMember,validItem)
            found = True
            break
    return found

def count_users(group):
  count = 0
  for member in group_list:
    count += 1
    if is_group(member):
      count += count_users(member)-1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


#print(is_group("everyone"))
print(count_users('sales')) #should be 3
#print(count_users("engineering")) #8
#print(count_users("everyone")) #18

def sum_positive_numbers(n):
    if n == 0:
        return 0
    else:
      return sum_positive_numbers(n-1)+n

#print(sum_positive_numbers(3))
#print(sum_positive_numbers(5))

#for x in range(1,10, 3):
#    print(x)  #final is 7

#Test is_power_of
#print(is_power_of(8,2))  #True
#print(is_power_of(64,4)) #True
#print(is_power_of(70,10))  #False

#Test retry
#retry(create_user, 3)
#retry(stop_service, 5)

#pratice factorial
#for n in range(0,10):
#    print(n, factorial(n+1))
#0 1/1 1/2 2/3 6/4 24/5 120

#for x in range(1,11):
#   print(x**3)
# 1 8 27 64 125 216 343 512 729 1000

#maxTimes = 100//7
#for x in range(0,maxTimes+1):
#    print(x*7)
#print mult. of 7 between 0 and 100

#print_prime_factors(100) #Test print_prime_factors
# Should print 2,2,5,5

#Test is_power_of_two
#print(is_power_of_two(0))  #False
#print(is_power_of_two(1))  #True
#print(is_power_of_two(8))  #True
#print(is_power_of_two(9))  #False

#Test sum_divisors
#print(sum_divisors(0))  #0
#print(sum_divisors(3))  #1
#print(sum_divisors(36)) #36
#print(sum_divisors(102)) #114

#Test multiplication_table
#multiplication_table(3) #3,6,9,12,15
#multiplication_table(5) #5,10,15,20,25
#multiplication_table(8) #8,16,24