from PIL import Image
import numpy as np
def readPic(filename):
	im = Image.open(str(filename))
	# im.show()
	pix = im.load()
	x = im.size[0]
	y = im.size[1]
	temp = []
	for i in range(x):
		for j in range(y):
			temp.append(pix[j,i])
	return ''.join(s for s in str(temp).split(', '))

	# temp = np.asarray(temp)
	# temp.resize(200, 200)
	# print len(temp)
	# img = Image.fromarray(temp)
	# img.show()

