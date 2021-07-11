def heapify(a,ub,i):
    left = 2*i+1
    right = 2*i+2
    largest=i
    if left<=ub and a[left]>a[largest]:
        largest=left
    if right<=ub and a[right]>a[largest]:
        largest=right
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,ub,largest)

def heap_sort(a):
    n=len(a)
    # Leaf nodes are from n//2 to n-1, so we need to apply heapify to non leaf starting from n//2 -1 till 0 i.e. root node
    # So this is building the max heap
    for i in range(n//2 - 1 , -1, -1):
        heapify(a,n-1,i)
    
    # Now we start deleting nodes from max heap
    # Only root node can be deleted in heap which is replaced with the last leaf node
    for i in range(n-1,-1,-1):
        a[0],a[i]=a[i],a[0]
        #upper bound is reduced because deleted root node is at the last of array and not part of the heap need not be checked
        heapify(a,i-1,0)


a=[5,6,20,10,9,2,4,8]
heap_sort(a)
print(a)

#First build a max heap
#Then delete nodes from max heap (remember only root node can be deleted and it is replaced with last leaf node, now again check if it becomes a max heap or not)

#Time Complexity
# Best O(n*logn)
# Worst O(n*logn)