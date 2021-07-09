def selection_sort(a,n):

    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if a[mini]>a[j]:
                mini=j
        a[i],a[mini]=a[mini],a[i]

a=[64, 25, 12, 22, 11]
n=len(a)
selection_sort(a,n)
print(a)


# Array divided into [  Sorted | Unsorted ]
# At the beginning nothing is considered sorted (All the elements are in unsorted part)
# Find min element in unsorted array and replace it with the first element of unsorted part


# Time Complexity
# Best O(n^2)
# Worst O(n^2)