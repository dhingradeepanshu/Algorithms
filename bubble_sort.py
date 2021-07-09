def bubble_sort(a,n):
    
    while(True):
        
        flag=True
        
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                flag=False
        
        if flag:
            break


a=[40,70,50,60,20,10,75,90,1]
n=len(a)
bubble_sort(a,n)
print(a)

# a[i] and a[i+1] are compared till then end and swapped
# after each iteration largest element reaches the end of array

# Time Complexity
# Best O(n)
# Worst O(n^2)