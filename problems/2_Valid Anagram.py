def valid_anagram(t , s):
    if len(t) != len(s):
        return False
    
    l = [0 for _ in range(26)]
    
    for i in range(len(s)):
        l[ord(s[i]) - 97] += 1
        l[ord(t[i]) - 97] -= 1
    
    for j in l:
        if j != 0:
            return False
        
    return True
    
print(valid_anagram('abcw','wcab'))