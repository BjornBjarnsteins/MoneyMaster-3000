#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Klasi sem skilgreinir l�n sem hlut (�tg�fa Le�s)

import locale
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
	
	def __str__(self):
		amount = locale.currency(self.amount, grouping = True)
		return "Lan: %s \nHofudstoll: %s \nArsvextir: %0.2f \nLengd(manudir): %0.2f \nVerdtryggt: %s" % (self.name, amount, self.interest, self.m, str(self.dex))
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment,M eru heilar t�lur >= 0
	# Eftir:  p er fylki, fyrsti d�lkur s�nir afborganir af l�ninu m.v. a� aukalega s�u greiddar
	#		  payment kr�nur inn � reikninginn m�na�arlega fyrstu M m�nu�ina, seinni d�lkur s�nir h�fu�st�l � byrjun hvers m�na�ar.
	def progression(self, payment, M):
		principle = self.amount
		months = self.m
		if self.dex:
			index = pow(1.0435, 1.0/12.0)
		else:
			index = 1
		interest = pow(1+(self.interest/100.0), 1.0/12.0)
		pay = []
		debt = []
		i = 0
		while principle > 0:
			fee = (1.0*principle)/(months-i)
			principle -= fee
			if i<M:
				payment = min(payment,principle)
			else:
				payment = 0
			principle -= payment
			pay.append(fee+payment)
			principle = principle*index
			principle = principle*interest
			debt.append(principle)
			i += 1
			
		return [pay,debt]
	
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
	
	# Notkun: i = interestM(payment, months)
	# Fyrir:  payment er heil tala >=0, months er heil tala >=0, M er heil tala >=0
	# Eftir:  i er heildar umframgrei�sla(�.m.t. vextir) � kr�num � t�mabilinu M, m.v. payment kr�nur aukalega � afborgun m�na�arlega fyrstu months m�nu�ina.
	# def interestM(self, payment, months, M):
		
	# Notkun: i = totInterest(payment, M)
	# Fyrir:  payment er heiltala >= 0, M er heiltala >=0
	# Eftir:  i eru heildarvextir � kr�num � �llu l�ninu m.v. payment aukaframlag fyrstu M m�nu�ina.
	def totInterest(self, payment, M):
		total = sum(self.payProgression(payment,M))
		return (total-self.amount)
	
if __name__ == '__main__':
	L = Loan("tra",2443,1.1,15,True)
	print L
