def factorial (n): 
    if n == 0:
        return 1
        else:
            return n * fctorial(n - 1)
            
number = 5
result = fctorial(number)
print(f"The factorial of {number} is {result}.")
