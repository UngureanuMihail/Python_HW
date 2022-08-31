# Write a program that outputs a list of non-repeating elements of the original sequence

num_list = [1, 2, 3, 5, 1, 5, 3, 10]


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(f'Your list of non-repeating elements of the original sequence is : {get_unique_numbers(num_list)}')
