import re

def rearrange_name(name):
    pattern = r" [0-9]{1,}|[0-9]*"
    name_filtered = re.sub(pattern, '', name, count=0, flags =0)
    print("Before: {}| After:{}".format(name, name_filtered))
    result = re.search(r"^([\w .]*), ([\w .]*)$", name_filtered)
    if result is None:
        return ""
    return "{} {}".format(result[2], result[1])

print(rearrange_name("0"))