#Write a program where user enter the integer number n and generate the binary number reprsentation of n digits width.
# Your task is to count those binary reprsentation's out of all the generated ones in which binary number string has consecutive 1's

n = int(input())

# Initialize the count variable.
count = 0

# Iterate over the binary representations of n.
for i in range(1 << n):
  # Convert the integer i to binary.
  binary = bin(i)[2:]

  # Check if the binary representation has consecutive 1s.
  if "11" in binary:
    count += 1

# Print the result.
print(count)
