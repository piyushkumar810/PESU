# 6. Move all zeros to the end
def move_all_zeros(arr):
    if(len(arr)==0):
        return []
    
    else:
        non_zero=[]
        zero_count=0
        for i in range(len(arr)):
            if(arr[i]==0):
                zero_count +=1
            else:
                non_zero.append(arr[i])
        
        result=non_zero + [0]*zero_count
        return result


arr=[10,30,0,40,2,0,0,23,0,0,24]
print(move_all_zeros(arr))



# ------------------ best approach
def move_all_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr

arr=[10,30,0,40,2,0,0,23,0,0,24]
print(move_all_zeros(arr))
