from elements import Elements

t = "abcdef"
x = Elements()
c = x.encrypt(t)
print(c)
v = x.decrypt(c)
print(v)

