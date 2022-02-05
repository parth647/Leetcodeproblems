def insertion_sort(arr):
    if(len(arr)<=1):
        return arr
    else: #taking new element and inserting it
        check_ele = 0
        for i in range(1,len(arr)):
            if(arr[i]>arr[check_ele]):#means new element can be trivially added
                check_ele+=1
                continue
            else:
                idx = i
                while(check_ele>=0):
                    if(arr[idx]<arr[check_ele]):
                        temp = arr[idx]
                        arr[idx] = arr[check_ele]
                        arr[check_ele] = temp
                    else:
                        break
                    idx-=1
                    check_ele-=1
                check_ele = i

                
    return arr

print("Running File now : \n",insertion_sort([1,2,3,4,5]))
print("Running File now : \n",insertion_sort([5,4,3,2,1]))
            