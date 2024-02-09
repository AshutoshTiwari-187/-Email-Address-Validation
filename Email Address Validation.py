print("Welcome Guys this is the project on Email Address Validation")
print("Let's Start")
email=input("Enter yous Email :") #g@g.in
#This is the format of a valid email address->ashutosh@gmail.com
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email: #Now we are cheacking all the email from start to end.
                    if i==i.isspace:#Here we cheacking is there any space in the email address or not.
                        k=1
                    elif i.isalpha():#Here we cheacking that upper case of the email.
                        if i==i.upper(): 
                            j=1
                    elif i.isdigit():#Now if we found the digit in email address then its ok we have to continue.
                        continue
                    elif i=="_" or i=="." or i=="@":#Here we give the permission to cheak the '.' and '@' bcoz here the for loop checks each word of the address so to avoid the error with '.' and '@' we have to put and check it here also.
                        continue
                    else:
                         d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Your Email",email,"is correct")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")

