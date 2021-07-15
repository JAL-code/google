x = ["Now", "we", "are", "cooking!"]
print(x.reverse())

'''print(x)

len(x)

print("are" in x)

print("Today" in x)

print(x[0])
print(x[3])

print(x[1:3])
print(x[:2]) #print 0, 1
print(x[2:]) #print 2, 3 '''

x = ["Now", "we", "are", "cooking!"]
x.append("Hot!")
print(x)
x.insert(0, "Bob, ")
print(x)
x.remove("cooking!")
test_x = []
test_x.append(x.reverse())
print(test_x)
x.pop(1)
print(x)
x[2] = "were"
print(x)

print(x.index("we"))

''' def skip_elements(elements):
    	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for x in elements:
		# Does this element belong in the resulting list?
		if elements.index(x) % 2 == 0:
			# Add this element to the resulting list
			new_list.append(x)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be [] '''

""" winners = ["Bob", "Billy", "Brian"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

def skip_elementsE(elements):
    	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("a@exe.com", "Alex Yo"), ("shay@example.com", "Shay Brandt")]))

multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

multiples2 = [ x*7 for x in range(1,11)]
print(multiples2)"""

languages = "Python"#, "Perl", "Ruby", "Go", "Java", "C"
lengths = ''.join([languages[i] for i in range(len(languages)-1, -1, -1)])
print(lengths)

#def odd_numbers(n):
#	return [x for x in range(1,n+1) if x % 2 > 0]

#print(odd_numbers(10))

#help(str)

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("a@exe.com", "Alex Yo"), ("shay@example.com", "Shay Brandt")]))