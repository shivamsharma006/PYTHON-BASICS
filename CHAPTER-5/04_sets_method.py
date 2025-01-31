s = {234,5,221,4523,3}
print(s)
s.add(432)
print(s)

s1 = {243,435,3}
print(s1.union(s))
print(s1.intersection(s))
print(s1-s)

print({5,234}.issubset(s))
