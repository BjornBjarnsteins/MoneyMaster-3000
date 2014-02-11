# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
from storage import *

S1 = Savings.Savings('�bersparna�ur', 100000, 1.7, True, 12)
S2 = Savings.Savings('Sparigr�s', 100000, 3.5, False, 3)
print S1
print
print S2
print

L1 = Loan.Loan('H�sn��isl�n', 30000000, 1.3, 240, True)
L2 = Loan.Loan('Yfirdr�ttur', 150000, 20, 6, False)
print L1
print
print L2

print '\nEf ma�ur borgar 1000 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
S1.printProgression(1000, 6, 12)
print '\nEf ma�ur borgar 0 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
S1.printProgression(1000, 0, 12)
print '\nEf ma�ur borgar 1000 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
S2.printProgression(1000, 6, 12)
print '\nEf ma�ur borgar 0 kr inn � sparna�inn n�stu 6 m�nu�i �� ver�ur �r�un reikningsins n�stu 12 m�nu�i:'
S2.printProgression(1000, 0, 12)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L1.printProgression(1000, 6)
print '\nUppsafna�ir vextir ver�a:'
print L1.totInterest(1000,6)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L2.printProgression(1000, 0)
print '\nUppsafna�ir vextir ver�a:'
print L1.totInterest(1000,6)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L1.printProgression(1000, 6)
print '\nUppsafna�ir vextir ver�a:'
print L1.totInterest(1000,6)

print '\nEf ma�ur borgar 1000 kr aukalega inn � l�ni� n�stu 6 m�nu�i �� ver�ur �r�un l�ns:'
L2.printProgression(1000, 0)
print '\nUppsafna�ir vextir ver�a:'
print L1.totInterest(1000,6)


print L1.datLoanDebt(1000,12)
print L2.datLoanPay(1000,12)
