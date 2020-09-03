a = [1,2,3,4,5,6,7,8,9,10,11,12]
num = 12

def binary(arr,num):
    left = 0
    right = len(arr)-1
    while(left<=right):
        mid = left+(right-left)//2
        if(arr[mid]==num):
            return True
        elif(arr[mid]>num):
            right=mid-1
        else:
            left=mid+1
    return False

print(binary(a,num))
