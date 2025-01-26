from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums : return 0

    k = 1
    for idx, num in enumerate(nums[1:], 1):
        if num != nums[idx-1]:
            nums[k] = num
            k += 1    

    return k

lst = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = removeDuplicates(lst)
print(lst[:k])
