# -*- coding: cp1252 -*-
# Notkun: L = compareLoans(L1, L2, payment, M)
# Fyrir:  L1 og L2 eru hlutir af taginu Loan, payment er heiltala >= 0 og M er rauntala >= 0
# Eftir:  L er �a� l�n sem er hagst��ara a� borga ni�ur fyrst.
from Savings import *
from Loan import *
def compareLoans(L1, L2, payment, M):
    A = L1.totInterest(0,0)-L1.totInterest(payment,M)
    B = L2.totInterest(0,0)-L2.totInterest(payment,M)
    if A > B:
        return L1
    else:
        return L2

#Notkun: s = compareSavings(s1,s2,monthly,M)
#Fyrir: s1,s2 eru Savings hlutir, monthly>=0 rauntala, M>=0 heiltala, s1 og s2 hafa s�mu upphafsinnist��u
#Eftir: s = s1 ef upph�� � s1 a� loknum M m�nu�um me� monthly m�na�arlegum innborgunum er h�rri en a s2.
#       s = s2 annars.
def compareSavings(s1, s2, monthly, m, M):
    x1 = s1.progression(monthly, m, M)
    x2 = s2.progression(monthly, m, M)

    sum1 = sum(x1[M]) #sta�a + uppsafna�ir vextir eftir M m�nu�i
    sum2 = sum(x2[M]) #sta�a + uppsafna�ir vextir eftir M m�nu�i.
    if(sum1 > sum2):
        return s1
    else:
        return s2
    
#Notkun: best = compareAllSavings(s,monthly,M)
#Fyrir: s er array af Savings hlutum, monthly>=0 rauntala, M>=0 heiltala
#Eftir: best er hagst��asti sparna�arreikningurinn af �llum reikningunum � s m.v. compareSavings falli� a� ofan.
def compareAllSavings(s, monthly, m, M):
    n = len(s)
    best = s[0]
    for i in range(1,n):
        best = compareSavings(best,s[i], monthly, m, M)
    
    return best

#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagst��ara er fyrir notanda a� grei�a upph�� monthly inn � l � M m�nu�i, t = s annars
#       'hagst��ara' telst vera meiri eignir a� M m�nu�um loknum.
def compareLS(l,s, monthly, m):

    M = l.m
    m = min(m, M)
    #Case 1: Borgum inn � sparna� en ekki l�n.
    #Tap1 = vextirnir sem safnast upp yfir l�nst�mann.
    #Grodi1 = vextirnir af m�na�arlega framlaginu sem safnast upp a t�mabilinu
    tap1 = -l.totInterest(0,0) #j�kv�� tala
    grodi1 = sum(s.progression(monthly, m, M)[M])-sum(s.progression(0,0,M)[M])-monthly*m
    netto1 = grodi1+tap1

    #Case 2: Borgum inn a l�n en ekki sparna�.
    #Tap2 = vextirnir sem safnast upp yfir l�nst�mann.
    #Gr��i2 = �g��i af �v� a� borga m�na�arlegt framlag inn a sparna�arreikning af �v� loknu a� borga ni�ur l�n
    #       + �g��i af �v� borga hef�bundna afborgun af l�ni inn a sparna�arreikning uns l�nst�ma l�kur.
    T = M-len(l.payProgression(monthly,m))
    t = max(m-T,0)
    tap2 = -l.totInterest(monthly,m)
    grodi2 = sum(s.progression(monthly, t, T)[T])-sum(s.progression(0,0,T)[T])-monthly*t
    grodi2 += sum(s.progression(l.baseFee, T, T)[T])-sum(s.progression(0,0,T)[T])-l.baseFee*T
    netto2 = grodi2+tap2

    if(netto1 > netto2):
        return s
    else:
        return l
    
    
    

