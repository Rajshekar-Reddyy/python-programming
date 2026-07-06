# Reverse a given string
if __name__=='__main__':
    s="cockroch"
    res=""
    for i in range(len(s)-1,-1,-1):
        res= res+s[i]
    print(res)
print("__"*100)
######################################################
#or
if __name__=='__main__':
    s="cockroch"
    res=""
    for i in range(0,len(s)):
        res= s[i]+res
    print(res)
print("__"*100)
####################################################################################################################
#write a pgm to check the srting is palindrome or not
if __name__=='__main__':
    s="malayalam"
    res=""
    for i in range(0,len(s)):
        res= s[i]+res
    if s==res:
        print("palindrome")
    else:
        print("not a palindrome")

print("__"*100)
