def isValid(s: str) -> bool:
    stack = []
    hashmap = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in hashmap.values():
            stack.append(char)
        elif char in hashmap.keys():
            if stack and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                return False
        else:
            return False
    return not stack

ret = isValid("(){{}}[[]]")
print(ret)