data = b'yabb\'adabba,do'
data2 = data.decode("utf-8")

print(data2)

before, sep, after = data2.partition(",")
print(before)
print(after)
x = after.strip("d")
print(x)