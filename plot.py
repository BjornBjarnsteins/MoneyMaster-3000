# -*- coding: cp1252 -*-
from Savings import *
from Loan import *
from Calculator import *

#Notkun: plotPayProg(L, monthly, m)
#Fyrir: L er Loan hlutur, monthly,m>=0 heilt�lur
#Eftir: plottar tv� gr�f � s�mu mynd af ni�urgrei�slu l�ns sem fall af t�ma.
#       Anna� grafi� mi�ast vi� a� greitt s� aukalega m�na�arlegur sparna�ur inn
#       � l�ni� � m m�nu�i, hitt mi�ast vi� a� ekkert s� greitt aukalega.
def plotPayProg(monthly, m):
    #Hj�lparfall ur Loan: datPayProg(monthly,m)
    
#Notkun:[Mynd1, Mynd2] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heilt�lur.
#Eftir: Skilar tveimur myndum me� tveimur gr�fum hvert:
#       Mynd1: H�fu�st�ll l�ns og inneign sparna�ar sem fall af t�ma.
#               Mi�ast vi� a� greitt s� aukalega upph�� monthly inn a l�ni� � m m�nu�i.
#       Mynd2: H�fu�st�ll l�ns og inneign sparna�ar sem fall af t�ma.
#               Mi�ast vi� a� greitt s� aukalega upph�� monthly inn a sparna� i m m�nu�i.
def plotLS(L,S,monthly,m):
    #Hj�lparf�ll: datDebtProg
    #             datSavings (Ath eftir a� �tf�ra betur!!)

#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heilt�lur.
#Eftir: Skilar mynd me� tveimur gr�fum:
#       H�fu�st�ll l�ns og inneign sparna�ar sem fall af t�ma.
#       Mi�ast vi� a� greitt s� aukalega upph�� monthly inn a l�ni� � m m�nu�i.       
def plotLoverS(L,S,monthly,m):

#Notkun: [Mynd] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heilt�lur.
#Eftir: Skilar mynd me� tveimur gr�fum:
#       H�fu�st�ll l�ns og inneign sparna�ar sem fall af t�ma.
#       Mi�ast vi� a� greitt s� aukalega upph�� monthly inn a sparna� � m m�nu�i.       
def plotSoverL(L,S,monthly,m):

