"""
John would like to create a function to check whether given number is
positive or negative or neutral. Help him to write an independent function
and pass different inputs to the function and check its behaviour
"""
def behaviour_check(val):
    if(val<0):
        return "Negative"
    elif(val==0):
        return "Zero"
    else:
        return "Positive"

print(behaviour_check(4))
print(behaviour_check(0))
print(behaviour_check(-1))

