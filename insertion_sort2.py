class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        
def insertionSort(pairs):
    n = len(pairs)
    result = []
    for i in range(n):
        j = i - 1 
        while j >= 0 and pairs[j].key > pairs[j+1].key:
            pairs[j], pairs[j+1] = pairs[j+1], pairs[j] 
            j -= 1
    result.append(pairs[:]) 
    return result 

pairs = [(5, "apple"), (2, "banana"),(9, "cherry")]     

print(insertionSort(pairs))  
        
        
        
        