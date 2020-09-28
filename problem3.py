#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

print("=============================")
username=input("Enter a username: ")
print("=============================")
user=str(username)
b="admin"
b=str(b)
if b in user:
  pw=input("Password: ")
  pw=str(pw)
  a="12345password"
  a=str(a)
  if pw is a:
    print("Access granted")

else:
  print("invalid user")
print("=============================\n\n\n")

