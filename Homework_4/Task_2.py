# Write a program that outputs a list of non-repeating elements of the original sequence

num_list = [x for x in range(13)]


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    for number in set(numbers):
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(f'Your list of non-repeating elements of the original sequence is : {get_unique_numbers(num_list)}')
