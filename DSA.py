#MERGE SORT ALGORITHM

def merge(arr1,arr2,res):
    i=0
    j=0
    k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            res[k]=arr1[i]
            k=k+1
            i=i+1
        else:
            res[k]=arr2[j]
            k=k+1
            j=j+1
    while j<len(arr2):
        res[k]=arr2[j]
        k=k+1
        j=j+1
    while i<len(arr1):
        res[k]=arr1[i]
        i=i+1
        k=k+1
    return res


def divide(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    divide(left)
    divide(right)
    return  merge(left,right,arr)

if __name__=="__main__":
    arr=[9,7,1,5,4,2,8,3]
    print(divide(arr))


