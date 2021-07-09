def partition(a,lb,ub):
    #lb is lower bound and ub is upper bound
    pivot=a[lb]
    start=lb
    end=ub
    while(start<end):

        while pivot>=a[start] and start<len(a):
            start+=1
        while pivot<a[end]:
            end-=1
        if start<end:
            a[start],a[end]=a[end],a[start]
    
    a[lb],a[end]=a[end],a[lb]
    return end


def quicksort(a,lb,ub):
    if (lb<ub):
        loc = partition(a,lb,ub)
        quicksort(a,lb,loc-1)
        quicksort(a,loc+1,ub)


a=[10,15,1,2,9,16,11]
n=len(a)
quicksort(a,0,n-1)
print(a)




# Select a pivot in the array (In this case 1st element is considered as pivot)
# Two functions in quick sort, one is partition and other to implement quick sort
# Partition is done like left side becomes less than pivot and right side is greater than pivot

#Time Complexity
# Best case O(n*log(n))
# Worst case O(n^2)