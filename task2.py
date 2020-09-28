#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
print("=============================")
a=input("Choose a number: ")
print("=============================")
a=float(a)
if a>0:
  print("positive")
elif a<0:
  print("negative")
else:
  print("zero")
print("=============================\n\n\n")