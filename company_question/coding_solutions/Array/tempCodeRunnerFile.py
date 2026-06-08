
def two_sum(num,n):
    l_n=len(num)

    for i in range(l_n):
        for j in range(i+1,l_n):
            if(num[i]+num[j]==n):
                return [i,j]

num=[10,20,4,20,3,4,6,3454,64]
targrt=int(input("enter the value : "))
print(two_sum(num,targrt))