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


pairs = [
    Pair(5, "apple"),
    Pair(2, "banana"),
    Pair(9, "cherry")
]  

print([(p.key, p.value) for p in insertionSort(pairs)[0]])

        
        
        
        