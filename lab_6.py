"""
Login app
Dmitrii Dolgov
Program simulates a login and password check
2/21/2026
"""
# initializing variables
max_wrong_pass : int = 3
login_attempts : int = 0
login : str
password : str
security_status : str
users={"gwalters" : "S3curePass",
       "ddolgov1" : "@br@c@d@br@",
       "cybersec" : "kXsdtgf672theaytf761hASDaodfg8712",
       "admin" : "admin", 
       "guest" : "guest"}

# Login check
login=input("Enter Login: ")
if login in users: 
    # assign a security group if login is correct
    if login=="guest":
        security_status="Guest Access"
    else:
        security_status="Security Level 1"
# Password loop. After 3 attempts(can be changed) account gets blocked
    for attempt in range(max_wrong_pass):
        password=input("Enter Password: ")
        login_attempts+=1
        # if password is correct, print the message and exit the loop
        if users[login]==password:
            print(f"Welcome, {login}. You have {security_status}.")
            break
        # if password is wrong, print the message and stay in the loop
        else: 
            print("Access Denied")
    #if the loop completed without breaking (3 attempts), "block" the account
    else:
        print("Too many attempts. Account Blocked.")
# login check failed
else: print("User not found. Exiting.")

