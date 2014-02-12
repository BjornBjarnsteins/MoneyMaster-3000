# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *
from Plot import *

S1 = Savings('�bersparna�ur', 100000, 1.7, True, 12)
S2 = Savings('Sparigr�s', 100000, 3.5, False, 3)

L1 = Loan('H�sn��isl�n', 30000000, 1.3, 240, True)
L2 = Loan('Yfirdr�ttur', 150000, 20, 6, False)
print L1
print
print L2

print S1
print '\nEf ma�ur borgar 1000 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
print S1.printProgression(1000, 6, 12)
print '\nEf ma�ur borgar 0 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
print S1.printProgression(1000, 0, 12)
print '\nMe� �v� a� leggja 1000 kr inn � m�nu�i inn �� getur�u teki� �t eftirfarandi upph�� eftir 12 m�nu�i:' #Ath ver�ur a� h�tta a� leggja inn svo bindit�mi kl�rist ��ur en teki� er �t
print S1.saveforM(1000, 12)
print '\nMe� �v� a� leggja 1000 kr inn � m�nu�i inn �� ver�ur sta�an a reikningunum or�in h�rri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)
print
print S2
print '\nEf ma�ur borgar 1000 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
print S2.printProgression(1000, 6, 12)
print '\nEf ma�ur borgar 0 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
print S2.printProgression(1000, 0, 12)
print '\nMe� �v� a� leggja 1000 kr inn � m�nu�i inn �� getur�u teki� �t eftirfarandi upph�� eftir 12 m�nu�i:' #Ath ver�ur a� h�tta a� leggja inn svo bindit�mi kl�rist ��ur en teki� er �t
print S2.saveforM(1000, 12)
print '\nMe� �v� a� leggja 1000 kr inn � m�nu�i inn �� ver�ur sta�an a reikningunum or�in h�rri en 250.000 eftir:'
print S1.saveuptoX(1000, 250000)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L1.printProgression(1000, 6)
print 'Uppsafna�ir vextir ver�a:'
print L1.totInterest(1000,6)

print '\nEf ma�ur borgar ekkert aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L1.printProgression(1000, 0)
print 'Uppsafna�ir vextir ver�a:'
print L1.totInterest(1000,0)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L2.printProgression(1000, 6)
print 'Uppsafna�ir vextir ver�a:'
print L2.totInterest(1000,6)

print '\nEf ma�ur borgar ekkert aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L2.printProgression(1000, 0)
print 'Uppsafna�ir vextir ver�a:'
print L2.totInterest(1000,0)

print '\nHvort l�ni� �ttir�u a� borga inn �:'
L = compareLoans(L1, L2, 1000, 6)
print L
print '\nHvor sparna�arreikningurinn er hagst��ari fyrir �ig:'
S = compareSavings(S1,S2,1000,6,12)
print S
print '\nHvort er hagst��ara a� borga m�na�arlegan sparna� inn � hagst��ari sparna�inn e�a hagst��ara l�ni�:'
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

