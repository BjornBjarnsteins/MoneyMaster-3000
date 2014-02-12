#! /usr/bin/env python
# -*- coding: cp1252 -*-
# Klasi sem skilgreinir lán sem hlut (útgáfa Leós)

import locale
import math
locale.setlocale( locale.LC_ALL, 'icelandic')
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
		self.baseFee = (amount*1.0)/months
	
	def __str__(self):
		amount = locale.currency(self.amount, grouping = True)
		if self.dex:
			vtr = 'Já'
		else:
			vtr = 'Nei'
		return "Lán: %s \nHöfuðstóll: %s \nÁrsvextir: %0.2f \nLengd(mánuðir): %d \nVerðtryggt: %s" % (self.name, amount, self.interest, self.m, vtr)
	
	# Notkun: p = progression(payment)
	# Fyrir:  payment,M eru heilar tölur >= 0
	# Eftir:  p er fylki, fyrsti dálkur sýnir afborganir af láninu m.v. að aukalega séu greiddar
	#         payment krónur inn á reikninginn mánaðarlega fyrstu M mánuðina, annar dálkur sýnir höfuðstól í byrjun hvers mánaðar
	#         og þriðji dálkur sýnir vexti hvers mánaðar.
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
		print 'Höfuðstóll í upphafi: '+amount
		for i in range(0,len(prog[0])):
			pay = locale.currency(prog[0][i], grouping = True)
			debt = locale.currency(prog[1][i], grouping = True)
			print 'Mánuður %d: \n Afborgun: %s Höfuðstóll: %s' %(i+1, pay, debt)
	
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
		
	# Notkun: i = totInterest(payment, M)
	# Fyrir:  payment er heiltala >= 0, M er heiltala >=0
	# Eftir:  i eru heildarvextir í krónum á öllu láninu m.v. payment aukaframlag fyrstu M mánuðina.
	def totInterest(self, payment, M):
		return round(sum(self.progression(payment,M)[2]))

	# Notkun: i = interestM(payment, m, M)
	# Fyrir:  payment, m og M eru jákvæðar heiltölur
	# Eftir:  i eru heildarvextir af láninu í krónum eftir M mánuði m.v. að greiddar séu payment auka
	#         krónur inn á höfuðstól fyrstu m mánuðina. (þ.e. vextir fyrstu M mánuða laggðir saman)
	def interestM(self, payment, m, M):
		return round(sum(self.progression(payment,M)[2][:M]))


	# Notkun: a = plotLoanDebt(payment, M)
	# Fyrir:  payment og M eru jákvÃ¦ðar heiltölur (eða 0)
	# Eftir:  a[1][n] er staða höfuðstóls á mánuði a[0][n] m.v. payment aukaframlag nÃ¦stu M mánuðina
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
	# Fyrir:  payment og M eru jákvÃ¦ðar heiltölur (eða 0)
	# Eftir:  a[1][n] er greiðslubyrðin á mánuði a[0][n] m.v. payment aukaframlag nÃ¦stu M mánuðina
	def datLoanPay(self, payment, M):
		month = range(1,self.m+1)
		pay = self.payProgression(payment,M)
		while len(pay)<len(month):
			pay.append(0.0)
		return [month, pay]
		
		
		
		
		
		
