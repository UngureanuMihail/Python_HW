# Write a program that will convert a decimal number to binary.
# Example:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input('Introduce your number : '))
bin_number = bin(decimal_number)
myBin = bin_number.replace('0b', '')
print(f'Your decimal number - {decimal_number} converted to binary is : {myBin}')
