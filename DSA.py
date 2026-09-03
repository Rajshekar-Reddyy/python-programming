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

###########################################################################################################################
# QUICK SORT

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low >= high:
        return
    pivot_index=partition(arr,low,high)

    quick_sort(arr,low,pivot_index-1)
    quick_sort(arr,pivot_index+1,high)


if __name__=="__main__":
    arr=[9,7,1,5,4,2,8,3,10]
    quick_sort(arr,0,len(arr)-1)
    print(arr)

################################################################################################################################
# Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        left=0
        right=len(s)-1
        while left <= right:
            ch1=s[left]
            ch2=s[right]
            if not ch1.isalnum():
                left+=1
                continue 
            if not ch2.isalnum():
                right-=1
                continue
            if ch1!=ch2:
                return False
            left+=1
            right-=1
        return True

        


        
            



