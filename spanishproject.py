import re
import futureconditionalirregulars as fcirreg
# Encoding: UTF-8
# -*- coding: utf-8 -*-

class Verb():
	def __init__(self, verb, person, tense, mood):
		self.v = verb
		self.p = person
		self.t = tense
		self.m = mood
		
	def root(self,verb):
		split = verb[:-2]
		return split
	
	def ending(self, verb):
		if re.findall("ar$", verb) == ['ar']:
			ending = "ar"
		elif re.findall("er$", verb) == ['er']:
			ending = "er"
		elif re.findall("ir$", verb) == ['ir']:
			ending = "ir"
		elif re.findall("ir$", verb) == []:
			print "You have entered an invalid verb"
			ending = "Invalid"
		return ending
		
	def doublevowel(self):
		if bool(re.findall("eer$", self.v)) == True:
			double = True
		elif bool(re.findall("aer$", self.v)) == True:
			double = True
		else:
			double = False
		return double
			
		
	def pastparticiple(self):
		if self.v in fcirreg.pastpart:
			pastpart = fcirreg.pastpart[self.v]
			return pastpart
		else: 
			type = self.ending(self.v)
			root = self.root(self.v)
			if type == "ar":
				add = "ado"
			elif type == "er" or type == "ir":
				doub = self.doublevowel()
				if doub == True:
					add = "ido (with accent over the last i)"
				else:
					add = "ido"
			pastpart = root + add
			return pastpart
				
	def conjugateImperfectIndicative(self):
		tense = "imperfect"
		root = self.root(self.v)
		type = self.ending(self.v)
		irregulars = ["dar", "ser", "ver"]
		'''if self.v in irregulars:
			if self.v == "dar":
				if self.p == "yo":
					conjugation = "de (with accent)"
				elif self.p == "tu":
					conjugation - "des"
				elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
					conjugation = "de (with accent)"
				elif self.p == "nosotros" or self.p == "nosotras":
					conjugation = '''
					
		
		if type == "ar":
			if self.p == "yo":
				add = "aba"
			elif self.p == "tu":
				add = "abas"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "aba"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "abamos (accent over first a)"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "abais (accent over the a in ais)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "aban"
		elif type == "er":
			if self.p == "yo":
				add = "ia"
			elif self.p == "tu":
				add = "ias"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "ia"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "iamos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "iais (accent over the e in eis)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ian"
			add = add + "(accent over the i in all of them)"
		elif type == "ir":
			if self.p == "yo":
				add = "ia"
			elif self.p == "tu":
				add = "ias"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "ia"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "iamos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "iais (accent over the i in is)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ian"
			add = add + "(accent over the i in all of them)"
		conjugation = root + add
		print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
				
	def conjugatePresentIndicative(self):
		tense = "present"
		root = self.root(self.v)
		type = self.ending(self.v)
		if root in fcirreg.stemchange:
			root = fcirreg.stemchange[root]
		
		if type == "ar":
			if self.p == "yo":
				add = "o"
			elif self.p == "tu":
				add = "as"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "a"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "amos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "ais (accent over the a in ais)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "an"
		elif type == "er":
			if self.p == "yo":
				add = "o"
			elif self.p == "tu":
				add = "es"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "e"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "emos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "eis (accent over the e in eis)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "en"
		elif type == "ir":
			if self.p == "yo":
				add = "o"
			elif self.p == "tu":
				add = "es"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "e"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "imos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "is (accent over the i in is)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "en"
		conjugation = root + add
		if self.m == "indicative":
			print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		elif self.m == "subjunctive":
			return conjugation
		elif self.m == "imperative" or self.m == "command" or self.m == "imp":
			return conjugation
	
	def conjugateFutureIndicative(self):
		tense = "future"
		if self.v in fcirreg.irregulars:
			root = fcirreg.irregulars[self.v]
		else:
			root = self.v
		if self.p == "yo":
			add = "e (with accent)"
		elif self.p == "tu":
			add = "as (with accent)"
		elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
			add = "a (with accent)"
		elif self.p == "nosotros" or self.p == "nosotras":
			add = "emos (with out accent)"
		elif self.p == "vosotros" or self.p == "vosotras":
			add = "eis (with accent)"
		elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
			add = "an (with accent"
		conjugation = root + add
		print "The", self.p, "form of",self.v, "in", tense,  "is", conjugation, "."
	
	def conjugateConditionalIndicative(self):
		tense = "conditional"
		if self.v in fcirreg.irregulars:
			root = fcirreg.irregulars[self.v]
		else:
			root = self.v
		if self.p == "yo":
			add = "ia (with accent over i)"
		elif self.p == "tu":
			add = "ias (with accent over i)"
		elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
			add = "ia (with accent over i)"
		elif self.p == "nosotros" or self.p == "nosotras":
			add = "iamos (with out accent over i)"
		elif self.p == "vosotros" or self.p == "vosotras":
			add = "iais (with accent over first i)"
		elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
			add = "ian (with accent over i)"
		conjugation = root + add
		print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
	
	def conjugatePresentPerfectIndicative(self):
		tense = "present perfect"
		pastpart = self.pastparticiple()
		if self.p == "yo":
			aux = "he "
		elif self.p == "tu":
			aux = "has "
		elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
			aux = "ha "
		elif self.p == "nosotros" or self.p == "nosotras":
			aux = "hemos "
		elif self.p == "vosotros" or self.p == "vosotras":
			aux = "habeis (accent over the e) "
		elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
			aux = "han "
		conjugation = aux + pastpart
		print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		
	def conjugatePluperfectIndicative(self):
		tense = "pluperfect"
		pastpart = self.pastparticiple()
		if self.p == "yo":
			aux = "habia "
		elif self.p == "tu":
			aux = "habias "
		elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
			aux = "habia "
		elif self.p == "nosotros" or self.p == "nosotras":
			aux = "habiamos "
		elif self.p == "vosotros" or self.p == "vosotras":
			aux = "habiais (accent over the e) "
		elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
			aux = "habian "
		conjugation = aux + "(accent over i)" + pastpart
		print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		
	def conjugateFuturePerfect(self):
		tense = "future perfect"
		pastpart = self.pastparticiple()
		if self.p == "yo":
			aux = "habre (with accent) "
		elif self.p == "tu":
			aux = "habras (with accent)"
		elif self.p == "el" or self. t == "ella" or self.t == "usted" or self.t == "ud":
			aux = "habra (with accent) "
		elif self.p == "nosotros" or self.t == "nosotras":
			aux = "habremos "
		elif self.p == "vosotros" or self.t == "vosotros":
			aux = "habreis (with accent over e) "
		elif self.p == "ellos" or self.t == "ellas" or self.t == "ustedes":
			aux = "habran (with accent over a)"
		conjugation = aux + pastpart
		print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
	
	def conjugateConditionalPerfect(self):
		tense = "conditional perfect"
		pastpart = self.pastparticiple()
		if self.p == "yo":
			aux = "habria (with accent) "
		elif self.p == "tu":
			aux = "habrias (with accent)"
		elif self.p == "el" or self. t == "ella" or self.t == "usted" or self.t == "ud":
			aux = "habria (with accent) "
		elif self.p == "nosotros" or self.t == "nosotras":
			aux = "habriamos (with accent) "
		elif self.p == "vosotros" or self.t == "vosotros":
			aux = "habriais (with accent) "
		elif self.p == "ellos" or self.t == "ellas" or self.t == "ustedes":
			aux = "habrian (with accent)"
		conjugation = aux + pastpart
		print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
	
	def conjugatePreteriteIndicative(self):
		root = self.root(self.v)
		type = self.ending(self.v)
		if self.v in fcirreg.stemchangepast:
			root = fcirreg.stemchangepast[self.v]
			if self.p == "yo":
				add = "e"
			elif self.p == "tu":
				add = "iste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "o"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "imos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "isteis"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ieron"
				type = "irregular"
		if type == "ar":
			if self.p == "yo":
				add = "e (with accent)"
			elif self.p == "tu":
				add = "aste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "o (with accent)"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "amos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "asteis"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "aron"
		elif type == "er" or type == "ir":
			if self.p == "yo":
				add = "i (with accent)"
			elif self.p == "tu":
				add = "iste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "io (with accent over o)"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "imos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "isteis (accent over the e in eis)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ieron"
		conjugation = root + add
		
		if self.m == "indicative":
			print "The", self.p, "form of",self.v, "in", self.t, self.m, "is", conjugation, "."
		elif self.m == "subjunctive":
			rootsubj = conjugation[:-3]
			return rootsubj
		
		
	def conjugatePresentSubjunctive(self):
		tense = "present subjunctive"
		self.p = person
		self.p = "yo"
		root = self.conjugatePresentIndicative()
		self.p = person
		newroot = root[:-1]
		type = self.ending(self.v)
		
		if type == "ar":
			if self.p == "yo":
				add = "e"
			elif self.p == "tu":
				add = "es"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "e"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "emos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "eis (accent over the e in eis)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "en"
		elif type == "er" or type == "ir":
			if self.p == "yo":
				add = "a"
			elif self.p == "tu":
				add = "as"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "a"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "amos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "ais (accent over the a in ais)"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "an"
		conjugation = newroot + add
		if self.m == "subjunctive":
			print "The", self.p, "form of",self.v, "in", tense, self.m, "is", conjugation, "."
		elif self.m == "imperative" or self.m == "command" or self.m == "imp":
			return conjugation
	
	def conjugatePresentPerfectSubjunctive(self):
		tense = "present perfect"
		pastpart = self.pastparticiple()
		if self.p == "yo":
			aux = "haya "
		elif self.p == "tu":
			aux = "hayas "
		elif self.p == "el" or self. t == "ella" or self.t == "usted" or self.t == "ud":
			aux = "haya "
		elif self.p == "nosotros" or self.t == "nosotras":
			aux = "hayamos "
		elif self.p == "vosotros" or self.t == "vosotros":
			aux = "hayais (accent over a) "
		elif self.p == "ellos" or self.t == "ellas" or self.t == "ustedes":
			aux = "hayan "
		conjugation = aux + pastpart
		print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
	
	def conjugateImperfectSubjunctive(self):
		tense = self.p
		self.p = "ustedes"
		root = self.conjugatePreteriteIndicative()
		self.p = tense
		
		type = self.ending(self.v)
			
		
		if type == "ar" or type == "er" or type == "ir":
			if self.p == "yo":
				add = "ra"
			elif self.p == "tu":
				add = "ras"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "ra"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "ramos (accent over vowel before the r)"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "rais"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ran"
		conjugation = root + add
		print "The", self.p, "form of", self.v, "in", self.t, self.m, "is", conjugation, "."
		
		
	def conjugatePluperfectSubjunctive(self):
		part = self.pastparticiple()
		
		if self.p == "yo":
			aux = "hubiera"
		elif self.p == "tu":
			aux = "hubieras"
		elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
			aux = "hubiera"
		elif self.p == "nosotros" or self.p == "nosotras":
			aux = "hubieramos (with accent)"
		elif self.p == "vosotros" or self.p == "vosotras":
			aux = "hubierais"
		elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
			aux = "hubieran"
		conjugation = aux + " " + part
		print "The", self.p, "form of",self.v, "in", self.t, self.m, "is", conjugation, "."
	
	
	def conjugateaffirmativecommand(self):
		tense = "affirmative command"
		if (self.p == "usted" or self.p == "ud" or self.p == "el" or self.p == "ella"
		or self.p == "nosotros" or self.p == "nosotras" or self.p == "ellos" or self.p == "ellas"
		or self.p == "ustedes" or self.p == "uds"):
			command = self.conjugatePresentSubjunctive()
		elif self.p == "tu":
			self.p = person
			self.p = "usted"
			command = self.conjugatePresentIndicative()
			self.p = person
		elif self.p == "vosotros" or self.p == "vosotras":
			root = self.v[:-1]
			command = root + "d"
		print "The", tense, "of", self.p, "is", command
			
			
	def conjugatenegativecommand(self):
		tense = "negative command"
		command = "no " + self.conjugatePresentSubjunctive()
		print "The", tense, "of", self.p, "is", command, "."
		
	
	
	
	def conjugateindicative(self):
		if self.t == "present":
			self.conjugatePresentIndicative()
		elif self.t == "preterite":
			self.conjugatePreteriteIndicative()
		elif self.t == "imperfect":
			self.conjugateImperfectIndicative()
		elif self.t == "future":
			self.conjugateFutureIndicative()
		elif self.t == "conditional":
			self.conjugateConditionalIndicative()
		elif self.t == "present perfect":
			self.conjugatePresentPerfectIndicative()
		elif self.t == "pluperfect" or self.t == "imperfect perfect" or self.t == "past perfect":
			self.conjugatePluperfectIndicative()
		elif self.t == "conditional perfect":
			self.conjugateConditionalPerfect()
		elif self.t == "future perfect":
			self.conjugateFuturePerfect()
		elif self.t == "all":
			self.conjugatePresentIndicative()
			self.conjugatePreteriteIndicative()
			self.conjugateImperfectIndicative()
			self.conjugateFutureIndicative()
			self.conjugateConditionalIndicative()
			self.conjugatePresentPerfectIndicative()
			self.conjugatePluperfectIndicative()
			self.conjugateConditionalPerfect()
			self.conjugateFuturePerfect()
		
		
		
	def conjugatesubjunctive(self):
		if self.t == "present":
			self.conjugatePresentSubjunctive()
		elif self.t == "imperfect" or self.t == "past":
			self.conjugateImperfectSubjunctive()
		elif self.t == "present perfect":
			self.conjugatePresentPerfectSubjunctive()
		elif self.t == "pluperfect" or self.t == "imperfect perfect" or self.t == "past perfect":
			self.conjugatePluperfectSubjunctive()
		elif self.t == "all":
			self.conjugatePresentSubjunctive()
			self.conjugateImperfectSubjunctive()
			self.conjugatePresentPerfectSubjunctive()
			self.conjugatePluperfectSubjunctive()
			
	def conjugatecommand(self):
		if self.t == "affirmative":
			self.conjugateaffirmativecommand()
		elif self.t == "negative":
			self.conjugatenegativecommand()
		elif self.t == "all":
			self.conjugateaffirmativecommand()
			self.conjuagenegativecommand()
				
	def whichmood(self):
		if self.m == "subjunctive" or self.m == "subj":
			self.conjugatesubjunctive()
		elif self.m == "command" or self.m == "imperative" or self.m == "imp":
			self.conjugatecommand()
		else:
			self.conjugateindicative()
			




done = False
while done == False:
		
	verb = raw_input("What is the verb you would like to conjugate? ")
	person = raw_input("What person would you like to conjugate in ? ")
	tense = raw_input("What tense would you like to conjugate in ? ")
	mood = raw_input("What mood would you like to conjugate in? ")
	
	
	verb1 = Verb(verb, person, tense, mood)
	print " "
	verb1.whichmood()
	print " "
	again = raw_input("Would you like to conjugate another verb? ")
	if again == "yes" or again == "y":
		print " "
		done = False
	else:
		done = True
print " "
print "Thank you for using this conjugator!"		
		