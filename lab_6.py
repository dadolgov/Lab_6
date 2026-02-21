"""
Login app
Dmitrii Dolgov
"""

max_wrong_pass : int = 3
login_attempts : int = 0
security_status : str

users={"gwalters" : "S3curePass",
       "ddolgov1" : "@br@c@d@br@",
       "cybersec" : "kXsdtgf672theaytf761hASDaodfg8712",
       "admin" : "admin", 
       "guest" : "guest"}

login=input("Enter Login: ")
if login in users: 
    if login=="guest":
        security_status="Guest Access"
    else:
        security_status="Security Level 1"

    for attempt in range(max_wrong_pass):
        password=input("Enter Password: ")
        login_attempts+=1
        if users[login]==password:
            print(f"Welcome, {users[login]}. You have {security_status}.")
            break
        else: 
            print("Access Denied")
    else:
        print("Too many attempts. Account Blocked.")
else: print("User not found. Exiting.")

