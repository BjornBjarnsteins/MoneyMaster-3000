# -*- coding: utf-8 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *
from plot import *
import unittest

class testAllFunctions(unittest.TestCase):
	#Testing for Savings.py
	#UT01
	#Markmið: Nota stikkprufur til að prufa Savings.progression
	def testSProgression_UT01(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.progression(100, 5, 12)[12],[1500,170])
		self.assertEqual(S.progression(100, 5, 12)[7],[1500,95])
		self.assertEqual(S.progression(100, 5, 12)[4],[1400,50])
	#UT02
	#Markmið: Nota stikkprufur til að prufa Savings.progression2
	def testSProgression2_UT02(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.progression2(0, 100, 5, 3, 12)[12],[1300,141])
		self.assertEqual(S.progression2(50, 100, 5, 3, 12)[7],[1450,79])
		self.assertEqual(S.progression2(0, 100, 5, 3, 12)[4],[1000,40])
	#UT03
	#Markmið: Nota stikkprufur til að prufa Savings.saveforM
	def testSaveforM_UT03(self):
		S = Savings('Bundinn 2', 1000, 12, False, 2)
		self.assertEqual(S.saveforM(100,2),1000)
		self.assertEqual(S.saveforM(100,4),1200)
		self.assertEqual(S.saveforM(100,14),2398)
	#UT04
	#Markmið: Nota stikkprufur til að prufa Savings.saveuptoX
	def testSaveuptoX_UT04(self):
		S = Savings('Bundinn 2', 1000, 12, False, 2)
		self.assertEqual(S.saveuptoX(100,1000),0)
		self.assertEqual(S.saveuptoX(100,1200),4)
		self.assertEqual(S.saveuptoX(100,2398),14)
	#UT05
	#Markmið: Nota stikkprufur til að prufa Savings.datSavings
	def testDatSavings_UT05(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.datSavings(100,5,12)[1][3],1450)
		self.assertEqual(S.datSavings(100,5,12)[1][6],1595)
		self.assertEqual(S.datSavings(100,5,12)[1][11],1670)
		self.assertEqual(S.datSavings(100,5,12)[0][6],7)
	#UT06
	#Markmið: Nota stikkprufur til að prufa Savings.datSavings2
	def testDatSavings2_UT06(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.datSavings2(0,100,5,3,12)[1][3],1040)
		self.assertEqual(S.datSavings2(50,100,5,3,12)[1][6],1529)
		self.assertEqual(S.datSavings2(0,100,5,3,12)[1][11],1441)
		
	#Testing for Loan.py
	#UT07
	#Markmið: Nota stikkprufur til að prufa Loan.progression
	def testLProgression_UT07(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.progression(1000, 5)[1][12],0)
		self.assertEqual(L.progression(1000, 5)[1][4],76000)
		self.assertEqual(L.progression(1000, 5)[0][11],5100)
		self.assertEqual(L.progression(1000, 5)[0][3],12740)
		self.assertEqual(round(L.progression(1000, 5)[2][11]),100.0)
		self.assertEqual(round(L.progression(1000, 5)[2][3]),1740.0)
	#UT08
	#Markmið: Nota stikkprufur til að prufa Loan.payProgression
	def testLpayProgression_UT08(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.payProgression(1000, 5)[11],5100)
		self.assertEqual(L.payProgression(1000, 5)[3],12740)
	#UT09
	#Markmið: Nota stikkprufur til að prufa Loan.debtProgression
	def testLdebtProgression_UT09(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.debtProgression(1000, 5)[12],0)
		self.assertEqual(L.debtProgression(1000, 5)[4],76000)
	#UT10
	#Markmið: Kanna virkni Loan.totInterest
	def testLtotInterest_UT10(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.totInterest(1000, 5),14700)
	#UT11
	#Markmið: Kanna virkni Loan.interestM
	def testLinterestM_UT11(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.interestM(1000, 5, 9),13800)
	#UT12
	#Markmið: Nota stikkprufur til að prufa Loan.datLoanDebt
	def testLdatLoanDebt_UT12(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(round(L.datLoanDebt(1000, 5)[1][11]),100)
		self.assertEqual(round(L.datLoanDebt(1000, 5)[1][3]),77740)
	#UT13
	#Markmið: Nota stikkprufur til að prufa Loan.datLoanPay
	def testLdatLoanPay_UT13(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(round(L.datLoanPay(1000, 5)[1][11]),5100)
		self.assertEqual(round(L.datLoanPay(1000, 5)[1][3]),12740)
		
	#Testing for Calculator.py
	#UT14
	#Markmið: Kanna virkni Calculator.compareLoans
	def testCcompareLoans_UT14(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		M = Loan('Smálán', 24000, 36, 6, False)
		self.assertEqual(compareLoans(L,M,1000,4),M)
	#UT15
	#Markmið: Kanna virkni Calculator.compareSavings
	def testCcompareSavings_UT15(self):
		S = Savings('Sparigrís', 0, 12, True, 0)
		T = Savings('Debet', 0, 1.2, False, 0)
		self.assertEqual(compareSavings(S,T,10000,5,12),S)
	#UT16
	#Markmið: Kanna virkni Calculator.compareLS
	def testCcompareLS_UT16(self):
		S = Savings('Sparigrís', 0, 12, True, 0)
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(compareLS(L,S,10000,5),L)
		
	#Testing for storage.py
	#UT17
	#Markmið: Kanna virkni storage.save og storage.load falla.
	def testStorage_UT17(self):
		S = Savings('Reikningur_unittest', 0, 12, True, 0)
		L = Loan('Lan_unittest', 120000, 24, 12, False)
		storeSAcct(S)
		storeLoan(L)
		x = False
		y = False
		for i in loadSAccts():
			x = x or (i.n==S.n and i.a==S.a and i.p==S.p and i.dex==S.dex and i.b==S.b)
		for i in loadLoans():
			y = y or (i.name==L.name and i.amount==L.amount and i.interest==L.interest and i.m==L.m and i.dex==L.dex)
		self.assertEqual(x,True)
		self.assertEqual(y,True)
		
	
		

if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)