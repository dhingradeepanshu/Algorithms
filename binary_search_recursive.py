def binary_search(a,elem,l,r):
    mid = int((l+r)/2)
    if l<=r:
        if a[mid]==elem:
            print("Element found at index {}".format(mid))
            return True
        elif a[mid]>elem:
            return binary_search(a,elem,l,mid-1)
        else:
            return binary_search(a,elem,mid+1,r)
    print("Element not found")
    return False






a=[10,20,30,40,50,60,70,80,90,100]
n=len(a)
elem=80
left=0
right=n-1
binary_search(a,elem,left,right)