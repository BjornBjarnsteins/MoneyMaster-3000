#! /usr/bin/env python
# -*- coding: cp1252 -*-
# Module sem s�r um geymslu l�na, sparna�ar, og m�na�arlegs sparna�ar
import Savings
import Loan
import os.path

#

# Notkun: resetFile(filename)
# Eftir:  Skr�in filename er t�m 
def resetFile(filename):
	storage = open(filename, 'w')


# F�ll til a� geyma og n� � l�n

# Notkun: storeLoan(l)
# Fyrir:  l er l�n
# Eftir:  l hefur veri� geymt � skr�nni 'loans.txt' � forminu 'name-amount-interest-months-index', eitt l�n � l�nu
def storeLoan(l):
	storage = open('loans.txt', 'a')
	storage.write('%s-%d-%f-%d-%s\n' % (l.name, l.amount, l.interest, l.m, l.dex)) 

# Notkun: storeAllLoans(l)
# Fyrir:  l er listi af l�num
# Eftir:  'loans.txt' er t�md og �ll l�nin � l hafa veri� sett � skr�na 'loans.txt'
def storeAllLoans(l):
	resetFile('loans.txt')
	for n in range(0, len(l)):
		storeLoan(l[n])

# Notkun: appendAllLoans(l)
# Fyrir:  l er listi af l�num
# Eftir:  'loans.txt' er EKKI t�md og �ll l�nin � l hafa veri� sett � skr�na 'loans.txt'
def appendAllLoans(l):
	for n in range(0, len(l)):
		storeLoan(l[n])

# Notkun: loans = loadLoans()
# Eftir:  loans er listi af �llum geymdum l�num
def loadLoans():
	loans = []
	for line in open('loans.txt'):
		args = line.split('-')
		loans = loans + [Loan.Loan(args[0], int(args[1]), float(args[2]), int(args[3]), args[4])]
	return loans


# F�ll til a� geyma og n� � reikninga

# Notkun: storeSAcct(s)
# Fyrir:  s er reikningur
# Eftir:  s er geymdur � 'savings.txt' � forminu name-amount-interest-pay, einn reikningur � l�nu
def storeSAcct(s):
	if(os.path.isfile('savings.txt')):
		storage = open('savings.txt', 'a')
		storage.write('%s-%d-%f-%d-%s\n' % (s.n, s.a, s.p, s.dex, s.b))

# Notkun: storeAllSAccts(s)
# Fyrir:  s er listi af reikningum
# Eftir:  Skr�in 'savings.txt' hefur veri� t�md og allir reikningarnir � s settir � hana
def storeAllSAccts(s):
	resetFile('savings.txt')
	for n in range(0, len(s)):
		storeSAcct(s[n])

# Notkun: accts = loadSAccts()
# Eftir:  accts inniheldur alla reikningana � 'savings.txt'
def loadSAccts():
	SAccts = []
	for line in open('savings.txt'):
		args = line.split('-')
		SAccts = SAccts + [Savings.Savings(args[0], int(args[1]), float(args[2]), int(args[3]), float(args[4]))]
	return SAccts

if __name__=="__main__":
	
	a = loadLoans()
	for i in a:
		print i
		
