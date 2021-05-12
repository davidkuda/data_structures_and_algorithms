def binary_search(ordered_list: list, item_to_find):
	"""Return index of the item in the list.

	If the item is not in the list, this function will return None.
	The algorithm will only work if the passed list is ordered."""

	low = 0
	high = len(ordered_list) - 1

	while low <= high:

		mid = (low + high) / 2
		guess = sorted_list[mid]

		if guess == item_to_find:
			return mid

		if guess > item_to_find:
			high = mid - 1

		else:
			low = mid + 1

	return None