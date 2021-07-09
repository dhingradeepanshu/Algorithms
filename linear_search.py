def linear_search(a,n,elem):
    found=False
    for i in range(n):
        if a[i]==elem:
            print("Element found at index {}".format(i))
            found=True
            break
    if found==False:
        print("No Element Found")

a=[10,20,30,40,50,60,70,80,90,100]
n=len(a)
elem=35
linear_search(a,n,elem)


