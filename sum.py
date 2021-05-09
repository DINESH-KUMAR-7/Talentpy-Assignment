from cache_decorator import Cache
"""
Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
"""
@Cache()#Cache decorator used to stor the recent values.
def sum_of_digits():
    sum =0
    initial = 1001

    for initial in range(22000):
        while(initial!=0):
            sum=sum+int(initial%10)
            initial = initial/10
    return sum

print(sum_of_digits())
#Without Cache <Execution Time: 4.79s>
#With Cache <Execution Time: 1.77s>
