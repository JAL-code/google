#create file descriptor
file = open("spider.txt")
print(file.readline())
print("NewLine A")
print(file.readline())
print("NewLine A")
print(file.read())
file.close()
print("New Section B")

with open("spider.txt") as file:
    print(file.readline())

print("New Section C")

with open("spider.txt") as file:
    for line in file:
        print(line.upper())

print("New Section D")

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

print("New Section E")

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

print("New Section F")

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

#stage1

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

#stage 2

with open("guests.txt") as guests:
    for line in guests:
        print(line)

#stage 3
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

#stage 4
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#stage 5
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

#stage 6
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#stage 7

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))