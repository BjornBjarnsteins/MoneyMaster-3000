# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *
import numpy as np
from matplotlib.pyplot import *

#Notkun: plotPayProg(L, monthly, m)
#Fyrir: L er Loan hlutur, monthly,m>=0 heiltölur
#Eftir: plottar tvö gröf á sömu mynd af niðurgreiðslu láns sem fall af tíma.
#       Annað grafið miðast við að greitt sé aukalega mánaðarlegur sparnaður inn
#       á lánið í m mánuði, hitt miðast við að ekkert sé greitt aukalega.
def plotPayProg(monthly, m):
    #Hjálparfall ur Loan: datPayProg(monthly,m)
    return
#Notkun:[Mynd1, Mynd2] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar tveimur myndum með tveimur gröfum hvert:
#       Mynd1: Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#               Miðast við að greitt sé aukalega upphæð monthly inn a lánið í m mánuði.
#       Mynd2: Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#               Miðast við að greitt sé aukalega upphæð monthly inn a sparnað i m mánuði.
def plotLS(L,S,monthly,m):
    #Case1: Borgum niður lán:
    Lx = L.datLoanDebt(monthly, m)
    n = len(L.payProgression(monthly,m))
    N = max(m-n-1,0)
    Sx = S.datSavings2(L.baseFee, monthly, n+1, N, L.m)

    plot(Lx[0],Lx[1])
    plot(Sx[0],Sx[1])

    show()
    
    return
    #Hjálparföll: datDebtProg
    #             datSavings (Ath eftir að útfæra betur!!)

#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar mynd með tveimur gröfum:
#       Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#       Miðast við að greitt sé aukalega upphæð monthly inn a lánið í m mánuði.       
def plotLoverS(L,S,monthly,m):
    return
#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar mynd með tveimur gröfum:
#       Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#       Miðast við að greitt sé aukalega upphæð monthly inn a sparnað í m mánuði.       
def plotSoverL(L,S,monthly,m):
    return
