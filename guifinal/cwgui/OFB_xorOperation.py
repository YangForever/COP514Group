import numpy as np

def mod_operation(x,y):  #mod operation
	return (x+y)%2

def xorOperation(matrixA,matrixB):
	temp_matrix = np.arange(len(matrixA)*len(matrixA))
	temp_matrix = temp_matrix.reshape(len(matrixA),len(matrixA))
	for i in xrange(0,len(matrixA)):
		for j in xrange(0,len(matrixA)):
			temp_matrix[i][j] = mod_operation(matrixA[i][j],matrixB[i][j])

	return temp_matrix


	