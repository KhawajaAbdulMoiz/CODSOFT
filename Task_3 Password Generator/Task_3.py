import string
import random
if __name__== "__main__":
    s1 = string.ascii_letters
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    s4 = string.digits
    s5 = string.punctuation
    while True:
        passlen=int(input("Enter your Password Lenght: \n"))
        s=[]
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
        s.extend(s5)
        random.shuffle(s)
        print("Your Password is : ","".join(s[0:passlen]))
    
        if passlen <= 0:
            print("Password length must be a positive integer.")
            continue

        repeat = input("Do you want to generate another password? (yes/no): ")
        if repeat.lower() != 'yes':
               
            if repeat.lower() == 'no':
                print("Thanks")
            break
            