"""
Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
"""
def sum_of_digits(num):
    sum=0
    while(num!=0):
        sum=sum+int(num%10)
        num=num/10
    return sum

num = int(input("Enter +ve Integer: "))

if(num>=1001 and num<=22000):
    print(sum_of_digits(num))
else:
    print("Not in Excepted Range")