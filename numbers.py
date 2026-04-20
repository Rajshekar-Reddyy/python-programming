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





