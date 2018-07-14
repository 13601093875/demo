print all(["1", "2", "0"])
print all([])
print any(["", 0, None])
print any(["", 0, None, "0"])
print any(["1"])
print any([])

print bin(123456)
print callable(any)
print callable(123)
print cmp("1000", "2")
print cmp(20, 1)  # -1 0 1
c = filter(lambda x: x * x != 4, [1, 2, 3, 4])
print c

