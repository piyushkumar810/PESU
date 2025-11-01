# Generate a list of cubes of odd numbers from 1 to 20 using List Comprehension
list_of_cubes_of_odd=[cube**3 for cube in range(1,21) if(cube%2==1)]
print(list_of_cubes_of_odd)
