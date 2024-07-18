#exceptation handling
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("Division performed successfully")
except ZeroDivisionError:
    print("it s errror")
print('outside try except block')

###################################### 
#handling exception without naming
try:
    nume=55
    deno=int(input("Enter denominator"))
    quotient=(nume/denom)
    print("division performed successfully")
except ValueError:
    print("Enter only integers")
except:
    print("oops some exception raised")
    
################################
#handling exception using try...except...else
try:
    nume=50
    deno=int(input("Enter denominator"))
    quotient=(nume/deno)
    print("division performed successfully")
except ZeroDivisionError:
    print("Denominator as zero is not allowed")
except ValueError:
    print("Enter only integers")
else:
    print("the result of division operation is ",quotient)
    
###################################
#handling exception using try...except...else...finally
try:
    nume=50
    deno=int(input("Enter denominator"))
    quotient=(nume/deno)
    print("division performed successfully")
except ZeroDivisionError:
    print("Denominator as zero is not allowed")
except ValueError:
    print("Enter only integers")
else:
    print("the result of division operation is ",quotient)
finally:
    print("OVER AND OUT")
    