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
