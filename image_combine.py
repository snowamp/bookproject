#######################################################################
'''
list_im = []
imgs = [Image.open(i) for i in list_im]

min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imags))

imgs_comb = Image.fromarray(imags_comb)
imgs_comb.save('combine.jpg')

imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('combine_vertical.jpg')
'''
##########################################################################
import numpy as np
from PIL import Image
import os

def readfiles(path):
	list_im = []
	order_list = []
	for filename in os.listdir(path):
		if 'png' in filename or 'jpg' in filename or 'jpeg' in filename:
			list_im.append(os.path.join(path, filename))
			index = filename.find('.')
			order_list.append(int(filename[:index]))

	orders = np.array(order_list)
	images = np.array(list_im)

	inds = orders.argsort()
	images_order = images[inds]

	
	combine_two_horizon(images_order, path)
	#combine_two_vertical(images_order,path)

def combine_four(list_im, path):
	imgs = []
	for item in list_im:
		temp_img = Image.open(item)
		width = temp_img.size[0]
		height = temp_img.size[1]
		temp = temp_img.crop((0, 2, width, height-2))
		imgs.append(temp)
	min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

	size = 4
	i = 0
	left = len(imgs) % 4

	for i in range(0, 4 - left):
		imgs.append(Image.new('RGB', min_shape, "white"))
	print(len(imgs))

	i = 0
	while i < len(imgs) - 1:
		result = Image.new("RGB", (min_shape[0]*2, min_shape[1]*2))
		w, h = min_shape
		result.paste(imgs[i], (0, 0, w, h))
		result.paste(imgs[i+1], (w, 0, w+w, h ))
		result.paste(imgs[i+2], (0, h, w, h+h))
		result.paste(imgs[i+3], (w, h, w+w, h+h))
		result.resize(min_shape).save('combine_' + str(i) + '.jpg')
		i = i+4
	'''
	while i < len(imgs)-1:
		imgs_h_1 = np.vstack((imgs[i].resize(min_shape), imgs[i+2].resize(min_shape)))
		imgs_h_1 = Image.fromarray(imgs_h_1)
		imgs_h_1.save('temp1.jpg')
		imgs_h_2 = np.vstack((imgs[i+1].resize(min_shape), imgs[i+3].resize(min_shape)))
		imgs_h_2 = Image.fromarray(imgs_h_2)
		imgs_h_2.save('temp2.jpg')
		img_hv = np.hstack((Image.open('temp1.jpg'), Image.open('temp2.jpg')))
		img_hv = Image.fromarray(img_hv)
		img_hv.resize(min_shape).save('combine_' + str(i) + '.jpg')

		i = i + 4
	'''

def combine_two_vertical(list_im, path):
	imgs = []
	for item in list_im:
		temp_img = Image.open(item)
		width = temp_img.size[0]
		height = temp_img.size[1]
		temp = temp_img.crop((0, 2, width, height-2))
		imgs.append(temp)
	min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

	size = 2
	i = 0
	left = len(imgs) % 2

	for i in range(0, left):
		imgs.append(Image.new('RGB', min_shape, "white"))
	print(len(imgs))

	i = 0
	while i < len(imgs) - 1:
		result = Image.new("RGB", (min_shape[0], min_shape[1]*2))
		w, h = min_shape
		result.paste(imgs[i].resize(min_shape), (0, 0, w, h))
		result.paste(imgs[i+1].resize(min_shape), (0, h, w, h+h))
		result.save(os.path.join(path, 'combine_' + str(i) + '.jpg'))
		i = i+2

def combine_two_horizon(list_im, path):
	imgs = []
	for item in list_im:
		temp_img = Image.open(item)
		width = temp_img.size[0]
		height = temp_img.size[1]
		temp = temp_img.crop((0, 2, width, height-2))
		imgs.append(temp)
	min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

	size = 2
	i = 0
	left = len(imgs) % 2

	for i in range(0, left):
		imgs.append(Image.new('RGB', min_shape, "white"))
	print(len(imgs))

	i = 0
	while i < len(imgs) - 1:
		result = Image.new("RGB", (min_shape[0]*2, min_shape[1]))
		w, h = min_shape
		result.paste(imgs[i].resize(min_shape), (0, 0, w, h))
		result.paste(imgs[i+1].resize(min_shape), (w, 0, w+w, h ))
		result.save(os.path.join(path, 'combine_' + str(i) + '.jpg'))
		i = i+2


def main():
	readfiles('../ifgiveamouseacookie/cookie/')

if __name__ == '__main__':
	main()


