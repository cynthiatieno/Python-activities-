def find_primes_in_range(start, end):
    primes = []
    
    for num in range(start, end + 1):
        if num > 1: #  prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    
    return primes


start = 50
end = 100
prime_numbers = find_primes_in_range(start, end)
print("Prime numbers between", start, "and", end, "are:", prime_numbers)
