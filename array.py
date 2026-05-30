#pgm to find min number in an array
arr = [12,13,14,8,15,43,44,5]
minimum=arr[0]
for x in arr:
    if x<minimum:
        minimum=x
print(minimum)

########################################################

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

############################################################
# linear search
def lsearch(arr,key):
    for i in range(0,len(arr)):
        if(arr[i]==key):
            return i
    return -1

if __name__=="__main__":
    arr=[10,20,30,40,50,60]
    key=40
    index=lsearch(arr,key)
    print(index)

################################################################
# binary search
def b_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif key > arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

if __name__=="__main__":
    arr=[2,4,8,12,14,16,18,19,20,22,24]
    key=16
    index=b_search(arr,key)
    print(index)

#################################################################### 
#reverse an array
def reverse_arr(arr):
    res=[]
    for i in range(len(arr)-1,-1,-1):
        res.append(arr[i])
    return res

if __name__=="__main__":
    arr=[2,4,6,8,10,12,24]
    res=reverse_arr(arr)
    print(res)

#######################################################################
# reverse an array using binary search
def rev_arr(arr):
    low=0
    high=len(arr)-1
    while low<high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

if __name__=="__main__":
    arr=[2,4,6,8,10,12,24]
    res = rev_arr(arr)
    print(res)

############################################################################3
#write a pgm to move the maximum element at the end of the array/list
print("write a pgm to move the maximum element at the end of the array/list")
if __name__=="__main__":
    arr=[20,87,97,24,45,26,60]
    for i in range (0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)

#########################################################
#bubble sort algorithm
if __name__=="__main__":
    arr=[20,87,97,24,45,26,60]
    for k in range(0,len(arr)):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)

######################################################################
# reverse an array in anti clock wise direction
arr=[10,20,30,40,50]
temp=arr[0]
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
arr[-1]=temp
print(arr)
##########################################################################
# reverse an array in anti clock wise direction for 4 times
def anti(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp

if __name__=="__main__":
    arr=[10,20,30,40,50]
    for i in range(4):
        anti(arr)
    print(arr)
###########################################################################
# rotate an array in clock wise direction
arr=[10,20,30,40,50]                                     ####o/p==[50, 10, 20, 30, 40]
temp=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=temp
print(arr)

#or

arr=[10,20,30,40,50]                                     ####o/p==[50, 10, 20, 30, 40]
temp=arr[-1]
for i in range(len(arr)-2,-1,-1):
    arr[i+1]=arr[i]
arr[0]=temp
print(arr)

####################################################################
# compare 2 arrays without using == operator

def equals(arr,brr):
    if len(arr)!=len(brr):
        return False
    else:
        for i in range(0,len(arr)):
            if arr[i]!=brr[i]:
                return False
        return True
if __name__=="__main__":
    arr=[1,2,3,4,5]
    brr=[1,2,3,4,5]
    


