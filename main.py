from elements import Elements

t = "abcdef"
x = Elements()
c = x.encode(t)
print(c)
v = x.decode(c)
print(v)

