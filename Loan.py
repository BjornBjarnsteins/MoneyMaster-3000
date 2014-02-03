#! /usr/bin/env python
# -*- coding: cp1252 -*-
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
		return "Lán: %s Hofudstoll: %d Arsvextir: %f Lengd(manudir): %f Verdtryggt: %s" % (self.name, self.amount, self.interest, self.m, str(self.dex))
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment,M eru heilar tölur >= 0
	# Eftir:  p er fylki, fyrsti dálkur sýnir afborganir af láninu m.v. að aukalega séu greiddar
	#		  payment krónur inn á reikninginn mánaðarlega fyrstu M mánuðina, seinni dálkur sýnir höfuðstól í byrjun hvers mánaðar.
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
	# Fyrir:  payment,M eru heiltölur >= 0
	# Eftir:  p er array sem sýnir stöðu nú og þróun greiðslubyrðar yfir lánstímabilið fyrstu M Mánuðina
	def payProgression(self,payment,M):
		return self.progression(payment,M)[0]
	
	# Notkun: p = debtProgression(payment,M)
	# Fyrir:  payment,M eru heiltölur >= 0
	# Eftir:  p er array sem sýnir stöðu nú og þróun skuldar yfir lánstímabilið fyrstu M Mánuðina
	def debtProgression(self,payment,M):
		return self.progression(payment,M)[1]
	
	# Notkun: i = interestM(payment, months)
	# Fyrir:  payment er heil tala >=0, months er heil tala >=0, M er heil tala >=0
	# Eftir:  i er heildar umframgreiðsla(þ.m.t. vextir) í krónum á tímabilinu M, m.v. payment krónur aukalega í afborgun mánaðarlega fyrstu months mánuðina.
	# def interestM(self, payment, months, M):
		
	# Notkun: i = totInterest(payment, M)
	# Fyrir:  payment er heiltala >= 0, M er heiltala >=0
	# Eftir:  i eru heildarvextir í krónum á öllu láninu m.v. payment aukaframlag fyrstu M mánuðina.
	def totInterest(self, payment, M):
		total = sum(self.payProgression(payment,M))
		return (total-self.amount)