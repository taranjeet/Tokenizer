#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
class Tokenizer():

	'''class that implements a basic tokenizer for Hindi language'''

	def __init__(self,text):
		'''sets the data members
			text contains the input text
			tokens : a list containing all the tokens
			words : a list containing all the words
			sentences : a list containing all the sentences
		'''
		self.text=text
		self.tokens=[]
		self.words=[]
		self.sentences=[]

	def len_text(self):
		'''return the len of the text'''
		return len(self.text)

	def words_count(self):
		'''return the number of the words'''
		return len(self.words)

	def tokens_count(self):
		'''return the number of tokens'''
		return len(self.tokens)

	def sentence_count(self):
		'''return the number of sentences'''
		return len(self.sentences)

	def unique_tokens_count(self):
		'''returns the number of unique tokens'''
		return len(set(self.tokens))

	def generate_sentences(self):
		'''generates a list of sentences'''
		text=self.text
		self.sentences=text.split(u"।")

	def generate_words(self):
		'''generate words from list of sentences'''
		sentences_list=self.sentences
		words=[]
		for each in sentences_list:
			word_list=each.split(' ')
			words=words+word_list
		self.words=words

	def generate_tokens(self):
		'''generates tokens'''
		self.generate_words()
		##self.tokens=set(self.words)
		self.tokens=self.words

	def remove_only_space_words(self):
		'''remove tokens containing only spaces'''
		words=filter(lambda tok: tok.strip(),self.words)
		self.words=words
		##self.tokens=set(self.words)
		self.tokens=self.words


	def hyphenated_tokens(self):
		'''removes tokens containing replicating words'''
		for each in self.words:
			if '-' in each:
				tok=each.split('-')
				self.words.remove(each)
				self.words.append(tok[0])
				#if tok[0]!=tok[1]:
				self.words.append(tok[1])
		##self.tokens=set(self.words)
		self.tokens=self.words

	def generate_stem_word(self):
		'''returns a dictionary of stem words for each token'''
		suffixes = {
    				1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    				2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    				3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    				4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    				5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
					}
		stem_word={}
		for each_token in self.tokens:
			#print type(each_token)
			temp=self.stem_word(each_token)
			#print temp
			stem_word[each_token]=temp
			
		return stem_word


	def stem_word(self,word):
		suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
}
		for L in 5, 4, 3, 2, 1:
			if len(word) > L + 1:
				for suf in suffixes[L]:
					#print type(suf),type(word),word,suf
					if word.endswith(suf):
						#print 'h'
						return word[:-L]
		return word

	def concordance(self,word):
		self.generate_sentences()
		sentence=self.sentences
		concordance_sent=[]
		for each in sentence:
			#print each
			each=each.encode('utf-8')
			if word in each:
				#print 'h'
				concordance_sent.append(each)
		return concordance_sent

	def remove_stop_words(self):
		f=codecs.open("rss.txt",encoding='utf-8')
		stopwords=[x.strip() for x in f.readlines()]
		tokens=[i for i in self.tokens if unicode(i) not in stopwords]
		self.tokens=tokens
		#return stopwords[61]

	def make_frequency(self):
		freq={}
		for each in self.tokens:
			freq[each]=self.words.count(each)
		return freq

		


def print_sentence(sent):
	print (sent.decode('utf-8'))


main_tokens=[]

for ii in range(1,6):


	fname='sports'+str(ii)
	f=codecs.open(fname+'.txt',encoding='utf-8')
	strings=f.read()
	#print type(strings)

	t=Tokenizer(strings)
	t.generate_sentences()
	sen=t.sentences

	# for i in sen:
	# 	print i
	t.generate_tokens()
	tok=t.tokens
	t.remove_only_space_words()
	t.hyphenated_tokens()
	ttok=list(t.tokens)
	f=open(fname+'token.txt','w')
	for i in ttok:
		f.write(i.encode('utf-8')+'\n')
		#print i.encode('utf-8')
	#print ttok[16]
	f.close()
	#print len(ttok),len(sen)
	s=t.generate_stem_word()
	#print 'generating stem words'
	f=open(fname+'stem.txt','w')
	# for i in s.keys():
	# 	if s[i]:
	# 		f.write(i.encode('utf-8')+'->'+s[i].encode('utf-8')+'\n')
	# 		#print i.encode('utf-8'),' - ', s[i].encode('utf-8')
	stem_words=[]
	for i in t.tokens:
		f.write(i.encode('utf-8')+'->'+s[i].encode('utf-8')+'\n')
		stem_words.append(s[i])

	f.close()

	f=open(fname+'stem_words.txt','w')
	for i in stem_words:
		f.write(i.encode('utf-8')+'\n')
	# w='काफी'
	# x=t.concordance(w)
	# for i in x:
	# # 	print_sentence(i)
	t.remove_stop_words()
	#print unicode(z)==unicode(ttok[16]),ttok[16],z
	f=open(fname+'stop.txt','w')
	ttok=t.tokens
	#print len(set(ttok))
	for i in ttok:
		f.write(i.encode('utf-8')+'\n')
		main_tokens.append(i)
	f.close()






temp_tokens=main_tokens
f=open('map_index.txt','w')
temp=0
fr={}
tok=set(main_tokens)
for i in tok:
	ch=temp_tokens.count(i)
	#print i,ch
	#print ch
	fr[i.encode('utf-8')]=ch
	f.write(i.encode('utf-8')+'->'+str(ch)+'\n')
	# dr[te]
	# temp+=1
	# fr[temp]=i
	# temp+=1

# for i in fr.keys():
# 	if fr[i]:
# 		f.write(i.encode('utf-8')+'->'+str(i)+'\n')

f.close()

# print fr["कमरों"]
# fre=t.make_frequency()
# f=open('freq.txt','w')
# for i in fre.keys():
# 	f.write(i.encode('utf-8')+'->'+str(fre[i])+'\n')
# f.close()






