#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
print("=============================")
a=input("A: ")
a=float(a)
a1=str(a)
b=input("B: ")
b=float(b)
b1=str(b)
c=input("C: ")
c=float(c)
c1=str(c)
print("=============================")
if a>b>c or a>c>b:
    expected = (c**2.0)+(b**2.0)
    if expected ==(expected>0.98*(a**2.0) and expected < 1.02*(a**2.0)):
        print("that is a right triangle")
    elif expected < 1.02*(a**2.0):
        print("that is an obtuse triangle")
    elif expected > 0.98*(a**2.0):
        print("that is an acute triangle")

if b>c>a or b>a>c:
    expected2 = (a**2.0)+(c**2.0)
    if expected2 ==(expected2 > 0.98*(b**2.0) and expected2 < 1.02*(b**2.0)):
        print("that is a right triangle")
    elif expected2 < 1.02*(b**2.0):
        print("that is an obtuse triangle")
    elif expected2 > 0.98*(b**2.0):
        print("that is an acute triangle")

if c>a>b or c>b>a:
    expect = (b**2.0)+(a**2.0)
    if expect > 0.98*(c**2.0) and expect< 1.02*(c**2.0):
        print("that is a right triangle")
    elif expect<1.02*(c**2.0):
        print("that is an obtuse triangle")
    elif expect> 0.98*(c**2.0):
        print("that is an acute triangle")
    
