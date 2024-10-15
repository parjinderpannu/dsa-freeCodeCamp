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

def recursive_binary_tree(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint]==target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_tree(list[midpoint+1:],target)
        else:
            return recursive_binary_tree(list[:midpoint],target)


# l1 = [1,2,3,4,5,6,7,8,9,10]
l1 = []
target = 11

# result = binary_search(l1, target)
r2 = recursive_binary_tree(l1, target)

if r2:
    print("Target present")
else:
    print("Target is not present")

# if result is not None:
#     print("Index of target: ",target," in list: ",l1," is = ",binary_search(l1,target))
# else:
#     print(target," is not present in list = ", l1)