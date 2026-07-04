# Reverse a given string
if __name__=='__main__':
    s="cockroch"
    res=""
    for i in range(len(s)-1,-1,-1):
        res= res+s[i]
    print(res)
print("__"*100)
