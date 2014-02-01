#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Module sem sér um geymslu lána, sparnaðar, og mánaðarlegs sparnaðar

"""
# Klasi fyrir lán
class Loan:
	# Notkun: l = Loan(name, amount, interest, pay)
	# Fyrir:  amount, interest og pay eru tölur (interest er á brotaformi
	# 	  EKKI á prósentuformi, þ.e. 0.05 í stað 5%), name er strengur
	# Eftir:  l er lán með nafnið name, höfuðstól amount, 
	#	  vexti interest og mánaðarlega innborgun pay
	def __init__(self, name, amount, interest, pay):
		self.amount = amount
		self.interest = interest
		self.name = name
		self.pay = pay

	# Notkun: print(l)
	# Fyrir:  l er lán
	# Eftir:  lánið er prentað á skjáinn
	def __str__(self):
		return "Lán: %s Höfuðstóll: %d Vextir: %f Mánaðarleg innborgun: %d" % (self.name, self.amount, self.interest, self.pay)

	# Notkun: l.changePay(newPay)
	# Fyrir:  newPay er tala
	# Eftir:  l.pay = newPay
	def changePay(newPay):
		self.pay = newPay

"""


# Klasi sem skilgreinir lán sem hlut (útgáfa Leós)
class Loan:
	# Notkun: L = Loan(Name, Amount, Interest, Months, Index)
	# Fyrir:  Name er strengur, Amount er heiltala >=0, Interest er heiltala >= 0, Months er heiltala >0 og Index er boolean.
	# Eftir:  L er lán sem heitir Name, með höfuðstól Amount, Interest ársvexti, Months tíma eftir og Index segir til um verðtryggingu.
	def __init__(self, name, amount, interest, months, index):
		self.name = name
		self.interest = interest
		self.dex = index
		self.amount = amount
		self.m = months
	
	def __str__(self):
		return "Lán: %s Höfuðstóll: %d Ársvextir: %f Lengd(mánuðir): %f Verðtryggt: %s" % (self.name, self.amount, self.interest, self.m, str(self.dex))
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment eru ráðstöfunartekjur, heil tala >= 0
	# Eftir:  p er array sem sýnir þróun lánsins m.v. að aukalega sé greitt
	#		  payment krónur inn á reikninginn
	def progression(self, payment):
		principle = self.amount
		months = self.m
		index = pow(1.04, 1.0/12.0)
		interest = pow(i, 1.0/12.0)
		array = []
		for i in range(0,m):
			fee = int(round((1.0*principle)/(months-i)))
			array.append(fee)
			principle -= fee
			principle -= payment
			principle = principle*index
			principle = principle*interest
		return array
	
	# Notkun: i = interestM(payment, months)
	# Fyrir:  payment er heil tala >=0, months er heiltala >0.
	# Eftir:  i er heildarvextir í krónum á tímabilinu months, m.v. payment krónur aukalega í afborgun mánaðarlega.
	def interestM(self, payment, months):
		prog = self.progression(payment, months)
		return sum(prog[0:months])-round(self.amount*((1.0*months)/self.m))
		
	# Notkun: i = totInterest(payment)
	# Fyrir:  payment er heiltala >= 0
	# Eftir:  i eru heildarvextir í krónum á öllu láninu.
	def totInterest(self, payment):
		return self.interestM(payment, self.m)

### Fann ekki útúr github almennilega svo ég editaði bara, þarf að breyta restinni af kóðanum til að styðja þennan klasa!!


# Klasi fyrir sparnaðarreikninga
class SavingsAcct:
	# Notkun: s = SavingsAcct(name, amount, interest, pay)
	# Fyrir:  amount, interest og pay eru tölur (interest er á brotaformi
	# 	  EKKI á prósentuformi, þ.e. 0.05 í stað 5%), name er strengur
	# Eftir:  s er sparnaðarreikningur/bók með nafnið name, höfuðstól amount, 
	#	  vexti interest og mánaðarlega innborgun pay
	def __init__(self, name, amount, interest, pay):
		self.amount = amount
		self.interest = interest
		self.name = name
		self.pay = pay

	# Notkun: print(s)
	# Fyrir:  s er sparnaðarreikningur
	# Eftir:  reikningurinn er prentaður á skjáinn
	def __str__(self):
		return "Reikningur: %s Inneign: %d Vextir: %f Mánaðarlegur sparnaður: %d" % (self.name, self.amount, self.interest, self.pay)
	
	# Notkun: s.changePay(newPay)
	# Fyrir:  newPay er tala
	# Eftir:  s.pay = newPay
	def changePay(newPay):
		self.pay = newPay


# Notkun: resetFile(filename)
# Eftir:  Skráin filename er tóm 
def resetFile(filename):
	storage = open(filename, 'w')


# Föll til að geyma og ná í lán

# Notkun: storeLoan(l)
# Fyrir:  l er lán
# Eftir:  l hefur verið geymt í skránni 'loans.txt' á forminu 'name-amount-interest-pay', eitt lán í línu
def storeLoan(l):
	storage = open('loans.txt', 'a')
	storage.write('%s-%d-%f-%d\n' % (l.name, l.amount, l.interest, l.pay)) # þarf að breyta, þurfum ekki pay, þurfum í staðin tíma sem er eftir af láninu og hvort hann sé verðtryggður.

# Notkun: storeAllLoans(l)
# Fyrir:  l er listi af lánum
# Eftir:  'loans.txt' er tæmd og öll lánin í l hafa verið sett í skrána 'loans.txt'
def storeAllLoans(l):
	resetFile('loans.txt')
	for n in range(0, len(l)):
		storeLoan(l[n])


# Notkun: loans = loadLoans()
# Eftir:  loans er listi af öllum geymdum lánum
def loadLoans():
	loans = []
	for line in open('loans.txt'):
		args = line.split('-')
		loans = loans + [Loan(args[0], int(args[1]), float(args[2]), int(args[3])]
	return loans


# Föll til að geyma og ná í reikninga

# Notkun: storeSAcct(s)
# Fyrir:  s er reikningur
# Eftir:  s er geymdur í 'savings.txt' á forminu name-amount-interest-pay, einn reikningur í línu
def storeSAcct(s):
	storage = open('savings.txt', 'a')
	storage.write('%s-%d-%f-%d\n' % (s.name, s.amount, s.interest, s.pay))

# Notkun: storeAllSAccts(s)
# Fyrir:  s er listi af reikningum
# Eftir:  Skráin 'savings.txt' hefur verið tæmd og allir reikningarnir í s settir í hana
def storeAllSAccts(s):
	resetFile('savings.txt', 'a')
	for n in range(0, len(l)):
		storeSAcct(s[n])

# Notkun: accts = loadSAccts()
# Eftir:  accts inniheldur alla reikningana í 'savings.txt'
def loadSAccts():
	SAccts = []
	for line in open('savings.txt'):
		args = line.split('-')
		SAccts = SAccts + [SavingAcct(args[0], int(args[1]), float(args[2]), int(args[3]))]
	return SAccts

if __name__=="__main__":
	l1 = Loan('bílalán', 100000, 0.05)
	l2 = Loan('húsnæðislán', 10000000, 0.04)
	loans = [l1, l2]
	storeAllLoans(loans)
	loans2 = loadLoans()
	print(loans2[0])
