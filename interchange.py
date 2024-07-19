def swap(n):
    size=len(n)
    temp=n[0]
    n[0]=n[size-1]
    n[size-1]=temp
 
    return n

n=[12,35,9,56,24]
print(swap(n))    