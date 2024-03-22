# input array
arr =[3,4,5,6,7,8,9]
target= 9

low= 0
high = len(arr)-1


#loop
result =False
while low <= high:
    #divid
    mid= (low + high)// 2 # this is sthe middle index (not the value of the arr)
    
   
    # compare the mid with target
    if arr[mid] == target:
        result = True
        break
    # compare and discard the half
    if target> arr[mid]:
        low = mid+1
    else:
        high= mid+1 

if result== True:
    print("Found")
else:
    print("Not found")

