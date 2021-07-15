import random
import datetime

now = datetime.datetime.now()

print(random.randint(1,10))

print(type(now))
print(now)  #__str__
print(now.year)

print(now + datetime.timedelta(days=28))