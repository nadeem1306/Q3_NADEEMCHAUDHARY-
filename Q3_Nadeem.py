def minChar(n,s):
    special=0
    digit=0
    up=0
    lp=0
    
    print("Password contains:")
    for i in s:
        if i.islower():
            lp+=1
        elif i.isdigit():
            digit+=1
        elif i.isupper():
            up+=1
        else:
            special+=1
    print("Digits=" + str(digit))
    print("Special character=" + str(special))
    print("Uppercase Alphabet=" + str(up))
    print("Lowercase Alphabet=" + str(lp))
    if n>7 and digit>0 and special>0 and up>0 and lp>0:
        print("Strong Password. Good to go")
    else:
        print(str(8-n)+" more characters should be added")
n=int(input())
s=str(input())
minChar(n,s)