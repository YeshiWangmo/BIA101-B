input_arr = [1,2,3,4,4]
def containsDuplicate(nums):
    # convert thr list to a set
    nums_set= set(nums)
    if len(nums)== len(nums_set):
        return True
    else:
        return False
    
result = containsDuplicate(input_arr)

print(result)
