import random
 
def klargest(lst, k):
    
    # if length is smaller that largest number
    if len(lst) < k:
        return -1
 
    copy_list = lst.copy()
    
    # calculation of kth largest
    while len(copy_list) > 0:

        left = []
        right = []
 
        random_pivot = copy_list[0]
 
        #appending left and right lists
        for i in copy_list:
            if i < random_pivot:
                left.append(i)
            if i > random_pivot:
                right.append(i)
 
        # checking for kth largest element
        if len(left) == k-1:
            return random_pivot
 
        # if kth largest element is not in left list
        elif len(left) < k:
            copy_list = right
            n = len(left) + 1
            k = k - n
 
        # if kth largest element is in left list
        else :
            copy_list = left
 
    return -1
 
 
 
# making array of random numberswith 10 elements
l = random.sample(range(100), 10)
 
largest = klargest(l.copy(), 5)
 
if largest == -1:
    print("No such element")
else:
    print("Largest element is: ", largest)