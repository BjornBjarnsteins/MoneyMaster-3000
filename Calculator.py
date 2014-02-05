# -*- coding: cp1252 -*-
# Notkun: L = compareLoans(L1, L2, payment, M)
# Fyrir:  L1 og L2 eru hlutir af taginu Loan, payment er heiltala >= 0 og M er rauntala >= 0
# Eftir:  L er það lán sem er hagstæðara að borga niður fyrst.
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
#Fyrir: s1,s2 eru Savings hlutir, monthly>=0 rauntala, M>=0 heiltala, s1 og s2 hafa sömu upphafsinnistæðu
#Eftir: s = s1 ef upphæð á s1 að loknum M mánuðum með monthly mánaðarlegum innborgunum er hærri en a s2.
#       s = s2 annars.
def compareSavings(s1, s2, monthly, m, M):
    x1 = s1.progression(monthly, m, M)
    x2 = s2.progression(monthly, m, M)

    sum1 = sum(x1[M]) #staða + uppsafnaðir vextir eftir M mánuði
    sum2 = sum(x2[M]) #staða + uppsafnaðir vextir eftir M mánuði.
    if(sum1 > sum2):
        return s1
    else:
        return s2
    
#Notkun: best = compareAllSavings(s,monthly,M)
#Fyrir: s er array af Savings hlutum, monthly>=0 rauntala, M>=0 heiltala
#Eftir: best er hagstæðasti sparnaðarreikningurinn af öllum reikningunum í s m.v. compareSavings fallið að ofan.
def compareAllSavings(s, monthly, m, M):
    n = len(s)
    best = s[0]
    for i in range(1,n):
        best = compareSavings(best,s[i], monthly, m, M)
    
    return best

#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstæðara er fyrir notanda að greiða upphæð monthly inn á l í M mánuði, t = s annars
#       'hagstæðara' telst vera meiri eignir að M mánuðum loknum.
def compareLS(l,s, monthly, m, M):
    m = min(m,M)
    #gróði af því að greiða inn á lán:
    profit1 = l.totInterest(0,0)-l.totInterest(monthly,m)

    t = len(l.payProgression(monthly, m))
    if(t<m):
        extraprofit = sum(s.progression(0, 0, t)[t])+sum(s.progression(monthly+l.baseFee,m-t,m-t)[m-t])+sum(s.progression(l.baseFee,M-m+t,M-m+t)[M-m+t])-3*s.a
    elif(t < M):
        extraprofit = sum(s.progression(0, 0, t)[t])+sum(s.progression(l.baseFee,M-t,M-t)[M-t])-2*s.a
    else:
        extraprofit = sum(s.progression(0, 0, t)[t])-s.a

    profit1 += extraprofit
    profit1 -= monthly*m
	
    #gróði af því að greiða inn á sparnað:
    profit2 = sum(s.progression(monthly,m,M)[M]) - sum(s.progression(0,0,M)[M]) - (monthly*m)
	
    if profit1 > profit2:
    	return l
    else:
        return s
	

    
    
    

