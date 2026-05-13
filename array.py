#pgm to find min number in an array
arr = [12,13,14,8,15,43,44,5]
minimum=arr[0]
for x in arr:
    if x<minimum:
        minimum=x
print(minimum)

######################################

#pgm to print max number in an array
arr = [12,13,14,8,15,78,5]
maximum= arr[0]
for x in arr:
    if x>maximum:
        maximum=x
print(maximum)

##########################################################
"""
array traversal
"""
if __name__=='__main__':
    arr=[10,20,30,40]
    #with using indexing
    for i in range(0,len(arr)):
        print(arr[i])
    print("-----------------------------------------------")
    #without using indexing
    for j in arr:
        print(j)
