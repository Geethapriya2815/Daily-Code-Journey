
def check_vowel_consonant(ch):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if ch in vowels:
        return "Vowel"
    return "Consonant"

def find_biggest(a, b):
    if a > b:
        return a
    return b

def find_group(n):
    if n > 50:
        return "Above 50"
    elif 40 <= n <= 50:
        return "Between 40 to 50"
    return "Less than 40"

def check_divisibility(n):
    if n % 3 == 0 and n % 4 == 0:
        return "Good Morning"
    elif n % 4 == 0:
        return "Good Afternoon"
    elif n % 3 == 0:
        return "Good Evening"
    return "Good Night"

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'

def calculator(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b if b != 0 else "Undefined"
    return "Invalid Choice"

def find_season(month):
    if 3 <= month <= 5:
        return "Spring Season"
    elif 6 <= month <= 8:
        return "Summer Season"
    elif 9 <= month <= 11:
        return "Autumn Season"
    elif month == 12 or 1 <= month <= 2:
        return "Winter Season"
    return "Invalid Month Entered"

## For Loop Problems

def print_numbers(n):
    for i in range(1, n+1):
        print(i, end=' ')

def sum_natural_numbers(n):
    sum_n = 0
    for i in range(1, n+1):
        sum_n += i
    return sum_n

def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=' ')

## While Loop Problems

def print_numbers_while(n):
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def largest_digit(n):
    max_digit = 0
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
    return max_digit

def count_even_numbers(n):
    count = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            count += 1
        i += 1
    return count

## Do-While Loop Problems (Simulated with While in Python)

def print_numbers_do_while(n):
    i = 1
    while True:
        print(i, end=' ')
        i += 1
        if i > n:
            break

def sum_of_digits_do_while(n):
    total = 0
    while True:
        total += n % 10
        n //= 10
        if n == 0:
            break
    return total

def power_do_while(base, exp):
    result = 1
    while True:
        if exp == 0:
            break
        result *= base
        exp -= 1
    return result

## Other Programs

def is_prime_number(n):
    return is_prime(n)

def factorial_method(n):
    return factorial(n)

def fibonacci_method(n):
    fibonacci(n)

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_armstrong(n):
    original, sum_n, temp = n, 0, n
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    temp = n
    while temp > 0:
        sum_n += (temp % 10) ** digits
        temp //= 10
    return sum_n == original

def is_perfect(n):
    sum_n = 0
    for i in range(1, n):
        if n % i == 0:
            sum_n += i
    return sum_n == n
