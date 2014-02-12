# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
#from storage import *
from Plot import *

#Profar Loan og Savings:
S1 = Savings('Ubersparnadur', 100000, 1.7, True, 12)
S2 = Savings('Sparigris', 100000, 3.5, False, 3)

L1 = Loan('Husnaedislan', 30000000, 1.3, 240, True)
L2 = Loan('Yfirdrattur', 450000, 20, 6, False)
print L1
print
print L2

print S1
print '\nEf madur borgar 1000 kr inn a sparnadinn naestu 6 manudi ta verdur troun reikningsins naestu 12 manudi:'
print S1.printProgression(1000, 6, 12)
print '\nEf madur borgar 0 kr inn a sparnadinn naestu 6 manudi ta verdur troun reikningsins naestu 12 manudi:'
print S1.printProgression(1000, 0, 12)
print '\nMed tvi ad leggja 1000 kr inn a manudi inn ta geturdu tekid ut eftirfarandi upphaed eftir 12 manudi:' #Ath verdur ad haetta ad leggja inn svo binditimi klarist adur en tekid er ut
print S1.saveforM(1000, 12)
print '\nMed tvi ad leggja 1000 kr inn a manudi inn ta verdur stadan a reikningunum ordin haerri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)
print
print S2
print '\nEf madur borgar 1000 kr inn a sparnadinn naestu 6 manudi ta verdur troun reikningsins naestu 12 manudi:'
print S2.printProgression(1000, 6, 12)
print '\nEf madur borgar 0 kr inn a sparnadinn naestu 6 manudi ta verdur troun reikningsins naestu 12 manudi:'
print S2.printProgression(1000, 0, 12)
print '\nMed tvi ad leggja 1000 kr inn a manudi inn ta geturdu tekid ut eftirfarandi upphaed eftir 12 manudi:' #Ath verdur ad haetta ad leggja inn svo binditimi klarist adur en tekid er ut
print S2.saveforM(1000, 12)
print '\nMed tvi ad leggja 1000 kr inn a manudi inn ta verdur stadan a reikningunum ordin haerri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)

print '\nEf madur borgar 1000 kr aukalega inn a lanid naestu 6 manudi ta verdur troun lans:'
L1.printProgression(1000, 6)
print 'Uppsafnadir vextir verda:'
print L1.totInterest(1000,6)

print '\nEf madur borgar ekkert aukalega inn a lanid naestu 6 manudi ta verdur troun lans:'
L1.printProgression(1000, 0)
print 'Uppsafnadir vextir verda:'
print L1.totInterest(1000,0)

print '\nEf madur borgar 1000 kr aukalega inn a lanid naestu 6 manudi ta verdur troun lans:'
L2.printProgression(1000, 6)
print 'Uppsafnadir vextir verda:'
print L2.totInterest(1000,6)

print '\nEf madur borgar ekkert aukalega inn a lanid naestu 6 manudi ta verdur troun lans:'
L2.printProgression(1000, 0)
print 'Uppsafnadir vextir verda:'
print L2.totInterest(1000,0)

#Profar Calculator
print '\nHvort lanid aettirdu ad borga inn a:'
L = compareLoans(L1, L2, 50000, 3)
print L
print '\nHvor sparnadarreikningurinn er hagstaedari fyrir tig:'
S = compareSavings(S1,S2,50000,3,16)
print S
print '\nHvort er hagstaedara ad borga manadarlegan sparnad inn a hagstaedari sparnadinn eda hagstaedara lanid:'
print compareLS(L,S,50000,3)

#Profar plot
plotLS(L,S,50000,3)
plotPayProg(L,50000,3)

# Profar storage
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

