#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
print("=============================")
num=input("Enter a number: ")
print("=============================")
num=float(num)

if int(num) == num:
  print("the number is an integer")
else:
  print("the number is not an integer")
print("=============================\n\n\n")

