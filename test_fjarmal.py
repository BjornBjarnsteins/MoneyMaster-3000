# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *
from Plot import *

S1 = Savings('Übersparnaður', 100000, 1.7, True, 12)
S2 = Savings('Sparigrís', 100000, 3.5, False, 3)

L1 = Loan('Húsnæðislán', 30000000, 1.3, 240, True)
L2 = Loan('Yfirdráttur', 150000, 20, 6, False)
print L1
print
print L2

print S1
print '\nEf maður borgar 1000 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
print S1.printProgression(1000, 6, 12)
print '\nEf maður borgar 0 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
print S1.printProgression(1000, 0, 12)
print '\nMeð því að leggja 1000 kr inn á mánuði inn þá geturðu tekið út eftirfarandi upphæð eftir 12 mánuði:' #Ath verður að hætta að leggja inn svo binditími klárist áður en tekið er út
print S1.saveforM(1000, 12)
print '\nMeð því að leggja 1000 kr inn á mánuði inn þá verður staðan a reikningunum orðin hærri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)
print
print S2
print '\nEf maður borgar 1000 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
print S2.printProgression(1000, 6, 12)
print '\nEf maður borgar 0 kr inn á sparnaðinn næstu 6 mánuði þá verður þróun reikningsins næstu 12 mánuði:'
print S2.printProgression(1000, 0, 12)
print '\nMeð því að leggja 1000 kr inn á mánuði inn þá geturðu tekið út eftirfarandi upphæð eftir 12 mánuði:' #Ath verður að hætta að leggja inn svo binditími klárist áður en tekið er út
print S2.saveforM(1000, 12)
print '\nMeð því að leggja 1000 kr inn á mánuði inn þá verður staðan a reikningunum orðin hærri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L1.printProgression(1000, 6)
print 'Uppsafnaðir vextir verða:'
print L1.totInterest(1000,6)

print '\nEf maður borgar ekkert aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L1.printProgression(1000, 0)
print 'Uppsafnaðir vextir verða:'
print L1.totInterest(1000,0)

print '\nEf maður borgar 1000 kr aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L2.printProgression(1000, 6)
print 'Uppsafnaðir vextir verða:'
print L2.totInterest(1000,6)

print '\nEf maður borgar ekkert aukalega inn á lánið næstu 6 mánuði þá verður þróun láns:'
L2.printProgression(1000, 0)
print 'Uppsafnaðir vextir verða:'
print L2.totInterest(1000,0)

print '\nHvort lánið ættirðu að borga inn á:'
L = compareLoans(L1, L2, 1000, 6)
print L
print '\nHvor sparnaðarreikningurinn er hagstæðari fyrir þig:'
S = compareSavings(S1,S2,1000,6,12)
print S
print '\nHvort er hagstæðara að borga mánaðarlegan sparnað inn á hagstæðari sparnaðinn eða hagstæðara lánið:'
print compareLS(L,S,1000,6)

plotLS(L,S,10000,12)

# Profar storage follin

storeAllLoans([L1, L2])
loans = loadLoans()
print "\n\nProfar loadLoans()"
for n in range(0, len(loans)):
	print loans[n]

print "\n\nProfar loadSAccts()"
savings = loadSAccts()
for n in range(0, len(savings)):
	print savings[n]

print "\n\nProfar getInflation()"
print getInflation()

