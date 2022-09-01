

def prime_number(number):
 
    if check_number == 1 or check_number == 2:
            return "It is prime" 
    for numbers in range(2, number):
        if check_number % numbers != 0 and check_number / check_number == 1:
            return "It is prime"
        else:
            return "It is not prime"
     

print("""
    This program will help you to check
    if one number is a prime number or not.
    Let's start
    """)

check_number = int(input("Please enter a number: "))

primenumber_check = prime_number(check_number)

print(primenumber_check)



