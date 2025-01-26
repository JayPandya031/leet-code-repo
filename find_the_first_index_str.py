def strStr(haystack: str, needle: str) -> int:
    length = len(needle)
    for idx in range(len(haystack) - length + 1):
        if needle == haystack[idx:idx+length]:
            return idx
    
    return -1

ret = strStr("leetcode", "code")
print(ret)