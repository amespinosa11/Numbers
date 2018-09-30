def get_amount_numbers(numbers):
	if numbers is "":
		amount_numbers = 0

	else:
		num = numbers.split(",")
		numbers_as_list = list(num)
		amount_numbers = len(numbers_as_list)

	result = [amount_numbers]
	return result

def get_min_number(numbers):
	amount_numbers = get_amount_numbers(numbers)[0]
	result = [amount_numbers,0]
	return result