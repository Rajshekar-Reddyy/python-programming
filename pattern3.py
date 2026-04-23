if __name__ == "__main__":
    r=5
    for i in range(1,r+1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()

    print("__"*100)
##############################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(r+1-i,5+1,1):
            print(j, end=" ")
        print()

    print("__"*100)
    #################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5,r+1-i-1,-1):
            print(j, end=" ")
        print()

    print("__" * 100)
    #################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1,i+1):
            print(j, end=" ")
        print()

    print("__" * 100)
    #################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(i,1-1,-1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ##########################     CHARACTERS PRINTING      #######################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(i, 1 - 1, -1):
            print(chr(j + 64), end=" ")
        print()

    print("__"*100)
    ####################################################################
    r=5
    for i in range(1,r+1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range(r-i+1,5+1,1):
            print(chr(j+64),end=" ")
        print()

    print("__"*100)
    #######################################################################
    r=5
    for i in range(1,r+1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range(i,1-1,-1):
            print(chr(j+64),end=" ")
        print()

    print("__"*100)
    #########################################################################
    r=5
    for i in range(1,r+1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range(5,r+1-i-1,-1):
            print(chr(j+64),end=" ")
        print()

    print("_"*100)
    #####################################################################33
    r=5
    for i in range(1,r+1):
        for j in range(1,r+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(chr(j+64),end=" ")
        print()

    print("__"*100)
   #############################  DAY 6 #####################################
    r = 5
    for i in range(1, r + 1):                    ###  TRIANGLE PATTERN
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1,i-1+1):
            print("*",end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(i,1-1,-1):
            print(j, end=" ")
        for j in range(2,i+1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5,r+1-i-1,-1):
            print(j, end=" ")
        for j in range(r+2-i,r+1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(r+1-i,5+1):
            print(j, end=" ")
        for j in range(r-1,r+1-i-1,-1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1,i+1):
            print(j, end=" ")
        for j in range(i-1,1-1,-1):
            print(j, end=" ")
        print()


    ###############            characters

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(i, 1 - 1, -1):
            print(chr(j+64), end=" ")
        for j in range(2, i + 1):
            print(chr(j+64), end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5, r + 1 - i - 1, -1):
            print(chr(j+64), end=" ")
        for j in range(r + 2 - i, r + 1):
            print(chr(j+64), end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(r + 1 - i, 5 + 1):
            print(chr(j+64), end=" ")
        for j in range(r - 1, r + 1 - i - 1, -1):
            print(chr(j+64), end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(chr(j+64), end=" ")
        for j in range(i - 1, 1 - 1, -1):
            print(chr(j+64), end=" ")
        print()

    print("__" * 100)
    print("DIAMOND SHAPE PATTERNS")
    #####################################       diamond shape patterns         ################

    r = 5
    for i in range(1, r + 1):  ###  diamond shape
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1, i - 1 + 1):
            print("*", end=" ")
        print()

    for i in range(r-1, 1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1, i - 1 + 1):
            print("*", end=" ")
        print()

    print("__"*100)
    ##############################################################
    r = 5
    for i in range(r,1-1,-1):  ###  diamond shape
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1, i - 1 + 1):
            print("*", end=" ")
        print()

    r = 5
    for i in range(2, r + 1):  ###  diamond shape
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        for j in range(1, i - 1 + 1):
            print("*", end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(r + 1 - i, 5 + 1):
            print(j, end=" ")
        for j in range(r - 1, r + 1 - i - 1, -1):
            print(j, end=" ")
        print()

    for i in range(r-1, 1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(r + 1 - i, 5 + 1):
            print(j, end=" ")
        for j in range(r - 1, r + 1 - i - 1, -1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 1 - 1, -1):
            print(j, end=" ")
        print()

    for i in range(r-1,1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 1 - 1, -1):
            print(j, end=" ")
        print()

    print("__" * 100)
    ########################################################################################
    r = 5
    for i in range(1,r+1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range (i,1-1,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")
        print()

    for i in range(r-1,1-1,-1):
        for j in range(1,r-i+1):
            print(" ",end=" ")
        for j in range (i,1-1,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")
        print()

    print("__" * 100)
        ########################################################################################
    r=5
    for i in range(r,1-1,-1):
            for j in range(1, r - i + 1):
                print(" ", end=" ")
            for j in range(5, r + 1 - i - 1, -1):
                print(j, end=" ")
            for j in range(r + 2 - i, r + 1):
                print(j, end=" ")
            print()

    for i in range(2, r + 1):
            for j in range(1, r - i + 1):
                print(" ", end=" ")
            for j in range(5, r + 1 - i - 1, -1):
                print(j, end=" ")
            for j in range(r + 2 - i, r + 1):
                print(j, end=" ")
            print()

    print("__" * 100)
        ########################################################################################

    r = 5
    for i in range(r, 1-1,-1):
            for j in range(1, r - i + 1):
                print(" ", end=" ")
            for j in range(i, 1 - 1, -1):
                print(j, end=" ")
            for j in range(2, i + 1):
                print(j, end=" ")
            print()

    for i in range(2, r + 1):
            for j in range(1, r - i + 1):
                print(" ", end=" ")
            for j in range(i, 1 - 1, -1):
                print(j, end=" ")
            for j in range(2, i + 1):
                print(j, end=" ")
            print()
    print("_"*100)

#############################################################3
    r = 5
    for i in range(r, 1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 1 - 1, -1):
            print(j, end=" ")
        print()

    for i in range(2, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 1 - 1, -1):
            print(j, end=" ")
        print()
    print("__"*100)
    ############################################3
    r = 5
    for i in range(r,1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5, r + 1 - i - 1, -1):
            print(j, end=" ")
        for j in range(r + 2 - i, r + 1):
            print(j, end=" ")
        print()

    r = 5
    for i in range(2, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5, r + 1 - i - 1, -1):
            print(j, end=" ")
        for j in range(r + 2 - i, r + 1):
            print(j, end=" ")
        print()

    ################################################
    r = 5
    for i in range(r,1-1,-1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5, r + 1 - i - 1, -1):
            print(chr(j+64), end=" ")
        for j in range(r + 2 - i, r + 1):
            print(chr(j+64), end=" ")
        print()

    r = 5
    for i in range(2, r + 1):
        for j in range(1, r - i + 1):
            print(" ", end=" ")
        for j in range(5, r + 1 - i - 1, -1):
            print(chr(j+64), end=" ")
        for j in range(r + 2 - i, r + 1):
            print(chr(j+64), end=" ")
        print()
############################################
k=1
    rows=5
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(k,end=" 
            ")
            k+=1

        print()

########################################
    rows=5
    for i in range(1,rows+1):
        k=rows
        for j in range(1,i+1):
            print(k,end=" ")
            k-=1
        print()
#######################################
    rows = 5
    for i in range(1, rows + 1):
        k = rows
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()
#######################################

    rows = 5
    for i in range(1, rows + 1):
        k = 1
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()
#####################################
    rows = 5
    for i in range(1, rows + 1):
        k = i
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()
#####################################3
    rows = 5
    for i in range(1, rows + 1):
        k = rows+1-i
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()
#######################################
    rows = 5
    for i in range(1, rows + 1):
        k = i
        for j in range(1, i + 1):
            print(k, end=" ")
            k -= 1
        print()
############################################
    rows=5
    k=1
    for i in range(1,rows+1):
        for j in range(1,i+1):
            if k%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
            k+=1
        print()





