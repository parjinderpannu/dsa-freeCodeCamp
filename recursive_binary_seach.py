def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint],target)
            

def verify(result):
    if result == False:
        print("Target is not present in list")
    else:
        print("Target is present in the list")

l1 = [1,2,3,4,5,6,7,8,9,10]
t1 = 12
result = recursive_binary_search(l1,t1)
verify(result)