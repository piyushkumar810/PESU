# sum of even numbers in your list

def sum_of_evens(args):
    sum=0
    for i in args:
        if(i % 2==0):
            sum=sum+i
    return sum

print(sum_of_evens([2,4,6,7,9,3,8,10,12]))


# count the vowels
print()
def count_the_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

print(count_the_vowels('isstring'))

