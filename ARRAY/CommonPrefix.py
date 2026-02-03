def commonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
    
strs = ["flower","flow","flight"]
print(commonPrefix(strs))