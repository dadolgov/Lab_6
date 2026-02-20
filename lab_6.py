"""
Login app
Dmitrii Dolgov
"""

users={"gwalters" : "S3curePass",
       "ddolgov1" : "@br@c@d@br@",
       "cybersec" : "kXsdtgf672theaytf761hASDaodfg8712",
       "admin" : "admin", # we all been there, aren't we?
       "guest" : "guest"}

login=input("Enter Login: ")

if(login in users): 
    password=input("Enter Password: ")
    if(users[login]==password):
        print("Welcome")
    else: 
        print("Wrong password")
else: print("User not found")

