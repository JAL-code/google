def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes *60
    return hours, minutes, remaining_seconds

cows = ["moo", "mouu", "mmmmmooo"]
for cow in cows:
    print(cow)
print(type(7))
print(type("s"))
print(type(2.5))

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
print(convert_seconds(5000))
print(type(convert_seconds(5000)))