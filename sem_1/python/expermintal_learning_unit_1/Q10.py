'''
Define is_leap(year) that returns True if the year is a leap year
. Loop through 2000–2025 and print leap years.
'''

def leap_year(year):
    if(year%400 == 0)or(year%4==0 and year%100!=0):
        return True
    else:
        return False
        
for i in range(2000,2026):
    if leap_year(i):
        print(i)