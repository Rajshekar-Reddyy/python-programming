if __name__ == "__main__":
    for i in range (1,5+1):
        print("*")

    print("-"*199)

    #(2)###################

    for i in range(1,6):
        for j in range(1,6):
            print("*",end=" ")
        print()

    print("_"*190)

    ##(3)####################

    for i in range (1,6):
        for j in range(1,6):
            print(i,end=" ")
        print()

    print("-"*100)

    ##(4)######################

    for i in range(1,6):
        for j in range(1,6):
            print(j,end=" ")
        print()

    print("__"*100)

    ##(5)#####################3
    for i in range(1,5+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

    print("_"*190)

    ##(6)######################

    for i in range (1,6):
        for j in range (5,6-i-1,-1):
            print(j,end=" ")
        print()

    print("__"*100)

    ##(7)##########################

    for i in range(1, 6):
        for j in range(6-i,5+1,1):
            print(j, end=" ")
        print()

    print("-"*100)
    ########################

