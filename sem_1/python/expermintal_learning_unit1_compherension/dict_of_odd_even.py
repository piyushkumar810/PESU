# Generate a dictionary where keys are numbers from 1 to 10 and values are even/odd labels.

dict_of_odd_even={key:("even" if key%2==0 else "odd") for key in range(1,11)}
print(dict_of_odd_even)