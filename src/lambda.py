lst = [1,2,3,4,5]

x = lambda a: a**2
print(x(4))

y = lambda b: b*2
print(y(lst))

def incr(x):
	return lambda n: n+x

inc = incr(10)
print(inc(2))
print(inc(3))
print(incr(15)(5))

test = lst.map(lambda x: (x, "a" * x))
print(test)
for x in test:
	print(x)
