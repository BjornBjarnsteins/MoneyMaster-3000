#! /usr/bin/env python
# -*- coding: cp1252 -*-
# Module sem sér um geymslu lána, sparnaðar, og mánaðarlegs sparnaðar
import Savings
import Loan


#

# Notkun: resetFile(filename)
# Eftir:  Skráin filename er tóm 
def resetFile(filename):
	storage = open(filename, 'w')


# Föll til að geyma og ná í lán

# Notkun: storeLoan(l)
# Fyrir:  l er lán
# Eftir:  l hefur verið geymt í skránni 'loans.txt' á forminu 'name-amount-interest-months-index', eitt lán í línu
def storeLoan(l):
	storage = open('loans.txt', 'a')
	storage.write('%s-%d-%f-%d-%s\n' % (l.name, l.amount, l.interest, l.m, l.dex)) 

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
		loans = loans + [Loan.Loan(args[0], int(args[1]), float(args[2]), int(args[3]), args[4]==1)]
	return loans


# Föll til að geyma og ná í reikninga

# Notkun: storeSAcct(s)
# Fyrir:  s er reikningur
# Eftir:  s er geymdur í 'savings.txt' á forminu name-amount-interest-pay, einn reikningur í línu
def storeSAcct(s):
	storage = open('savings.txt', 'a')
	storage.write('%s-%d-%f-%d-%s-%d\n' % (s.name, s.amount, s.interest, s.index, s.bound))

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
		SAccts = SAccts + [Savings.Savings(args[0], int(args[1]), float(args[2]), int(args[3]), args[4]==1, int(args[5]))]
	return SAccts

if __name__=="__main__":
	l1 = Loan.Loan('bílalán', 100000, 0.05, 5, 1)
	l2 = Loan.Loan('húsnæðislán', 10000000, 0.04, 10, 0)
	loans = [l1, l2]
	storeAllLoans(loans)
	loans2 = loadLoans()
	print(loans2[0])
	print(loans2[1])
