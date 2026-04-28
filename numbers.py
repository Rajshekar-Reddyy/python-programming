#########       NUMBERS          ###########33333

if __name__=="__main__":
    n=int(input("enter a no"))    #pgm to write odd and even numbers side by side
    for i in range(1,n+1):
        if i%2!=0:
            print(i,end=" ")
        else:
            print(i)

        ######  or

    n = int(input("enter a no"))
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, i+1)

            #   or

    n = int(input("enter a no"))
    for i in range(1, n + 1,2):
        print(i,i+1)

######################
# WRITE A PGM TO WRITE YHE FACTORS OF A NUMBER
    n=int(input("enter a no to find factors"))
    for i in range(1,n+1):
        if n%i==0:
            print(i)

def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

if __name__=="__main__":
    n=12
    factor(n)

#########################
# write a pgm to print prime numbers from 1,10000
def prime_number(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count

if __name__=="__main__":
    for k in range(1,10000):
        num=k
        prime=prime_number(num)
        if prime==2:
            print(num)
##################################
# write a pgm to check wheather the given number is perfect or not

def sum_count(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=1
    return sum

if __name__ == "__main__":
    num=5
    sum=sum_count(num)
    if num==sum:
        print("perfect number")
    else:
        print("not perfect number")
###########################################
# pgm to reverse a number without using inbuilt method
def reverse(num):
    res = 0
    while num != 0:
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res


if __name__ == "__main__":
    num=532
    res=reverse(num)
    print(res)
#######################################################
# write a pgm to check wheather a number is a plandrome or not
def reverse(num):
    res = 0
    while num != 0:
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res


if __name__ == "__main__":
    num=12321
    res=reverse(num)
    if res ==num:
        print("palindrom")
    else:
        print("not palindrom")

###################################################
# write a pgm to print a plandrome number from 1 to 10000
def reverse(num):
    res = 0
    while num != 0:
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res


if __name__ == "__main__":
    for k in range(1,10000):
        num=k
        res=reverse(num)
        if res ==num:
            print(num)

###################################################
# write a pgm to print a plandrome number from 1 to 10000
def reverse(num):
    count=0
    res = 0
    while num != 0:
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res


if __name__ == "__main__":
    sum=0
    count=0
    k=1
    while(True):
        num=k
        res=reverse(num)
        if res ==num:
            print(num)
            sum+=num
            count+=1
        if count == 50:
            print("the avg is")
            print(sum / 50)
            break

        k+=1





