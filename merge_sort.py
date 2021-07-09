def merge(a,lb,mid,ub):
    arr=[0 for i in range(ub-lb+1)]
    k=0
    i=lb
    j=mid+1
    while(i<=mid and j<=ub):
        if a[i]<=a[j]:
            arr[k]=a[i]
            i+=1
            k+=1
        else:
            arr[k]=a[j]
            j+=1
            k+=1
    if i>mid:
        while(j<=ub):
            arr[k]=a[j]
            j+=1
            k+=1
    if j>ub:
        while(i<=mid):
            arr[k]=a[i]
            i+=1
            k+=1
    i=0
    for k in range(lb,ub+1):
        a[k]=arr[i]
        i+=1

def mergesort(a,start,end):
    if start<end:
        mid=int((start+end)/2)
        mergesort(a,start,mid)
        mergesort(a,mid+1,end)
        merge(a,start,mid,end)

a=[12, 11, 13, 5, 6, 7]
n=len(a)
mergesort(a,0,n-1)
print(a)


# Two functions mergesort->to recursively divide array and merge->to merge two sorted arrays
# Divide array recursively uptill when there is one element and then call merge

#Time Complexity
# Best case O(n*log(n))
# Worst case O(n*log(n))