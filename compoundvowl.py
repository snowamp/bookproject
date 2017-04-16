import sys
import os
from collections import defaultdict
import re

compound = ['ee', 'ea', 'ie', 'ei', 'er', 'ur', 'ir', 'or', 'ar', 'ear', 'ai', 'ay', 'ey', 'uy', 'ou', 'ow', 'aw', 'au','ought', 'al', 'oi'
'ew', 'eu', 'ue', 'ui']
single = [ 'e e', 'a e', 'i e', 'o e', 'u e']

vowelcompound = defaultdict(list)

vowel = {'i:':['ee', 'ea', 'ie', 'ei', 'e e'], '&r':['er', 'ur', 'ir', 'or', 'ar', 'ear'], 'e':['ea', 'e e'], 'ei':['ai', 'ay', 'ei', 'ey', 'ea', 'a e'],
'a:':['ar'], 'ai':['ie', 'uy'], 'au':['ou', 'ow'], 'o:':['aw', 'au', 'ought', 'al', 'o e'], 'oi':['oi', 'oy'], 'ou':['oa', 'ow'],
'yu:':['ew', 'eu', 'ue', 'ui','ou'], 'u':['oo', 'ou', 'o e', 'u e']}


words = defaultdict(list)

def find_words(words_list):
	for w in words_list:
		for item in compound:
			if item in w:
				words[item].append(w)
		for item in single:
			p = re.compile(item[0]+'[b-z]'+item[-1])
			if p.search(w):
				words[item].append(w)


	for key in vowel:
		for item in vowel[key]:
			vowelcompound[item].append(key)

	with open('vowelwords.txt', 'w+') as g:
		for key in words.keys():
			for item in words[key]:
				g.write(key+'\t')
				for j in vowelcompound[key]:
					g.write(j+'\t')
				g.write(item+'\n')




			

