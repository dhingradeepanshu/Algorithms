def binary_search(a,elem,l,r):
    while(l<=r):
        mid = int((l+r)/2)
        if a[mid]==elem:
            print("Element found at index {}".format(mid))
            return True
        elif a[mid]>elem:
            r=mid-1
        else:
            l=mid+1

    print("Element not found")
    return False






a=[10,20,30,40,50,60,70,80,90,100]
n=len(a)
elem=30
left=0
right=n-1
binary_search(a,elem,left,right)