def longestCommonPrefix(strs):
    first_set = set(i for i in strs[0])
    res = ""
    indexs = []
    for s in strs:
        first_set = first_set.intersection(set([i for i in s]))
    first_str = strs[0]
    for i in range(len(first_str)):
        r = first_str[i]
        if r in first_set:
            if len(indexs) == 0:
                indexs.append(i)
                res += r
            elif i-1 == indexs[-1]:
                res += r
                indexs.append(i)
    return res


print(longestCommonPrefix(["reflower", "flow", "flight"]))
