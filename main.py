def findDoubles(x):
   

    for i in range (0, len(x) - 1):
        if x[i] == x[i + 1]: 
            return True
    return False
print (findDoubles("madagascar"))