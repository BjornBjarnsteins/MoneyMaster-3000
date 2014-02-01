#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Module sem sér um geymslu lána, sparnaðar, og mánaðarlegs sparnaðar

class Loan:
	# Notkun: l = Loan(amount, interest)
	# Fyrir:  amount og interest eru tölur (interest er á brotaformi
	# EKKI á prósentuformi, þ.e. 0.05 í stað 5%), name er strengur
	# Eftir:  l er lán með nafnið name, höfuðstól amount og 
	#	  vexti interest
	def __init__(self, name, amount, interest):
		self.amount = amount
		self.interest = interest
		self.name = name

	# Notkun: print(l)
	# Fyrir:  l er lán
	# Eftir:  lánið er prentað á skjáinn
	def __str__(self):
		return "Lán: %s Höfuðstóll: %d Vextir: %f" % (self.name, self.amount, self.interest)

# Notkun: storeLoan(l)
# Fyrir:  l er lán
# Eftir:  l hefur verið geymt í skránni 'loans.txt' á forminu 'name-amount-interest', eitt lán í línu
def storeLoan(l):
	storage = open('loans.txt', 'a')
	storage.write('%s-%d-%f\n' % (l.name, l.amount, l.interest))

# Notkun: storeAllLoans(l)
# Fyrir:  l er listi af lánum
# Eftir:  Öll lánin í l hafa verið sett í skrána 'loans.txt'
def storeAllLoans(l):
	resetFile('loans.txt')
	for n in range(0, len(l)):
		storeLoan(l[n])

# Notkun: resetFile(filename)
# Eftir:  Skráin filename er tóm 
def resetFile(filename):
	storage = open(filename, 'w')

# Notkun: loans = loadLoans()
# Eftir:  loans er listi af öllum geymdum lánum
def loadLoans():
	loans = []
	for line in open('loans.txt'):
		args = line.split('-')
		loans = loans + [Loan(args[0], int(args[1]), float(args[2]))]
	return loans

if __name__=="__main__":
	l1 = Loan('bílalán', 100000, 0.05)
	l2 = Loan('húsnæðislán', 10000000, 0.04)
	loans = [l1, l2]
	storeAllLoans(loans)
	loans2 = loadLoans()
	print(loans2[0])
