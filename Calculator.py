# -*- coding: cp1252 -*-
# Notkun: L = compareLoans(L1, L2, payment, M)
# Fyrir:  L1 og L2 eru hlutir af taginu Loan, payment er heiltala >= 0 og M er rauntala >= 0
# Eftir:  L er það lán sem er hagstæðara að borga niður fyrst.
from Savings import *
from Loan import *
def compareLoans(L1, L2, payment, M):
    M = min(M,L1.m,L2.m)
    A = L1.interestM(payment,M)
    B = L2.interestM(payment,M)
    if A > B:
        return L2
    else:
        return L1

#Notkun: s = compareSavings(s1,s2,monthly,M)
#Fyrir: s1,s2 eru Savings hlutir, monthly>=0 rauntala, M>=0 heiltala, s1 og s2 hafa sömu upphafsinnistæðu
#Eftir: s = s1 ef upphæð á s1 að loknum M mánuðum með monthly mánaðarlegum innborgunum er hærri en a s2.
#       s = s2 annars.
def compareSavings(s1, s2, monthly, M):
    x1 = s1.progression(monthly, M)
    x2 = s2.progression(monthly, M)

    if(x1[M] < x2[M]):
        return s2
    else:
        return s1
    
#Notkun: best = compareAllSavings(s,monthly,M)
#Fyrir: s er array af Savings hlutum, monthly>=0 rauntala, M>=0 heiltala
#Eftir: best er hagstæðasti sparnaðarreikningurinn af öllum reikningunum í s m.v. compareSavings fallið að ofan.
def compareAllSavings(s, monthly, M):
    n = len(s)
    best = s[0]
    for i in range(1,n):
        best = compareSavings(best,s[i], monthly, M)
    
    return best

#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstæðara er fyrir notanda að greiða upphæð monthly inn á l í M mánuði, t = s annars
#       'hagstæðara' telst vera meiri eignir að M mánuðum loknum.
def compareLS(l,s, monthly, m):
    
    
    #Case 1:
    lProg1 = l.payProgression(0, m)
    M = len(lProg1)
    m = min(m, M)
    sProg1 = s.progression(monthly, m, M)

    profit1 = sProg1[M]-sProg1[0]-(m*monthly)
    loss1 = l.totInterest(0,m)
    d1 = profit1-loss1
    
    #Case 2:
    lProg2 = l.payProgression(monthly, m)
    M = len(lProg2)
    m = min(m, M)
    sProg2 = s.progression(0, m, M)

    profit2 = sProg2[M]-sProg2[0]-(m*monthly)
    loss2 = l.totInterest(monthly,m)
    d2 = profit2-loss2

    if(d1 > d2):
        return s
    else:
        return l

    
    
    

