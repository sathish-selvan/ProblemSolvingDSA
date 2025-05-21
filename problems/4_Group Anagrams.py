from collections import defaultdict

def group_anagram(arr):
    
    d = defaultdict(list)

    for word in arr:
        print(word)
        alpha_list = [0 for i in range(26)]
        
        for char in word:
            print(char)
            alpha_list[ord(char) - ord("a")] += 1
            
        print(alpha_list)
        
        coded_str = " ".join(map(str,alpha_list))
        
        d[coded_str].append(word)
    print(d)
    return list(dict(d).values())
        
        
print(group_anagram(["bdddddddddd","bbbbbbbbbbc"]))
    