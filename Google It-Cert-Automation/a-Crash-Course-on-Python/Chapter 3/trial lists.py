def pig_latin(text):
    say  = ""
    words = text.split(" ")
    for word in words:
        #add the last letter in the word, then the 2nd to last and so on. . .
        #then add final reversed word to the phrase "hay"
        say += "{}{}".format("".join([word[i] for i in range(len(word)-1, -1, -1)]),"hay ")
    return say.strip()
    
print(pig_latin("Hello Dave and Steve"))

def group_list(group, users):
    members = ", ".join(users[x] for x in range(0,len(users))) #list(enumerate(users))
    #members = ("{}, ".format(users[x]) for x in range(0, len(users)+1))
    #print(members[1].values(1))
    return ("{}: {}".format(group, members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"