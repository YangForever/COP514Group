import numpy as np

def shift_column(matrix):
	temp_matrix = np.arange(64)
	temp_matrix = temp_matrix.reshape(8,8)
	for i in xrange(0,len(matrix)):
		for j in xrange(0,len(matrix)):
			temp_matrix[(i+j)%len(matrix)][j] = matrix[i][j]


	return temp_matrix