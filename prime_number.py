def prime_number(number):
    count = 0
    if number == 1:
        return "It is a prime number"
            
    for numbers in range(1, number):
        hola =  number % numbers
        if hola == 0:
            count += 1
    if count >=2:
        return "It is not a prime number"
    else:
        return "It is a prime number"
            

print("""
    This program will help you to check
    if one number is a prime number or not.
    Let's start
    """)

check_number = int(input("Please enter a number: "))

primenumber_check = prime_number(check_number)

print(primenumber_check)



