#!/usr/bin/python
# -*- coding: utf-8 -*-

def wordsCount(words):
	return len(words)

def tokensCount(tokens):
	return len(tokens)

fileName='text1.txt'
inputFile=open(fileName)
text=inputFile.read()


text=text.decode('utf-8')
sentences=text.split(u"।")
words=[]

for eachSentence in sentences:
	#print (i)
	token=eachSentence.split(' ')
	words = words + token

for each in words:
	if '-' in each:
		temp=each.split('-')
		words.remove(each)
		words.append(temp[0])
		words.append(temp[1])

#removing only spaces words from tokens list
words=filter(lambda tok: tok.strip(),words)
#words=filter(None,words)
wordsNo=wordsCount(words)
print 'Total words : %d' % (wordsNo)
tokens=set(words)

tokensNo=tokensCount(tokens)
print 'Total tokens : %d' % (tokensNo)

outFileName=fileName.split('.')[0]
outFileName = outFileName+'Tokens'
outputFile=open(outFileName,'wb')
for each in tokens:
	outputFile.write(each.encode('utf-8')+'\n')

outputFile.close()
inputFile.close()