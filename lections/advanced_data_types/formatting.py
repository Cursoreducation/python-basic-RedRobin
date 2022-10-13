a = 7
b = 9
balloons = a + b * 2
def add_nums(a, b):
    return a + b

print("Sammy has {} balloons.".format(add_nums(a, b)))
print("Sammy has {1} balloons and {0} toys".format(7, 9))
print("Sammy has {balloons} balloons and {toys} toys".format(toys=7, balloons=9))

print(f"Sammy has {balloons} balloons.")

print(f"Sum of {a} and {b} is {a + b}")
print(f"Sum of {a} and {b} is {add_nums(a, b)}")

print("Sammy has %d balloons." % balloons)