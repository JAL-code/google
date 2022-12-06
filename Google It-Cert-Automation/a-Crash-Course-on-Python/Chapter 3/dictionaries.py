x = {}
print(type(x))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)


print(f"Text: {file_counts['txt']}")

print("html" in file_counts) #true if found
#dictionaries are mutable

file_counts["cfg"] = 8  #add item
print(file_counts)

file_counts["csv"] = 17 #replaces value for already assigned csv 
print(file_counts)

del file_counts["cfg"]
print(file_counts) 

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():  #value pairs
    print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys(), file_counts.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys, values in cool_beasts.items():
    print("{} have {}".format(keys, values))
    
    
print("Test get: " + cool_beasts.get("octopuses"))

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

count_letters("aaaaa")
count_letters("tenant")
print(count_letters("lksdajfo;asijnfl;kdnv;oisrnfg;lzknv;oizdfo;hgj"))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes, color in wardrobe.items():
	for n in color:
		print("{} {}".format(n, clothes))