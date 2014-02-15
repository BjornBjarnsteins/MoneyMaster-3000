#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Klasi sem skilgreinir lan sem hlut (utgafa Leos)

import locale
import math
import storage
locale.setlocale( locale.LC_ALL, 'icelandic')
class Loan:
	# Notkun: L = Loan(Name, Amount, Interest, Months, Index)
	# Fyrir:  Name er strengur, Amount er heiltala >=0, Interest er heiltala >= 0, Months er heiltala >0 og Index er boolean.
	# Eftir:  L er lan sem heitir Name, med hofudstol Amount, Interest arsvexti, Months tima eftir og Index segir til um verdtryggingu.
	def __init__(self, name, amount, interest, months, index):
		self.name = name
		self.interest = interest
		self.dex = index
		self.amount = amount
		self.m = months
		self.baseFee = (amount*1.0)/months
	
	def __str__(self):
		amount = locale.currency(self.amount, grouping = True)
		if self.dex:
			vtr = 'Ja'
		else:
			vtr = 'Nei'
		return "Lan: %s \nHofudstoll: %s \n�rsvextir: %0.2f \nLengd(manudir): %d \nVerdtryggt: %s" % (self.name, amount, self.interest, self.m, vtr)
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment,M eru heilar tolur >= 0
	# Eftir:  p er fylki, fyrsti dalkur synir afborganir af laninu m.v. ad aukalega seu greiddar
	#         payment kronur inn a reikninginn manadarlega fyrstu M manudina, annar dalkur synir hofudstol i byrjun hvers manadar
	#         og tridji dalkur synir vexti hvers manadar.
	def progression(self, payment, M):
		principle = self.amount
		months = self.m
		if self.dex:
			index = storage.getInflation()/1200.0
		else:
			index = 0
		interest =(self.interest/100.0)/12.0
		pay = []
		intData = []
		debt = [self.amount]
		i = 0
		while principle > 0:
			intPay = principle*((1+index)*(1+interest)-1)
			fee = min(self.baseFee, principle)
			principle -= fee
			if i<M:
				payment = min(payment,principle)
			else:
				payment = 0
			principle -= payment
			pay.append(round(fee+payment+intPay))
			intData.append(intPay)
			debt.append(principle)
			i += 1
			
		return [pay,debt,intData]
	# Notkun: printProgression(payment, M)
	# Fyrir:  payment og M eru jakvaedar heiltolur
	# Eftir:  nidurstodur ur progression(payment, M) eru prentadar ut a snyrtilegan mata i skel.
	def printProgression(self, payment, M):
		prog = self.progression(payment, M)
		amount = locale.currency(self.amount, grouping = True)
		print 'Hofudstoll i upphafi: '+amount
		for i in range(0,len(prog[0])):
			pay = locale.currency(prog[0][i], grouping = True)
			debt = locale.currency(prog[1][i], grouping = True)
			print 'Manudur %d: \n Afborgun: %s Hofudstoll: %s' %(i+1, pay, debt)
	
	# Notkun: p = payProgression(payment,M)
	# Fyrir:  payment,M eru heiltolur >= 0
	# Eftir:  p er array sem synir stodu nu og troun greidslubyrdar yfir lanstimabilid fyrstu M Manudina
	def payProgression(self,payment,M):
		return self.progression(payment,M)[0]
	
	# Notkun: p = debtProgression(payment,M)
	# Fyrir:  payment,M eru heiltolur >= 0
	# Eftir:  p er array sem synir stodu nu og troun skuldar yfir lanstimabilid fyrstu M Manudina
	def debtProgression(self,payment,M):
		return self.progression(payment,M)[1]
		
	# Notkun: i = totInterest(payment, M)
	# Fyrir:  payment er heiltala >= 0, M er heiltala >=0
	# Eftir:  i eru heildarvextir i kronum a ollu laninu m.v. payment aukaframlag fyrstu M manudina.
	def totInterest(self, payment, M):
		return round(sum(self.progression(payment,M)[2]))

	# Notkun: i = interestM(payment, m, M)
	# Fyrir:  payment, m og M eru jakvaedar heiltolur
	# Eftir:  i eru heildarvextir af laninu  kronum eftir M manudi m.v. ad greiddar seu payment auka
	#         kronur inn a hofudstol fyrstu m manudina. (t.e. vextir fyrstu M manuda laggdir saman)
	def interestM(self, payment, m, M):
		return round(sum(self.progression(payment,M)[2][:M]))


	# Notkun: a = plotLoanDebt(payment, M)
	# Fyrir:  payment og M eru jakvædar heiltolur (eda 0)
	# Eftir:  a[1][n] er stada hofudstols a manudi a[0][n] m.v. payment aukaframlag næstu M manudina
	def datLoanDebt(self, payment, M):
		month = range(1,self.m+1)
		debt = self.debtProgression(payment,M)[1:]
		interest = self.progression(payment,M)[2][:len(debt)]
		while len(debt)<len(month):
			debt.append(0.0)
		while len(interest)<len(month):
			interest.append(0.0)
		data = [ debt[i] + interest[i] for i in range(len(month))]
		return [month, debt]
	
	
	# Notkun: a = plotLoanPay(payment, M)
	# Fyrir:  payment og M eru jakvædar heiltolur (eda 0)
	# Eftir:  a[1][n] er greidslubyrdin a manudi a[0][n] m.v. payment aukaframlag næstu M manudina
	def datLoanPay(self, payment, M):
		month = range(1,self.m+1)
		pay = self.payProgression(payment,M)
		while len(pay)<len(month):
			pay.append(0.0)
		return [month, pay]
		
		
		
		
		
		
