from typing import List

def removeElement(nums: List[int], val: int) -> int:
    k = 0 
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  
            k += 1
    return k

nums = [1, 1, 2, 3, 2, 5, 4, 2]
ret = removeElement(nums, 2)
print(nums[:ret])