import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row = len(a)
	col = len(a[0]) if row > 0 else 0

	if row * col != new_shape[0] * new_shape[1]:
		return a
	
	flattened = []
	for row in a:
		flattened.extend(row)
	
	reshaped_matrix = []
	index = 0
	for i in range(new_shape[0]):
		new_rows = []
		for j in range(new_shape[1]):
			new_rows.append(flattened[index])
			index += 1
		reshaped_matrix.append(new_rows)

	return reshaped_matrix