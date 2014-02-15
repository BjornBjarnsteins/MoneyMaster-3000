#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Module sem ser um geymslu lana, sparnadar, og manadarlegs sparnadar
import Savings
import Loan
from xlrd import *

#

# Notkun: resetFile(filename)
# Eftir:  Skrain filename er tom 
def resetFile(filename):
	storage = open(filename, 'w')


# Foll til ad geyma og na i lan

# Notkun: storeLoan(l)
# Fyrir:  l er lan
# Eftir:  l hefur verid geymt i skranni 'loans.txt' a forminu 'name-amount-interest-months-index', eitt lan i linu
def storeLoan(l):
	storage = open('loans.txt', 'a')
	storage.write('%s-%d-%f-%d-%s\n' % (l.name, l.amount, l.interest, l.m, l.dex)) 

# Notkun: storeAllLoans(l)
# Fyrir:  l er listi af lanum
# Eftir:  'loans.txt' er taemd og oll lanin i l hafa verid sett i skrana 'loans.txt'
def storeAllLoans(l):
	resetFile('loans.txt')
	for n in range(0, len(l)):
		storeLoan(l[n])


# Notkun: loans = loadLoans()
# Eftir:  loans er listi af ollum geymdum lanum
def loadLoans():
	loans = []
	for line in open('loans.txt'):
		args = line.split('-')
		loans = loans + [Loan.Loan(args[0], int(args[1]), float(args[2]), int(args[3]), args[4]==1)]
	return loans


# Foll til ad geyma og na i reikninga

# Notkun: storeSAcct(s)
# Fyrir:  s er reikningur
# Eftir:  s er geymdur i 'usersavings.txt' a forminu name-amount-interest-pay-index-bound, einn reikningur i linu
def storeSAcct(s):
	storage = open('usersavings.txt', 'a')
	storage.write('%s-%d-%f-%s-%f\n' % (s.n, s.a, s.p*100, s.dex, s.b))

# Notkun: storeAllSAccts(s)
# Fyrir:  s er listi af reikningum
# Eftir:  Skrain 'usersavings.txt' hefur verid taemd og allir reikningarnir i s settir i hana
def storeAllSAccts(s):
	resetFile('usersavings.txt')
	for n in range(0, len(l)):
		storeSAcct(s[n])

# Notkun: accts = loadSAccts()
# Eftir:  accts inniheldur alla reikningana i 'savings.txt'
def loadSAccts():
	SAccts = []
	for line in open('savings.txt'):
		args = line.split('-')
		SAccts = SAccts + [Savings.Savings(args[0], int(args[1]), float(args[2]), args[3]==1, int(args[4]))]
	for line in open('usersavings.txt'):
		args = line.split('-')
		SAccts = SAccts + [Savings.Savings(args[0], int(args[1]), float(args[2]), args[3]==1, int(args[4]))]
	return SAccts

# Foll til ad lesa verdbolguspa

# Notkun: infl = getInflation()
# Eftir:  infl er medalverdbolga seinustu tveggja ara m.v. gogn sem sott
#	  eru af heimasidu sedlabankans
def getInflation():
	# Opnar Excel-skjalid
	infl = open_workbook('infl.xls')
	sheet = infl.sheet_by_index(0)
	inflsum = 0
	for n in range(279, 303):
		inflsum = inflsum + sheet.cell_value(n-1, 1)
	return inflsum/24.0

# Notkun: i = getLastLine(sheet, n)
# Fyrir:  sheet er sida i Excelskjali, n er heiltala
# Eftir:  i er numerid a seinustu linunni i skjalinu eftir linu n
def getLastLine(sheet, n):
	while (True):	
		if sheet.cell(n, 0) == empty_cell:
			return n-1
		else:
			n = n+1

if __name__=="__main__":
#	l1 = Loan.Loan('bilalan', 100000, 0.05, 5, 1)
#	l2 = Loan.Loan('husnaedislan', 10000000, 0.04, 10, 0)
#	loans = [l1, l2]
#	storeAllLoans(loans)
#	loans2 = loadLoans()
#	print(loans2[0])
#	print(loans2[1])

#	s = loadSAccts()
#	print s[0]

	print getInflation()
