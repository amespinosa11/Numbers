def get_info_numbers(numbers):
	if numbers is "":
		amount_numbers = 0
		min_number = 0

	else:
		num = numbers.split(",")
		numbers_as_list = list(num)
		amount_numbers = len(numbers_as_list)

	result = [amount_numbers,min_number]
	return result
