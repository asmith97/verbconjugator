#uses theme from http://www.designkindle.com/2011/01/19/simple-ui-elements/
#need to add affirmative/negative for commands
import pygame
pi = 3.14159
import __future__

import re
import futureconditionalirregulars as fcirreg

pygame.init()

size = [675,350]
screen = pygame.display.set_mode(size)

white = [0xFF, 0xFF, 0xFF]
green = (0, 250, 0)
black = (0,0,0)
red = (250,0,0)
yellow = (255,255,0)
aqua = (0,255,255)

waitinginput = pygame.image.load("enterverbwaiting_edited-1.jpg")
textbox = waitinginput
gettinginput = pygame.image.load("gettingverb_edited-1.jpg")
#submitinput = pygame.image.load("submitverb_edited-1.psd")
personmenu = pygame.image.load("chooseperson_edited-2.jpg")
personyo = pygame.image.load("choosepersonselectyo2_edited-1.jpg")
persontu = pygame.image.load("choosepersonselecttu_edited-1.jpg")
personel = pygame.image.load("choosepersonselectel_edited-1.jpg")
personnosotros = pygame.image.load("choosepersonselectnosotros_edited-1.jpg")
personvosotros = pygame.image.load("choosepersonselectvosotros_edited-1.jpg")
personellos = pygame.image.load("choosepersonselectellos_edited-1.jpg")
pmenu = personmenu

tensemenu = pygame.image.load("tenseselection_edited-2.jpg")
tensepresent = pygame.image.load("tenseselectionselectpresent_edited-2.jpg")
tensepreterite = pygame.image.load("tenseselectionselectpreterite_edited-3.jpg")
tenseimperfect = pygame.image.load("tenseselectionselectimperfect_edited-3.jpg")
tensefuture = pygame.image.load("tenseselectionselectfuture_edited-3.jpg")
tenseconditional = pygame.image.load("tenseselectionselectconditional_edited-3.jpg")
tmenu = tensemenu

tensemenu2 = pygame.image.load("tenseselection2_edited-1.jpg")
tmenu2 = tensemenu2

moodmenu = pygame.image.load("moodselection_edited-1.jpg")
moodindicative = pygame.image.load("moodselectionselectindicative_edited-1.jpg")
moodsubjunctive = pygame.image.load("moodselectionselectsubjunctive_edited-1.jpg")
moodimperative = pygame.image.load("moodselectionselectimperative_edited-1.jpg")
mmenu = moodmenu

resetbutton = pygame.image.load("resetbutton_edited-1.jpg")
pressedresetbutton = pygame.image.load("pressedresetbutton_edited-2.jpg")
rbutton = resetbutton

pygame.display.set_caption("Bub's Spanish Conjugator")


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
		irregulars = ["ir", "ser", "ver"]
		if self.v in irregulars:
			if self.v == "ir":
				if self.p == "yo":
					conjugation = "iba"
				elif self.p == "tu":
					conjugation - "ibas"
				elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
					conjugation = "iba"
				elif self.p == "nosotros" or self.p == "nosotras":
					conjugation = "ibamos (with accent over i)"
				elif self.p == "vosotros" or self.p == "vosotras":
					conjugation = "ibais"
				elif self.p == "ellos" or self.p == "ellas":
					conjugation = "iban"
			elif self.v == "ver":
				if self.p == "yo":
					conjugation = "veia (with accent over i)"
				elif self.p == "tu":
					conjugation - "veias (with accent over i)"
				elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
					conjugation = "veia (with accent over i)"
				elif self.p == "nosotros" or self.p == "nosotras":
					conjugation = "veiamos (with accent over i)"
				elif self.p == "vosotros" or self.p == "vosotras":
					conjugation = "veiais (with accent over i)"
				elif self.p == "ellos" or self.p == "ellas":
					conjugation = "veian (with accent over i)"
			elif self.v == "ser":
				if self.p == "yo":
					conjugation = "era"
				elif self.p == "tu":
					conjugation - "eras"
				elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
					conjugation = "era"
				elif self.p == "nosotros" or self.p == "nosotras":
					conjugation = "eramos (with accent over e)"
				elif self.p == "vosotros" or self.p == "vosotras":
					conjugation = "erais"
				elif self.p == "ellos" or self.p == "ellas":
					conjugation = "eran"
					
		else:
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
		#print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
				
	def conjugatePresentIndicative(self):
		tense = "present"
		root = self.root(self.v)
		type = self.ending(self.v)
		'''if root in fcirreg.stemchange:
			root = fcirreg.stemchange[root]
		#there's an extra space at the begining of the verb for some reason
		list = ['almorzar','cerrar','comenzar','confesar','contar','costar','defender','devolver','dormir','empezar','encontrar','entender','jugar','medir','morir','mostrar','pedir','pensar','perder','poder','preferir','querer','recordar','referir','repetir','resolver','sentir','servir','sonar','volar','volver']	
		for i in range(len(list)):
			list[i] = " " + list[i]
		
		if self.v in list:
			if "o" in self.v:
				self.v = verb
				self.v = self.v.replace("o", "ue")
				root = self.root(self.v)
				self.v = verb'''
		'''for i in range(len(fcirreg.eiestemchange)):
			fcirreg.eiestemchange[i] = " " + fcirreg.eiestemchange[i]'''
		
				
		if self.v in fcirreg.eiestemchange:
			if self.p == "nosotros" or self.p == "vosotros":
				pass
			else:
				self.v = verb
				self.v = self.v.replace("e", "ie")
				root = self.root(self.v)
				self.v = verb
		'''for i in range(len(fcirreg.eistemchange)):
			fcirreg.eistemchange[i] = " " + fcirreg.eistemchange[i]'''
		if self.v in fcirreg.eistemchange:
			if self.p == "nosotros" or self.p == "vosotros":
				pass
			else:
				self.v = verb
				self.v = self.v.replace("e", "i")
				root = self.root(self.v)
				self.v = verb
		'''for i in range(len(fcirreg.ouestemchange)):
			fcirreg.ouestemchange[i] = " " + fcirreg.ouestemchange[i]'''
		if self.v in fcirreg.ouestemchange:
			if self.p == "nosotros" or self.p == "vosotros":
				pass
			else:
				self.v = verb
				self.v = self.v.replace("o", "ue")
				root = self.root(self.v)
				self.v = verb
		
				
		
		if type == "ar":
			if self.p == "yo":
				if self.v in fcirreg.presentirregulars:
					root = ""
					add = fcirreg.presentirregulars[self.v]
				else:
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
				if self.v in fcirreg.presentirregulars:
					root = ""
					add = fcirreg.presentirregulars[self.v]
				else:
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
				if self.v in fcirreg.presentirregulars:
					root = ""
					add = fcirreg.presentirregulars[self.v]
				else:
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
				
		if self.v == "ser":
			if self.p == "yo":
				root = ""
				add = "soy"
			elif self.p == "tu":
				root = ""
				add = "eres"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				root = ""
				add = "es"
			elif self.p == "nosotros" or self.p == "nosotras":
				root = ""
				add = "somos"
			elif self.p == "vosotros" or self.p == "vosotras":
				root = ""
				add = "sois"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				root = ""
				add = "son"
		conjugation = root + add
		if self.m == "indicative":
			#print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
			self.c = conjugation
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
		#print "The", self.p, "form of",self.v, "in", tense,  "is", conjugation, "."
		self.c = conjugation
		
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
		#print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation	
	
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
		#print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
		
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
		#print "The", self.p, "form of",self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
		
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
		#print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
	
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
		#print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
	
	def conjugatePreteriteIndicative(self):
		root = self.root(self.v)
		type = self.ending(self.v)
		#fix verbs with car/gar/zar ending page 10 spanish book
		if self.v in fcirreg.stemchangepast:
			root = fcirreg.stemchangepast[self.v]
			if self.p == "yo":
				add = "e"
			elif self.p == "tu":
				add = "iste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				if self.v == "hacer":
					root = ""
					add = "hizo"
				else:
					add = "o"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "imos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "isteis"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				if re.findall("j$", root) == ['j']:
					add = "eron"
				else:
					add = "ieron"
			type = "irregular"
			conjugation = root + add
		elif self.v == "ser" or self.v == "ir":
			if self.p == "yo":
				conjugation = "fui"
			elif self.p == "tu":
				conjugation = "fuiste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				conjugation = "fue"
			elif self.p == "nosotros" or self.p == "nosotras":
				conjugation = "fuimos"
			elif self.p == "vosotros" or self.p == "vosotras":
				conjugation = "fuisteis"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				conjugation = "fueron"
		elif self.v == "dar" or self.v == "ver":
			if self.v == "dar":
				root ="d"
			elif self.v == "ver":
				root = "v"
			if self.p == "yo":
				add = "i"
			elif self.p == "tu":
				add = "iste"
			elif self.p == "el" or self.p == "ella" or self.p == "usted" or self.p == "ud":
				add = "io"
			elif self.p == "nosotros" or self.p == "nosotras":
				add = "imos"
			elif self.p == "vosotros" or self.p == "vosotras":
				add = "isteis"
			elif self.p == "ellos" or self.p == "ellas" or self.p == "ustedes" or self.p == "uds":
				add = "ieron"
			conjugation = root + add
		else:
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
			#print "The", self.p, "form of",self.v, "in", self.t, self.m, "is", conjugation, "."
			self.c = conjugation
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
			#print "The", self.p, "form of",self.v, "in", tense, self.m, "is", conjugation, "."
			self.c = conjugation
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
		#print "The", self.p, "form of", self.v, "in", tense, "is", conjugation, "."
		self.c = conjugation
		
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
		#print "The", self.p, "form of", self.v, "in", self.t, self.m, "is", conjugation, "."
		self.c = conjugation
		
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
		#print "The", self.p, "form of",self.v, "in", self.t, self.m, "is", conjugation, "."
		self.c = conjugation
	
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
		#print "The", tense, "of", self.p, "is", command
		self.c = conjugation
			
	def conjugatenegativecommand(self):
		tense = "negative command"
		command = "no " + self.conjugatePresentSubjunctive()
		#print "The", tense, "of", self.p, "is", command, "."
		self.c = conjugation	
	
	
	
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

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		self.c = color
		self.w = width
		self.h = height
		self.state = " "
		self.t = " "
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		
	def changestate(self):
		color = green
		self.image.fill(color)
		self.state = "on"
		
	def resetstate(self):
		color = self.c
		self.image.fill(color)
		self.state = "off"
	
	def positionx(self):
		xval = self.rect.x
		xpos = range(xval,xval + self.w)
		return xpos
		
	def positiony(self):
		yval = self.rect.y
		ypos = range(yval, yval + self.h)
		return ypos
	
	def text(self):
		font = pygame.font.Font(None,25)
		text = font.render(self.t, True, black)
		screen.blit(text, [self.rect.x + 1,self.rect.y + 10 ])
		
block_list = pygame.sprite.RenderPlain()
all_sprites_list = pygame.sprite.RenderPlain()

block = Block(white, 80,25)
block2 = Block(aqua, 118,25)
block3 = Block(aqua, 118, 25)
block4 = Block(aqua, 118, 25)
block5 = Block(aqua, 118,22)
block6 = Block(aqua, 118, 25)
block7 = Block(aqua, 118, 25)
block8 = Block(aqua, 118,25)
block9 = Block(aqua, 118, 22)
block10 = Block(aqua, 118, 25)
block11 = Block(yellow, 118,25)
block12 = Block(yellow, 118, 25)
block13 = Block(yellow, 118,22)
block14 = Block(aqua, 118,25)
block15 = Block(aqua, 118,25)
block16 = Block(aqua, 118,25)
block17 = Block(aqua, 118,25)
block18 = Block(aqua, 118,25)
block19 = Block(aqua, 118,20)
all_sprites_list.add(block)
all_sprites_list.add(block2)
all_sprites_list.add(block3)
all_sprites_list.add(block4)
all_sprites_list.add(block5)
all_sprites_list.add(block6)
all_sprites_list.add(block7)
all_sprites_list.add(block8)
all_sprites_list.add(block9)
all_sprites_list.add(block10)
all_sprites_list.add(block11)
all_sprites_list.add(block12)
all_sprites_list.add(block13)
all_sprites_list.add(block14)
all_sprites_list.add(block15)
all_sprites_list.add(block16)
all_sprites_list.add(block17)
all_sprites_list.add(block18)
all_sprites_list.add(block19)
block_list.add(block2)

x = 50
y = 50
x1 = 200
y1 = 100
x2 = 200
y2 = 150
x3 = 200
y3 = 125
x4 = 200
y4 = 200
x5 = 200
y5 = 175

x6 = 350
y6 = 100
x7 = 350
y7 = 125
x8 = 350
y8 = 175
x9 = 350
y9 = 150

x12 = 500
y12 = 100
x13 = 500
y13 = 125
x14 = 500
y14 = 150

x15 = 50
y15 = 100
x16 = 50
y16 = 125
x17 = 50
y17 = 150
x18 = 50
y18 = 175
x19 = 50
y19 = 200
x20 = 50
y20 = 225

done=False

#Creates the text for the boxes
block.t = " "#"Reset"
block2.t = " "#"Present"
block3.t = " "#"Imperfect"
block4.t  = " "#"Preterite"
block5.t = " "#"Conditional"
block6.t = " "#"Future"
block7.t = " "#"Present Perfect"
block8.t = " "#"Pluperfect"
block9.t = " "#"Conditional Perfect"
block10.t = " "#"Future Perfect"
block11.t = " "#"Indicative"
block12.t = " "#"Subjunctive"
block13.t = " "#"Imperative"
block14.t = " "#"Yo"
block15.t = " "#"Tu"
block16.t = " "#"El/Ella/Usted"
block17.t = " "#"Nosotros"
block18.t = " "#"Vosotros"
block19.t = " "#"Ellos/Ellas/Ustedes"

clock = pygame.time.Clock()
verb = ""
conjugation = " "
sentence = " "
font = pygame.font.Font(None,25)
#Main Loop
while done == False:
	for event in pygame.event.get():
		if block2.state == "on":
			tense = "present"
			tmenu = tensepresent
		if block3.state == "on":
			tense = "imperfect"
			tmenu = tenseimperfect
		if block4.state == "on":
			tense = "preterite"
			tmenu = tensepreterite
		if block5.state == "on":
			tense = "conditional"
			tmenu = tenseconditional
		if block6.state == "on":
			tense = "future"
			tmenu = tensefuture
		if block7.state == "on":
			tense = "present perfect"
		if block8.state == "on":
			tense = "pluperfect"
		if block9.state == "on":
			tense = "conditional perfect"
		if block10.state == "on":
			tense = "future perfect"
		if block11.state == "on":
			mood = "indicative"
			mmenu = moodindicative
		if block12.state == "on":
			mood = "subjunctive"
			mmenu = moodsubjunctive
		if block13.state == "on":
			mood = "imperative"
			mmenu = moodimperative
		if block14.state == "on":
			person = "yo"
			pmenu = personyo
		if block15.state == "on":
			person = "tu"
			pmenu = persontu
		if block16.state == "on":
			person = "el"
			pmenu = personel
		if block17.state == "on":
			person = "nosotros"
			pmenu = personnosotros
		if block18.state == "on":
			person = "vosotros"
			pmenu = personvosotros
		if block19.state == "on":
			person = "ellos"
			pmenu = personellos
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RETURN:
				#textbox = submitinput
				#person = "yo"
				#tense = "present"
				#mood = "indicative"
				try:
					verb1 = Verb(verb, person, tense, mood)	
					verb1.whichmood()
					sentence = "The " + verb1.p + " form of " + verb1.v + " in " + verb1.t + " " + verb1.m + " is " + verb1.c + "."
				except:
					sentence = "Please specify the verb, person, tense, and mood"
				#conjugation = verb1.c
			elif event.key == pygame.K_BACKSPACE:
				verb = verb[:-1]
			#elif event.key == pygame.K_SPACE:
			#	rbutton = pressedresetbutton
			elif event.key < 127:
				verb = verb + chr(event.key)
				textbox = gettinginput
		if event.type == pygame.MOUSEBUTTONDOWN:
			xcoord = block.positionx()
			ycoord = block.positiony()
			if pos[0] in xcoord and pos[1] in ycoord:
				block.changestate()
				rbutton = pressedresetbutton
			elif pos[0] in block2.positionx() and pos[1] in block2.positiony():
				block2.changestate()
				
			elif pos[0] in block3.positionx() and pos[1] in block3.positiony():
				block3.changestate()
			elif pos[0] in block4.positionx() and pos[1] in block4.positiony():
				block4.changestate()
			elif pos[0] in block5.positionx() and pos[1] in block5.positiony():
				block5.changestate()
			elif pos[0] in block6.positionx() and pos[1] in block6.positiony():
				block6.changestate()
			elif pos[0] in block7.positionx() and pos[1] in block7.positiony():
				block7.changestate()
			elif pos[0] in block8.positionx() and pos[1] in block8.positiony():
				block8.changestate()
			elif pos[0] in block9.positionx() and pos[1] in block9.positiony():
				block9.changestate()
			elif pos[0] in block10.positionx() and pos[1] in block10.positiony():
				block10.changestate()
			elif pos[0] in block11.positionx() and pos[1] in block11.positiony():
				block11.changestate()
			elif pos[0] in block12.positionx() and pos[1] in block12.positiony():
				block12.changestate()
			elif pos[0] in block13.positionx() and pos[1] in block13.positiony():
				block13.changestate()
			elif pos[0] in block14.positionx() and pos[1] in block14.positiony():
				block14.changestate()
			elif pos[0] in block15.positionx() and pos[1] in block15.positiony():
				block15.changestate()
			elif pos[0] in block16.positionx() and pos[1] in block16.positiony():
				block16.changestate()
			elif pos[0] in block17.positionx() and pos[1] in block17.positiony():
				block17.changestate()
			elif pos[0] in block18.positionx() and pos[1] in block18.positiony():
				block18.changestate()
			elif pos[0] in block19.positionx() and pos[1] in block19.positiony():
				block19.changestate()
			else:
				block.resetstate()
				rbutton = resetbutton
				block2.resetstate()	
				block3.resetstate()
				block4.resetstate()
				block5.resetstate()
				block6.resetstate()
				block7.resetstate()
				block8.resetstate()
				block9.resetstate()
				block10.resetstate()
				block11.resetstate()
				block12.resetstate()
				block13.resetstate()
				block14.resetstate()
				block15.resetstate()
				block16.resetstate()
				block17.resetstate()
				block18.resetstate()
				block19.resetstate()
				textbox = waitinginput
				pmenu = personmenu
				tmenu = tensemenu
				tmenu2 = tensemenu2
				mmenu = moodmenu
				
	#All event processing above this comment
	
	pos = pygame.mouse.get_pos()
	
	
	block.rect.x = x
	block.rect.y = y
	
	block2.rect.x = x1
	block2.rect.y = y1
	
	block3.rect.x = x2
	block3.rect.y = y2
	
	block4.rect.x = x3
	block4.rect.y = y3
	
	block5.rect.x = x4
	block5.rect.y = y4
	
	block6.rect.x = x5
	block6.rect.y = y5
	
	block7.rect.x = x6
	block7.rect.y = y6
	
	block8.rect.x = x7
	block8.rect.y = y7
	
	block9.rect.x = x8
	block9.rect.y = y8
	
	block10.rect.x = x9
	block10.rect.y = y9
	
	block11.rect.x = x12
	block11.rect.y = y12
	
	block12.rect.x = x13
	block12.rect.y = y13
	
	block13.rect.x = x14
	block13.rect.y = y14
	
	block14.rect.x = x15
	block14.rect.y = y15
	
	block15.rect.x = x16
	block15.rect.y = y16
	
	block16.rect.x = x17
	block16.rect.y = y17
	
	block17.rect.x = x18
	block17.rect.y = y18
	
	block18.rect.x = x19
	block18.rect.y = y19
	
	block19.rect.x = x20
	block19.rect.y = y20
	
	
	#All game logic below this comment
	
	if block.state == "on":
		verb = ""
		sentence = " "
		textbox = waitinginput
		pmenu = personmenu
		tmenu = tensemenu
		tmenu2 = tensemenu2
		mmenu = moodmenu
	
	
	#All game logic above this comment
	
	#All draw code below this comment	
	
	screen.fill(white)
	
	screen.blit(textbox, (198,10))
	
	font = pygame.font.Font(None,25)
	text = font.render(verb, True, black)
	screen.blit(text, [205,20])
	
	font = pygame.font.Font(None,25)
	text = font.render(sentence, True, black)
	screen.blit(text, [50,300])
	
	'''font = pygame.font.Font(None,25)
	text = font.render(conjugation, True, black)
	screen.blit(text, [50,350])'''
	
	block_list.draw(screen)
	all_sprites_list.draw(screen)
	block.text()
	block2.text()
	block3.text()
	block4.text()
	block5.text()
	block6.text()
	block7.text()
	block8.text()
	block9.text()
	block10.text()
	block11.text()
	block12.text()
	block13.text()
	block14.text()
	block15.text()
	block16.text()
	block17.text()
	block18.text()
	block19.text()
	#All draw code above this comment
	
	
	screen.blit(pmenu, (50,100))
	screen.blit(tmenu, (200, 100))
	screen.blit(tmenu2, (350,100))
	screen.blit(mmenu, (500, 100))
	screen.blit(rbutton, (50,50))
	
	pygame.display.flip()
			
	clock.tick(20)
	
	
	
pygame.quit()