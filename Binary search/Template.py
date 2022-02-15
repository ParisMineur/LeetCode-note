## template for binary search

left, right = 0, len(array) - 1

while left <= right:
    mid = (left + right)/2
    if array[mid] == target:
        ## find target
        bresk or return result
    elif array[mid]<target:
        left = mid +1
    elif array[mid]>target:
        right = mid - 1
  
