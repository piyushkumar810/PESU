'''
Write a function calc_sum_avg(numbers) that takes a list of integers and returns both the sum and average.
'''

def calc_sum_avg(num_list):
    total_sum_value=0
    for each_num in num_list:
        total_sum_value=total_sum_value+each_num
        
    if len(num_list)>0:
        average_value_result=total_sum_value/len(num_list)
        
    else:
        average_value_result=0
        
    return total_sum_value,average_value_result
    
    
number_data=[10,20,30,40,50]
sum_result,avg_result=calc_sum_avg(number_data)
print("sum: ", sum_result)
print("average: ",avg_result)
    