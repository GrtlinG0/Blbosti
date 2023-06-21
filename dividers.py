def find_dividers(number):
    dividers = []
    for i in range(1, number + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers

# Taking input from the user
num = int(input("Enter a number: "))

# Finding dividers
result = find_dividers(num)

# Displaying the dividers
print("Dividers of", num, "are:", result)