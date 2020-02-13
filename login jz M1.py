#Jose Zavala
# 1/16/2020
# This is how to comment on pyhon
# This shows to to create a login, and give acesses to certain users
# This is good to be able to protect and give authorization to someone. 
#!/usr/bin/env python
username = input("Login: >> ")
user1 = "Jack"
user2 = "Jill"
if username == user1:
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
else:
    print("Access denied")

