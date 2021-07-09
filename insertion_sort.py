def insertion_sort(a,n):
    for i in range(1,n):
        temp = a[i]
        j=i-1
        while(j>=0 and temp<a[j]):
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp


a=[40,70,50,60,20,10,75,90,1]
n=len(a)
insertion_sort(a,n)
print(a)


# Array is divided into [  Sorted | Unsorted  ]
# Starting from index 1 as index 0 is already sorted in itself

# Time Complexity
# Best O(n)
# Worst O(n^2)