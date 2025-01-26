from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: return ""

    prefix = strs[0]
    for string in strs[1:]:
        length = min(len(prefix), len(string))
        num = 0
        while num < length and prefix[num] == string[num]:
            num += 1
        prefix = string[:num]
        
    return prefix

ret = longestCommonPrefix(["flower","flow","flight"])
print(ret)