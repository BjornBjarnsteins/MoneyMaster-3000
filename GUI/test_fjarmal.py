# -*- coding: utf-8 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *
from plot import *
import unittest

class testAllFunctions(unittest.TestCase):
	#Testing for Savings.py class
	def testSProgression(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.progression(100, 5, 12)[12],[1500,170])
		self.assertEqual(S.progression(100, 5, 12)[7],[1500,95])
		self.assertEqual(S.progression(100, 5, 12)[4],[1400,50])
	def testSProgression2(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.progression2(0, 100, 5, 3, 12)[12],[1300,141])
		self.assertEqual(S.progression2(50, 100, 5, 3, 12)[7],[1450,79])
		self.assertEqual(S.progression2(0, 100, 5, 3, 12)[4],[1000,40])
	def testSaveforM(self):
		S = Savings('Bundinn 2', 1000, 12, False, 2)
		self.assertEqual(S.saveforM(100,2),1000)
		self.assertEqual(S.saveforM(100,4),1200)
		self.assertEqual(S.saveforM(100,14),2398)
	def testSaveuptoX(self):
		S = Savings('Bundinn 2', 1000, 12, False, 2)
		self.assertEqual(S.saveuptoX(100,1000),0)
		self.assertEqual(S.saveuptoX(100,1200),4)
		self.assertEqual(S.saveuptoX(100,2398),14)
	def testDatSavings(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.datSavings(100,5,12)[1][3],1450)
		self.assertEqual(S.datSavings(100,5,12)[1][6],1595)
		self.assertEqual(S.datSavings(100,5,12)[1][11],1670)
		self.assertEqual(S.datSavings(100,5,12)[0][6],7)
	def testDatSavings2(self):
		S = Savings('Sparigrís', 1000, 12, False, 0)
		self.assertEqual(S.datSavings2(0,100,5,3,12)[1][3],1040)
		self.assertEqual(S.datSavings2(50,100,5,3,12)[1][6],1529)
		self.assertEqual(S.datSavings2(0,100,5,3,12)[1][11],1441)
		
	#Testing for Loan.py class
	def testLProgression(self):
		L = Loan('Yfirdráttur', 120000, 24, 12, False)
		self.assertEqual(L.progression(1000, 5)[1][12],0)
		self.assertEqual(L.progression(1000, 5)[1][4],76000)
		self.assertEqual(L.progression(1000, 5)[0][11],5100)
		self.assertEqual(L.progression(1000, 5)[0][3],12740)
		self.assertEqual(round(L.progression(1000, 5)[2][11]),100.0)
		self.assertEqual(round(L.progression(1000, 5)[2][3]),1740.0)
		
	
		

if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)