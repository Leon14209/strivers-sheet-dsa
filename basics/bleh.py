#LARGEST ODD NO
"""s="6942014"
o=1
for i in range(len(s)):
    k=s[0:i+1]
    if int(k)%2!=0:
        o=k
print(o)""" 
#LONHEST COMMON PREFIX
"""def longestCommonPrefix(strs):
    first = strs[0]

    for i in range(len(first)):
        for j in strs:
            if i >= len(j) or first[i] != j[i]: #ENSURES WE DONT EXCEED INDEX
                return first[:i]

    return first """
# 