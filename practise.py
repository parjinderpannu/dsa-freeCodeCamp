def binary_search(list, target):
    first, last = 0, len(list)-1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint]<target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None


l1 = [1,2,3,4,5,6,7,8,9,10]
target = 10

result = binary_search(l1, target)

if result is not None:
    print("Index of target: ",target," in list: ",l1," is = ",binary_search(l1,target))
else:
    print(target," is not present in list = ", l1)