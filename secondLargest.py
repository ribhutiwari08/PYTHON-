def second_largest(numbers):
    unique_numbers = list(set(numbers))  
    if len(unique_numbers) < 2:
        return None 
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = second_largest(numbers)

if result:
    print(f"The second largest number is: {result}")
else:
    print("The list doesn't have a second largest number.")
