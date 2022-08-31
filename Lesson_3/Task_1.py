# A program that will find the sum of the list items standing in an odd position.
# Example: [2, 3, 5, 9, 3] -> result: 12
my_list = [1, 10, 2, 4, 1, 6]
l = []
for i in range(len(my_list)):
    if i % 2 != 0:
        l.append(my_list[i])
print(f'Summ of items standing in an odd position is : {(sum(l))}')

# v2
list_one = [1, 10, 2, 4, 1, 6]
print(f'Summ of items standing in an odd position is : {(sum(list_one[1::2]))}')
