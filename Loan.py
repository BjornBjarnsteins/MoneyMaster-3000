#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
		return "Lan: %s Hofudstoll: %d Arsvextir: %f Lengd(manudir): %f Verdtryggt: %s" % (self.name, self.amount, self.interest, self.m, str(self.dex))
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment eru ráðstöfunartekjur, heil tala >= 0
	# Eftir:  p er fylki, fyrsti dálkur sýnir afborganir af láninu m.v. að aukalega séu greiddar
	#		  payment krónur inn á reikninginn mánaðarlega, seinni dálkur sýnir höfuðstól í byrjun hvers mánaðar.
	def progression(self, payment):
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
			debt.append(principle)
			fee = (1.0*principle)/(months-i)
			i += 1
			principle -= fee
			payment = min(payment,principle)
			principle -= payment
			pay.append(fee+payment)
			principle = principle*index
			principle = principle*interest
		
		while i<months:
			pay.append(0)
			debt.append(0)
			
		return [pay,debt]
	# Notkun: p = payProgression(payment,M)
	# Fyrir:  payment,M eru heiltölur >= 0
	# Eftir:  p er array sem sýnir stöðu nú og þróun greiðslubyrðar yfir lánstímabilið fyrstu M Mánuðina
	def payProgression(self,payment,M):
		pay = self.progression(payment)[0][:M+1]
		while len(pay) < M+1:
			pay.append(0)
		return pay
	
	# Notkun: p = debtProgression(payment,M)
	# Fyrir:  payment,M eru heiltölur >= 0
	# Eftir:  p er array sem sýnir stöðu nú og þróun skuldar yfir lánstímabilið fyrstu M Mánuðina
	def debtProgression(self,payment,M):
		dept = self.progression(payment)[1][:M+1]
		while len(debt) < M+1:
			debt.append(0)
		return pay
	
	# Notkun: i = interestM(payment, months)
	# Fyrir:  payment er heil tala >=0, months er heiltala með 0<=months<=tímabil láns.
	# Eftir:  i er heildar umframgreiðsla í krónum á tímabilinu months, m.v. payment krónur aukalega í afborgun mánaðarlega.
	def interestM(self, payment, months):
		prog = self.payProgression(payment)
		control = min(self.m,months)
		m = min(len(prog),months)
		return (sum(prog[0:m])-self.amount*((1.0*control)/self.m))
		
	# Notkun: i = totInterest(payment)
	# Fyrir:  payment er heiltala >= 0
	# Eftir:  i eru heildarvextir í krónum á öllu láninu.
	def totInterest(self, payment):
		m = self.m
		return self.interestM(payment, m)
