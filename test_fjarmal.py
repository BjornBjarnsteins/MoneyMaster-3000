# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *

S1 = Savings.Savings('Übersparnaður', 100000, 1.7, True, 12)
S2 = Savings.Savings('Sparigrís', 100000, 3.5, False, 3)
print S1
print
print S2
print

L1 = Loan.Loan('Húsnæðislán', 30000000, 1.3, 240, True)
L2 = Loan.Loan('Yfirdráttur', 150000, 20, 6, False)
print L1
print
print L2

print '\nEf maður borgar 1000 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
S1.printProgression(1000, 6, 12)
print '\nEf maður borgar 0 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
S1.printProgression(1000, 0, 12)
print '\nEf maður borgar 1000 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
S2.printProgression(1000, 6, 12)
print '\nEf maður borgar 0 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
S2.printProgression(1000, 0, 12)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L1.printProgression(1000, 6)
print '\nUppsafnaðir vextir verða:'
print L1.totInterest(1000,6)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L2.printProgression(1000, 0)
print '\nUppsafnaðir vextir verða:'
print L1.totInterest(1000,6)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L1.printProgression(1000, 6)
print '\nUppsafnaðir vextir verða:'
print L1.totInterest(1000,6)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L2.printProgression(1000, 0)
print '\nUppsafnaðir vextir verða:'
print L1.totInterest(1000,6)


print L1.datLoanDebt(1000,12)
print L2.datLoanPay(1000,12)
