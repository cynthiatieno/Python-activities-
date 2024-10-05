def filter_even_numbers(numbers):
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

input_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
even_numbers = filter_even_numbers(input_list)
print("Even numbers:", even_numbers)
