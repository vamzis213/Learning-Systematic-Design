u_pass = 911 
count = 1

user_passwd = int(input('Enter your password: '))
while user_passwd != u_pass :
    u_pass = int(input('Wrong password, Try agin: '))
    count += 1
    if count == 3 :
        print('"ALERT:Account Locked')
