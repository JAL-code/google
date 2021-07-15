#name = "Jaylen"
#print(name[1])

#for n in range(len(name)):
#    print(name[n])

text = "Random string with a lot of characters"
#print(text[-1])
#print(text[-2])
#print(text[1:4])
#print(text[20:])
#print(text[:20])
#print(len(text[:4]))

new_text = text[0:2] + "l" + text[3:]
print(new_text.index("lot"))

print("lot" in text)  #is substring in text

def first_and_last(message):
    len("")
    if message != "":
        if message[0] == message[-1]:
            return True
        else:
            return False
    else:
        return True

print(first_and_last("else"))
print(first_and_last("tree"))

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("tart@good.com","evil.com","good.com"))

answer = 'YES'
if answer.lower() == "yes":
    print("User said yes")

print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus"))

print("Forest".endswith("rest"))
print("Universal Serial Bus".count("e"))

cname = "Manny"
cnumber = len(cname) * 3
print("Hello {}, your lucky number is {}".format(cname, cnumber))

print("Your luck number is {dnumber}, {dname}.".format(dname=cname, dnumber=len(cname)*3))