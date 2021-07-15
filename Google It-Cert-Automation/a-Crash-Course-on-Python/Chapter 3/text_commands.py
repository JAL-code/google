def first_and_last(message):
    
    if len(message) != 0:
        if message[0] == message[-1]:
            return True
        else: 
            return False
    else:
        return True

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        print(word)
        result += word[0].upper()
    return result

def to_celsius(x):
    return (x-32)*5/9

#for x in range(0, 101, 10):
#    print("{:>3} F | {:>6.2f} C". format(x, to_celsius(x)))

#samplePhrase ="cow and cat and horse"
#print(initials(samplePhrase))

#color = "Orange"
#print(color[1:4])

#print(first_and_last("else"))
#print(first_and_last("tree"))
#print(first_and_last(""))\\

def group_list(group, users):
    members = ("{}, ".format(users) for x in range(0,len(users)+1))
    print(members)
    return "{}: {}".format(group, members)

#print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
#print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
#print(group_list("Users", "")) # Should be "Users:"

def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split(" ")
    for word in words:
        print(word)
        say += lettr for lettr in range(len(word),0,-1)
    # Turn the list back into a phrase
    return "hay ".join(words).strip()
		
print(pig_latin("hello how are you")) 