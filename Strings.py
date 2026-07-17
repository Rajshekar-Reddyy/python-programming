# Reverse a given string
if __name__=='__main__':
    s="cockroch"
    res=""
    for i in range(len(s)-1,-1,-1):
        res= res+s[i]
    print(res)

######################################################
#or
if __name__=='__main__':
    s="cockroch"
    res=""
    for i in range(0,len(s)):
        res= s[i]+res
    print(res)
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
#######################################################################################################################
#convert lowercase str to uppercase str
def upper1(s):
    res=""
    for ch in s:
        if ord(ch)>=97 and ord(ch)<=122:
            res+=chr(ord(ch)-32)
        else:
            res+=ch
    return res
if __name__=='__main__':
    s="HelLo"
    res=upper1(s)
    print(res)

#############################################################################################################################
#convert uppercase str to lowercase str
def lower1(s):
    res=""
    for ch in s:
        if ord(ch)>=65 and ord(ch)<=90:
            res+=chr(ord(ch)+32)
        else:
            res+=ch
    return res
if __name__=='__main__':
    s="HelLo"
    res=lower1(s)
    print(res)

########################################################################################################################
#Swapping th uppercase into lower case and lower into uppercase
def swap1(s):
    res=""
    for ch in s:
        if ord(ch)>=65 and ord(ch)<=90:
            res+=chr(ord(ch)+32)
        elif ord(ch) >= 97 and ord(ch) <= 122:
            res+=chr(ord(ch)-32)

    return res
if __name__=='__main__':
    s="HelLo"
    res=swap1(s)
    print(res)

##############################################################################################################################
#pgm to check the count of vowel in a string
if __name__=='__main__':
    s="lalith kumar soni ravikumar"
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
    print(count)

################################################################################
# pgm to count vowels, consonants, and spaces in a string
if __name__=='__main__':
    s="Dhee coding lab"
    countvowels=0
    countconsonents=0
    countspaces=0
    for ch in s:
        if ch in "aeiouAEIOU":
            countvowels+=1
        elif ch==" ":
            countspaces+=1
        else:
            countconsonents+=1
    print(countspaces)
    print(countconsonents)
    print(countspaces)

##############################################################################
# pgm to split a given string where # is given.
if __name__=='__main__':
    s="zeus#your#son#has#returned"
    arr=s.split("#")
    print(arr)

#############################################################################
#String reversal pgm
def rev(s):
    res=""
    for ch in s:
        res=ch+res
    return res
if __name__=='__main__':
    s="dhee coding lab"
    res=rev(s)
    print(res)
