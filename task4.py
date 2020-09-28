#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"
print("=============================")
a=input("Write a sentence: ")
print("=============================")
a=str(a)
b="password"
b=str(b)
if b in a:
  print("the sentence contains password")
else:
  print("the sentence does not contain password")
print("=============================\n\n\n")

