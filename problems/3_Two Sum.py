def two_sum(arr: list , output:int):
    hashmap = {}
    
    for i,j in enumerate(arr):
        remainder = output - j
        if remainder in hashmap.keys():
            return [hashmap[remainder],i]
        
        hashmap[j] = i
        
    return []

print(two_sum([3,2,4],6))