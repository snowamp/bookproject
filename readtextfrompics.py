###########################################
#Analyze the pictures' word from Dr. Seuss
#Apply Ocr technology to these pictures
###########################################

import sys
from PIL import Image
import pytesseract
import os
import string

def obtain_text(path):
	filelist = []
	text = []
	printable = set(string.printable)
	for filename in os.listdir(path):
		if '.jpg' in filename or 'jpeg' in filename or 'png' in filename:
			substring = pytesseract.image_to_string(Image.open(os.path.join(path,filename)))
			string_update = ''.join(filter(lambda x: x in printable, substring))
			filelist.append(filename)
			text.append(string_update)

	output_text(filelist, text, path)

def output_text(filelist, text, path):
	piccontent = 'picscontent.txt'
	f = open(os.path.join(path, piccontent), 'w+')

	for i in range(len(text)):
		f.write(filelist[i] + '\n')
		f.write(text[i])
		f.write('\n')
	f.close()
	print("Done")
def main():
	obtain_text('/Users/yanchunyang/Documents/highschools/scripts/millioncats/')

if __name__ == '__main__':
	main()


