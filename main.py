#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tokenizer():

	'''class that implements a basic tokenizer for Hindi language'''

	def __init__(self,text):
		'''sets the data members
			text contains the input text
			tokens : a list containing all the tokens
			words : a list containing all the words
			sentences : a list containing all the sentences
		'''
		self.text=text.decode('utf-8')
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
		self.tokens=set(self.words)

	def remove_only_space_words(self):
		'''remove tokens containing only spaces'''
		tokens=filter(lambda tok: tok.strip(),self.tokens)
		self.tokens=tokens

	def hyphenated_tokens(self):
		'''removes tokens containing replicating words'''
		for each in self.tokens:
			if '-' in each:
				tok=each.split('-')
				self.tokens.remove(each)
				self.tokens.append(tok[0])
				self.tokens.append(tok[1])
		self.tokens=set(self.tokens)

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
			for i in range(5,0,-1):
				if len(each_token)>i+1:
					for suf in suffixes[i]:
						if each_token.encode('utf-8').endswith(suf):
							stem_word[each_token]=each_token[:-i]
						else:
							stem_word[each_token]=each_token
		return stem_word

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

def print_sentence(sent):
	print (sent.decode('utf-8'))


t=Tokenizer('भारत का काफी-काफी समृद्ध-एवं विस्तृत है।पुलिस की प्रवक्ता के मुताबिक़ हम्बर्गर मॉर्गनपोस्ट अखबार की इमारत पर पहले खिड़की से पत्थर फेंके गए और फिर एक जलती हुई मसाल फेंकी गई। इससे इमारत की निचली मंजिल के दो कमरों को नुकसान पहुंचा है। हालांकि सूत्रों की मानें तो आग पर तुरंत काबू पा लिया गया।')
t.generate_sentences()
sen=t.sentences

# for i in sen:
# 	print i
t.generate_tokens()
tok=t.tokens
t.remove_only_space_words()
t.hyphenated_tokens()
ttok=t.tokens
for i in ttok:
	print i.encode('utf-8')

print len(ttok),len(sen)
s=t.generate_stem_word()
print 'generating stem words'
for i in s.keys():
	print i.encode('utf-8'),' - ', s[i].encode('utf-8')
w='काफी'
x=t.concordance(w)
for i in x:
	print_sentence(i)



