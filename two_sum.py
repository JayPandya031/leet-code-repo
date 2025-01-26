from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for idx, num in enumerate(nums):
        if ( prev_idx := hash_map.get(target - num) ) is not None:
            return [prev_idx, idx]
        
        hash_map[num] = idx

ret = twoSum([2, 7, 11, 15], 9)
print(ret)