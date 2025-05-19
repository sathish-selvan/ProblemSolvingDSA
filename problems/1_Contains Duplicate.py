# return True if have duplicates else False

def check_duplicates(arr:list):
    
    hashset = set()
    
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False


print(check_duplicates([1,2,3,4,3,6]))