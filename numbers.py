def get_info_numbers(numbers):
	if numbers is "":
		amount_numbers = 0
		min_number = 0
		max_number = 0
		average = 0

	else:
		num = numbers.split(",")
		amount_numbers = len(list(num))
		list_as_num = []
		for i in list(num):
			list_as_num.append(int(i))

		min_number = int(min(list_as_num))
		max_number = int(max(list_as_num))
		average = float(sum(list_as_num)/amount_numbers)

	result = [amount_numbers,min_number,max_number,average]
	return result


