# -*- coding: utf-8 -*-
# Notkun: L = compareLoans(L1, L2, payment, M)
# Fyrir:  L1 og L2 eru hlutir af taginu Loan, payment er heiltala >= 0 og M er rauntala >= 0
# Eftir:  L er tad lan sem er hagstaedara ad borga nidur fyrst.
from Savings import *
from Loan import *
def compareLoans(L1, L2, payment, m):
    M = min(L1.m,L2.m)
    A = L1.interestM(0,0,M)-L1.interestM(payment,m,M)
    B = L2.interestM(0,0,M)-L2.interestM(payment,m,M)
    if A > B:
        return L1
    else:
        return L2

#Notkun: s = compareSavings(s1,s2,monthly,M)
#Fyrir: s1,s2 eru Savings hlutir, monthly>=0 rauntala, M>=0 heiltala, s1 og s2 hafa somu upphafsinnistaedu
#Eftir: s = s1 ef upphaed a s1 ad loknum M manudum med monthly manadarlegum innborgunum er haerri en a s2.
#       s = s2 annars.
def compareSavings(s1, s2, monthly, m, M):
    x1 = s1.progression(monthly, m, M)
    x2 = s2.progression(monthly, m, M)

    sum1 = sum(x1[M]) #stada + uppsafnadir vextir eftir M manudi
    sum2 = sum(x2[M]) #stada + uppsafnadir vextir eftir M manudi.
    if(sum1 > sum2):
        return s1
    else:
        return s2
    
#Notkun: best = compareAllSavings(s,monthly,M)
#Fyrir: s er array af Savings hlutum, monthly>=0 rauntala, M>=0 heiltala
#Eftir: best er hagstaedasti sparnadarreikningurinn af ollum reikningunum i s m.v. compareSavings fallid ad ofan.
def compareAllSavings(s, monthly, m, M):
    n = len(s)
    best = s[0]
    for i in range(1,n):
        best = compareSavings(best,s[i], monthly, m, M)
    
    return best

#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstaedara er fyrir notanda ad greida upphaed monthly inn a l i M manudi, t = s annars
#       'hagstaedara' telst vera meiri eignir ad M manudum loknum.
def compareLS(l,s, monthly, m):

    M = l.m
    m = min(m, M)
    #Case 1: Borgum inn a sparnad en ekki lan.
    #Tap1 = vextirnir sem safnast upp yfir lanstimann.
    #Grodi1 = vextirnir af manadarlega framlaginu sem safnast upp a timabilinu
    tap1 = -l.totInterest(0,0) #jakvaed tala
    grodi1 = sum(s.progression(monthly, m, M)[M])-sum(s.progression(0,0,M)[M])-monthly*m
    netto1 = grodi1+tap1

    #Case 2: Borgum inn a lan en ekki sparnad.
    #Tap2 = vextirnir sem safnast upp yfir lanstimann.
    #Grodi2 = §odi af tvi ad borga manadarlegt framlag inn a sparnadarreikning af tvi loknu ad borga nidur lan
    #       + agodi af tvi borga hefdbundna afborgun af lani inn a sparnadarreikning uns lanstima likur.
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
    
    
    

