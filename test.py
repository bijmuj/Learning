x = []
for i in range(10):
    x.append(i)

y = x
y[0] += 1
print(x)
print(y)
