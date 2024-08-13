#Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number


# Initialize the previous number
previous = 0

# Iterate the first 10 numbers
for i in range(1, 11):
    # Print the sum of the current and previous number
    print(f"Current: {i}, Previous: {previous}, Sum: {i + previous}")

    # Update the previous number for the next iteration
    previous = i