# Regular expressions can be used to search text within a string.
#use the re module
import re

# use findall to find any text within a string. Case sensitive, unless use re.IGNORECASE
# the first argument is the regular expression to match
# starts with a and ends with c.  zero or more instances of b.
# the second argument is the string to search

# one without b
print(re.findall("ab*c", "ac"))
# one with b
print(re.findall("ab*c", "abcd"))
# one without b again
print(re.findall("ab*c", "acc"))
# multiple patterns found
print(re.findall("ab*c", "abcac"))
# no patterns found returns empty list
print(re.findall("ab*c", "abdc"))
print(f"Using IGNORECASE.")
# Example to ignore case
# no solution
print(re.findall("ab*c", "ABC"))
# solution found even though sting is capitalized.
print(re.findall("ab*c", "ABC", re.IGNORECASE))
print(f"Using a period to represent any single character.")
# period (.) can represent any single character.
print(re.findall("a.c", "abc"))
print(re.findall("a.c", "abbc"))
print(re.findall("a.c", "ac"))
print(re.findall("a.c", "acc"))

print(f"Using (.*) to find every sub string inbetween starting and ending characters.")
# (.*) can represent any sub string regardless of letters.
print(re.findall("a.*c", "abc"))
print(re.findall("a.*c", "abbc"))
print(re.findall("a.*c", "ac"))
print(re.findall("a.*c", "acc"))

print(f"Using search to find the first and most inclusive result.")
# Use re.search to find the first and most inclusive result
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

print(f"Using sub to replace the longest text found in a search.")
# Use re.sub (.*) to replace every instance that matches the regular expression
string = "Everything is <replaced> if it's in <tags>."
print(f"Before: {string}")
string = re.sub("<.*>", "ELEPANTS", string)
print(f"After: {string}")

print(f"Using sub to replace the shortest text found in a search.")
# Use re.sub (.*?) to replace every instance that matches the regular expression
string = "Everything is <replaced> if it's in <tags>."
print(f"Before: {string}")
string = re.sub("<.*?>", "ELEPANTS", string)
print(f"After: {string}")