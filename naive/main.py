#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs,re
from math import log
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
		self.final=[]

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

	def remove_stop_words(self,inthis):
		f=codecs.open("rss.txt",encoding='utf-8')
		stopwords=[x.strip() for x in f.readlines()]
		tokens=[i for i in inthis if unicode(i) not in stopwords]
		self.final=tokens
		#return stopwords[61]

	def make_frequency(self):
		freq={}
		for each in self.tokens:
			freq[each]=self.words.count(each)
		return freq

		

def size_dict(fr):
	temp=0
	for i in fr.keys():
		temp+=fr[i]
	return temp

def print_sentence(sent):
	print (sent.decode('utf-8'))


def find_prob(fr,word,word_count):
	return 1.0*fr[word]/word_count

#generate sports token
sports_token=[]

for i in range(1,30):
	fname='sports'+str(i)
	f=codecs.open(fname+'.txt',encoding='utf-8')
	strings=f.read()
	#remove numbers
	strings=re.sub(r'(\d+)',r'',strings)
	strings=strings.replace(',','')
	strings=strings.replace('(','')
	strings=strings.replace(')','')
	strings=strings.replace(u"‘‘",'')
	strings=strings.replace(u"’’",'')
	strings=strings.replace("''",'')
	strings=strings.replace(".",'')


	t=Tokenizer(strings)
	t.generate_sentences()
	sen=t.sentences

	t.generate_tokens()
	tok=t.tokens
	t.remove_only_space_words()
	t.hyphenated_tokens()
	ttok=list(t.tokens)
	s=t.generate_stem_word()
	stem_words=[]
	for i in t.tokens:
		stem_words.append(s[i])

	#f.close()

	#f=open(fname+'stem_words.txt','w')
	# for i in stem_words:
	# 	f.write(i.encode('utf-8')+'\n')
	# w='काफी'
	# x=t.concordance(w)
	# for i in x:
	# # 	print_sentence(i)
	t.remove_stop_words(stem_words)
	#print unicode(z)==unicode(ttok[16]),ttok[16],z
	# f=open(fname+'stop.txt','w')
	ttok=t.final
	#print len(set(ttok))
	for i in ttok:
		# f.write(i.encode('utf-8')+'\n')
		sports_token.append(i)

sports_token=filter(lambda a: a!='-',sports_token)
for i in sports_token:
	i=i.strip()

f=open(fname+'_map_index.txt','w')
temp_tokens=sports_token
temp=0
sfr={}
tok=set(sports_token)
sports_data_count=0
for i in tok:
	if i:
		ch=temp_tokens.count(i)
		sfr[i.encode('utf-8')]=ch
for w in sorted(sfr,key=sfr.get,reverse=True):
	#print w,fr[w]
	if w:
		#sports_data_count+=sfr[w]
		f.write(w+' '+str(sfr[w])+'\n')
f.close()
sports_data_count=size_dict(sfr)
print sports_data_count

#generate business token

business_token=[]

for i in range(1,18):
	fname='business'+str(i)
	f=codecs.open(fname+'.txt',encoding='utf-8')
	strings=f.read()
	#remove numbers
	strings=re.sub(r'(\d+)',r'',strings)
	strings=strings.replace(',','')
	strings=strings.replace('(','')
	strings=strings.replace(')','')
	strings=strings.replace(u"‘‘",'')
	strings=strings.replace(u"’’",'')
	strings=strings.replace("''",'')
	strings=strings.replace(".",'')


	t=Tokenizer(strings)
	t.generate_sentences()
	sen=t.sentences

	t.generate_tokens()
	tok=t.tokens
	t.remove_only_space_words()
	t.hyphenated_tokens()
	ttok=list(t.tokens)
	# f=open(fname+'token.txt','w')
	# for i in ttok:
	# 	f.write(i.encode('utf-8')+'\n')
	# f.close()
	s=t.generate_stem_word()
	#f=open(fname+'stem.txt','w')
	# for i in s.keys():
	# 	if s[i]:
	# 		f.write(i.encode('utf-8')+'->'+s[i].encode('utf-8')+'\n')
	# 		#print i.encode('utf-8'),' - ', s[i].encode('utf-8')
	stem_words=[]
	for i in t.tokens:
		#f.write(i.encode('utf-8')+'->'+s[i].encode('utf-8')+'\n')
		stem_words.append(s[i])

	#f.close()

	#f=open(fname+'stem_words.txt','w')
	# for i in stem_words:
	# 	f.write(i.encode('utf-8')+'\n')
	# w='काफी'
	# x=t.concordance(w)
	# for i in x:
	# # 	print_sentence(i)
	t.remove_stop_words(stem_words)
	#print unicode(z)==unicode(ttok[16]),ttok[16],z
	# f=open(fname+'stop.txt','w')
	ttok=t.final
	#print len(set(ttok))
	for i in ttok:
		# f.write(i.encode('utf-8')+'\n')
		business_token.append(i)

business_token=filter(lambda a: a!='-',business_token)
for i in business_token:
	i=i.strip()

f=open(fname+'_map_index.txt','w')
temp_tokens=business_token
temp=0
bfr={}
tok=set(business_token)
business_data_count=0
for i in tok:
	if i:
		ch=temp_tokens.count(i)
		bfr[i.encode('utf-8')]=ch
for w in sorted(bfr,key=bfr.get,reverse=True):
	#print w,fr[w]
	if w:
		business_data_count+=bfr[w]
		f.write(w+' '+str(bfr[w])+'\n')
f.close()
print business_data_count
# print fr["कमरों"]
# fre=t.make_frequency()
# f=open('freq.txt','w')
# for i in fre.keys():
# 	f.write(i.encode('utf-8')+'->'+str(fre[i])+'\n')
# f.close()


#lets work on sample data
fname='sample'
f=codecs.open(fname+'.txt',encoding='utf-8')
strings=f.read()
sample_tokens=[]
#remove numbers
strings=re.sub(r'(\d+)',r'',strings)
strings=strings.replace(',','')
strings=strings.replace('(','')
strings=strings.replace(')','')
strings=strings.replace(u"‘‘",'')
strings=strings.replace(u"’’",'')
strings=strings.replace("''",'')
strings=strings.replace(".",'')


t=Tokenizer(strings)
t.generate_sentences()
sen=t.sentences
t.generate_tokens()
tok=t.tokens
t.remove_only_space_words()
t.hyphenated_tokens()
ttok=list(t.tokens)
s=t.generate_stem_word()
stem_words=[]
for i in t.tokens:
	stem_words.append(s[i])
t.remove_stop_words(stem_words)
ttok=t.final
for i in ttok:
	sample_tokens.append(i)
f=open('sample_map_index.txt','w')
temp_tokens=sample_tokens
temp=0
ssfr={}
tok=set(sample_tokens)
sample_data_count=0
for i in tok:
	if i:
		ch=temp_tokens.count(i)
		ssfr[i.encode('utf-8')]=ch
for w in sorted(ssfr,key=ssfr.get,reverse=True):
	#print w,fr[w]
	if w:
		sample_data_count+=ssfr[w]
		f.write(w+' '+str(ssfr[w])+'\n')
f.close()
print sample_data_count

prob_sports_news=log(0.5)
prob_sports_business=log(0.5)

def count_word(word,fr):
	if word in fr:
		return fr[word]
	else:
		return 0



p_sp=[]
p_bu=[]
p_sp_sum=prob_sports_news
p_bu_sum=prob_sports_business
for w in ssfr.keys():
	word=w
	word_count=0
	p_word_business,p_word_sports=1,1
	if word in sfr.keys():
		p_word_sports=find_prob(sfr,word,sports_data_count)
		word_count+=sfr[word]
	if word in bfr.keys():
		p_word_business=find_prob(bfr,word,business_data_count)
		word_count+=bfr[word]
	p_word=1.0*word_count/(sports_data_count+business_data_count)
	if p_word==0:
		p_word=1
	temp_business=log(1.0*p_word_business)-log(p_word)
	temp_sports=log(1.0*p_word_sports)-log(p_word)
	p_sp_sum+=temp_business
	p_bu_sum+=temp_sports
# 	prob_word_business ,prob_word_sports=1,1
# 	if word in sfr.keys():
# 		prob_word_sports=find_prob(sfr,word,sports_data_count)
# 	if word in bfr.keys():
# 		prob_word_business=find_prob(bfr,word,business_data_count)
# 	#print word,prob_word_sports,prob_word_business
# 	if prob_word_sports!=0:
# 		prob_word_given_sports=log(1.0*prob_word_sports)-(log(1.0*prob_word_sports)+log(1.0*prob_word_business))
# 		p_sp.append(prob_word_given_sports)
# 		p_sp_sum+=prob_word_given_sports
# 	if prob_word_business!=0:
# 		prob_word_given_business=log(1.0*prob_word_business)-(log(1.0*prob_word_sports)+log(1.0*prob_word_business))
# 		p_bu.append(prob_word_given_business)
# 		p_bu_sum+=prob_word_given_business

print 'business = ', p_bu_sum,'sports = ',p_sp_sum








