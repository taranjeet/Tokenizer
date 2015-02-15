#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tokenizer():

	def __init__(self,text):
		self.text=text.decode('utf-8')
		self.tokens=[]
		self.words=[]
		self.sentences=[]

	def words_count(self):
		return len(self.text)

	def tokens_count(self):
		return len(self.tokens)

	def unique_tokens_count(self):
		return len(set(self.tokens))

	def generate_sentences(self):
		text=self.text
		self.sentences=text.split(u"।")

	def generate_words(self):
		sentences_list=self.sentences
		words=[]
		for each in sentences_list:
			word_list=each.split(' ')
			words=words+word_list
		self.words=words

	def generate_tokens(self):
		
		self.generate_words()
		self.tokens=set(self.words)

	def remove_only_space_words(self):
		tokens=filter(lambda tok: tok.strip(),self.tokens)
		self.tokens=tokens

	# def generate_unique_tokens(self):


t=Tokenizer('भारत का काफी-काफी समृद्ध एवं विस्तृत है।पुलिस की प्रवक्ता के मुताबिक़ हम्बर्गर मॉर्गनपोस्ट अखबार की इमारत पर पहले खिड़की से पत्थर फेंके गए और फिर एक जलती हुई मसाल फेंकी गई। इससे इमारत की निचली मंजिल के दो कमरों को नुकसान पहुंचा है। हालांकि सूत्रों की मानें तो आग पर तुरंत काबू पा लिया गया।')
t.generate_sentences()
sen=t.sentences

for i in sen:
	print i
t.generate_tokens()
tok=t.tokens
t.remove_only_space_words()
ttok=t.tokens
for i in ttok:
	print i

print len(ttok),len(sen)

