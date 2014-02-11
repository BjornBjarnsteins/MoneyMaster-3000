# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *

#Notkun: plotPayProg(L, monthly, m)
#Fyrir: L er Loan hlutur, monthly,m>=0 heiltölur
#Eftir: plottar tvö gröf á sömu mynd af niðurgreiðslu láns sem fall af tíma.
#       Annað grafið miðast við að greitt sé aukalega mánaðarlegur sparnaður inn
#       á lánið í m mánuði, hitt miðast við að ekkert sé greitt aukalega.
def plotPayProg(monthly, m):
    #Hjálparfall ur Loan: datPayProg(monthly,m)
    
#Notkun:[Mynd1, Mynd2] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar tveimur myndum með tveimur gröfum hvert:
#       Mynd1: Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#               Miðast við að greitt sé aukalega upphæð monthly inn a lánið í m mánuði.
#       Mynd2: Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#               Miðast við að greitt sé aukalega upphæð monthly inn a sparnað i m mánuði.
def plotLS(L,S,monthly,m):
    #Hjálparföll: datDebtProg
    #             datSavings (Ath eftir að útfæra betur!!)

#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar mynd með tveimur gröfum:
#       Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#       Miðast við að greitt sé aukalega upphæð monthly inn a lánið í m mánuði.       
def plotLoverS(L,S,monthly,m):

#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltölur.
#Eftir: Skilar mynd með tveimur gröfum:
#       Höfuðstóll láns og inneign sparnaðar sem fall af tíma.
#       Miðast við að greitt sé aukalega upphæð monthly inn a sparnað í m mánuði.       
def plotSoverL(L,S,monthly,m):

