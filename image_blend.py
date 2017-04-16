################################################
#Try to blend the image 
# Make image as background and draw lines on it
#
#################################################

from PIL import Image
import os


def image_blend(path):
	images = []
	for filename in os.listdir(path):
		if 'png' in filename or 'jpg' in filename or 'jpeg' in filename:
			images.append(filename)

	for image in images:
		im1 = Image.open(os.path.join(path, image))
		im2 = im1.convert('RGBA')
		im3 = Image.new('RGBA', im1.size, (255, 255, 255))
		alpha = 0.7
		out = Image.blend(im2, im3, alpha)
		index = image.find('.')
		newfilename = image[:index]+'_blend'+'.png'
		out.save(os.path.join(path, newfilename), "png")

def main():
	image_blend('/Users/yanchunyang/Documents/highschools/scripts/snow/')

if __name__ == '__main__':
	main()
