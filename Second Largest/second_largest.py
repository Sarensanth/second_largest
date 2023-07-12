def second_largest(array):
    maxi=-float('inf')
    for i in array:
        if maxi<i:
            maxi=i

    count=0
    for i in array:
        if i==maxi:
            count+=1
    
    if len(array)-count!=0:
        return 1
    return -1

array=list(map(int,input().split()))
print(second_largest(array))


    