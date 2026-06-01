
def LargstElement(arr1):
    if(len(arr1)==0):
        return None
    
    else:
        largest1=arr1[0]
        for i in range (len(arr1)-1):
            if(largest1<arr1[i+1]):
                largest1=arr1[i]
        
        return largest1


arr1=[10,645,94,20,30,45,200,100]
print(LargstElement(arr1))