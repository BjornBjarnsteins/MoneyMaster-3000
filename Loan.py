#! /usr/bin/env python
# -*- coding: cp1252 -*-
# Klasi sem skilgreinir l�n sem hlut (�tg�fa Le�s)

import locale
import math
locale.setlocale( locale.LC_ALL, 'icelandic')
class Loan:
	# Notkun: L = Loan(Name, Amount, Interest, Months, Index)
	# Fyrir:  Name er strengur, Amount er heiltala >=0, Interest er heiltala >= 0, Months er heiltala >0 og Index er boolean.
	# Eftir:  L er l�n sem heitir Name, me� h�fu�st�l Amount, Interest �rsvexti, Months t�ma eftir og Index segir til um ver�tryggingu.
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
			vtr = 'J�'
		else:
			vtr = 'Nei'
		return "L�n: %s \nH�fu�st�ll: %s \n�rsvextir: %0.2f \nLengd(m�nu�ir): %d \nVer�tryggt: %s" % (self.name, amount, self.interest, self.m, vtr)
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment,M eru heilar t�lur >= 0
	# Eftir:  p er fylki, fyrsti d�lkur s�nir afborganir af l�ninu m.v. a� aukalega s�u greiddar
	#         payment kr�nur inn � reikninginn m�na�arlega fyrstu M m�nu�ina, annar d�lkur s�nir h�fu�st�l � byrjun hvers m�na�ar
	#         og �ri�ji d�lkur s�nir vexti hvers m�na�ar.
	def progression(self, payment, M):
		principle = self.amount
		months = self.m
		if self.dex:
			index = 0.0435/12.0
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
		
	def printProgression(self, payment, M):
		prog = self.progression(payment, M)
		amount = locale.currency(self.amount, grouping = True)
		print 'H�fu�st�ll � upphafi: '+amount
		for i in range(0,len(prog[0])):
			pay = locale.currency(prog[0][i], grouping = True)
			debt = locale.currency(prog[1][i], grouping = True)
			print 'M�nu�ur %d: \n Afborgun: %s H�fu�st�ll: %s' %(i+1, pay, debt)
	
	# Notkun: p = payProgression(payment,M)
	# Fyrir:  payment,M eru heilt�lur >= 0
	# Eftir:  p er array sem s�nir st��u n� og �r�un grei�slubyr�ar yfir l�nst�mabili� fyrstu M M�nu�ina
	def payProgression(self,payment,M):
		return self.progression(payment,M)[0]
	
	# Notkun: p = debtProgression(payment,M)
	# Fyrir:  payment,M eru heilt�lur >= 0
	# Eftir:  p er array sem s�nir st��u n� og �r�un skuldar yfir l�nst�mabili� fyrstu M M�nu�ina
	def debtProgression(self,payment,M):
		return self.progression(payment,M)[1]
		
	# Notkun: i = totInterest(payment, M)
	# Fyrir:  payment er heiltala >= 0, M er heiltala >=0
	# Eftir:  i eru heildarvextir � kr�num � �llu l�ninu m.v. payment aukaframlag fyrstu M m�nu�ina.
	def totInterest(self, payment, M):
		return round(sum(self.progression(payment,M)[2]))

	# Notkun: i = interestM(payment, m, M)
	# Fyrir:  payment, m og M eru j�kv��ar heilt�lur
	# Eftir:  i eru heildarvextir af l�ninu � kr�num eftir M m�nu�i m.v. a� greiddar s�u payment auka
	#         kr�nur inn � h�fu�st�l fyrstu m m�nu�ina. (�.e. vextir fyrstu M m�nu�a lagg�ir saman)
	def interestM(self, payment, m, M):
		return round(sum(self.progression(payment,M)[2][:M]))


	# Notkun: a = plotLoanDebt(payment, M)
	# Fyrir:  payment og M eru j�kvæ�ar heilt�lur (e�a 0)
	# Eftir:  a[1][n] er sta�a h�fu�st�ls � m�nu�i a[0][n] m.v. payment aukaframlag næstu M m�nu�ina
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
	# Fyrir:  payment og M eru j�kvæ�ar heilt�lur (e�a 0)
	# Eftir:  a[1][n] er grei�slubyr�in � m�nu�i a[0][n] m.v. payment aukaframlag næstu M m�nu�ina
	def datLoanPay(self, payment, M):
		month = range(1,self.m+1)
		pay = self.payProgression(payment,M)
		while len(pay)<len(month):
			pay.append(0.0)
		return [month, pay]
		
		
		
		
		
		
