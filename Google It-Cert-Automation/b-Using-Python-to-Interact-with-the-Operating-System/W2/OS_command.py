#remove file
import os

with open("first_draft.txt", "w") as file:
    file.write("It was a dark and stormy night")

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night2")

os.remove("novel.txt")
os.remove("finished_masterpiece.txt")

#rename
os.rename("first_draft.txt", "finished_masterpiece.txt")

#check
print(os.path.exists("finished_masterpiece.txt"))

print(os.path.getsize("spider.txt"))
print(os.path.getmtime("spider.txt"))
import datetime
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))

file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")

print(os.path.abspath("spider.txt"))

#check current directory - getcwd
#unix - pwd

print(os.getcwd())

#mkdir  make directory
os.mkdir("new_dir")
os.listdir("new_dir")

#chdir change dir
os.chdir("new_dir")
print(os.getcwd())
#os.rmdir("new_dir") #directory must be empty

os.listdir("website")  #list directory