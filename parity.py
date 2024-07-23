def even(number):
    return(f"your numer {number} is even")

def odd(number):
    return(f"your numer {number} is odd")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(even(number))
    
elif number %2 != 0:
    print(odd(number))