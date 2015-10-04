#!/usr/bin/env python
def next_perm(arr,length):    
    k,l = -1,-1
    for i in range(length-2,-1,-1):
        if arr[i] < arr[i+1]:
            k = i
            break
    if k == -1:
        print('No next permutation!')    
        return 
    for i in range(length-1,-1,-1):
        if arr[i] > arr[k]:
            l = i
            break
    temp = arr[l]
    arr[l] = arr[k]
    arr[k] = temp
    unchange_part = arr[:k+1]
    reverse_part = list(reversed(arr[k+1:]))
    arr = unchange_part + reverse_part
    print(arr)        #print next permutation

########### DEMO #############
ls = ['A','B','C','D']
next_perm(ls,len(ls))
