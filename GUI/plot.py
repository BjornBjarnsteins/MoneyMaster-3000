# -*- coding: utf-8 -*-
from Savings import *
from Loan import *
from Calculator import *
import numpy as np
from matplotlib.pyplot import *

#Notkun: plotPayProg(L, monthly, m)
#Fyrir: L er Loan hlutur, monthly,m>=0 heiltolur
#Eftir: plottar tvo grof a somu mynd af nidurgreidslu lans sem fall af tima.
#       Annad grafid midast vid ad greitt se aukalega manadarlegur sparnadur inn
#       a lanid i m manudi, hitt midast vid ad ekkert se greitt aukalega.
def plotPayProg(L,monthly, m):

    fig = figure(1)
    fig.canvas.set_window_title('Greidslubyrdi lans')
    fig.suptitle('Greidslubyrdi lans')
    p = fig.add_subplot(111, autoscale_on=True)
    
    Lx1 = L.datLoanPay(monthly,m)
    Lx2 = L.datLoanPay(0,0)

    xlim(xmin=1)
    xlim(xmax=L.m)
    A, = p.plot(Lx1[0],Lx1[1])
    B, = p.plot(Lx2[0],Lx2[1])

    l = p.legend([A, B], ['Med aukagreidslum', 'An aukagreidslna'], loc=1)
    
    show()

#Notkun:[Mynd1, Mynd2] = plotLS(L,S,monthly,m)
#Fyrir: L er Loan hlutur, S Savings hlutur, monthly,m>=0 heiltolur.
#Eftir: Skilar tveimur myndum med tveimur grofum hvert:
#       Mynd1: Hofudstoll lans og inneign sparnadar sem fall af tima.
#               Midast vid ad greitt se aukalega upphaed monthly inn a lanid i m manudi.
#       Mynd2: Hofudstoll lans og inneign sparnadar sem fall af tima.
#               Midast vid ad greitt se aukalega upphaed monthly inn a sparnad i m manudi.
def plotLS(L,S,monthly,m):

    fig1 = figure(1)
    fig1.canvas.set_window_title('Samanburdur 1')
    fig1.suptitle('Borgum aukalega inn a hofudstol lans')
    p1 = fig1.add_subplot(111, autoscale_on=True)

    xlim(xmin=1)
    xlim(xmax=L.m)
    xlabel('Manudur')
    ylabel('Hofudstoll / Innistaeda')
    
    fig2 = figure(2)
    fig2.canvas.set_window_title('Samanburdur 2')
    fig2.suptitle('Borgum aukalega inn a sparnadarreikning')
    p2 = fig2.add_subplot(111, autoscale_on=True)
    xlim(xmin=1)
    xlim(xmax=L.m)
    xlabel('Manudur')
    ylabel('Hofudstoll / Innistaeda')

    
    #Case1: Borgum nidur lan:
    Lx = L.datLoanDebt(monthly, m)
    n = len(L.payProgression(monthly,m))
    N = max(m-n-1,0)
    Sx = S.datSavings2(L.baseFee, monthly, n+1, N, L.m)

    A1, = p1.plot(Lx[0],Lx[1], label='Lan')
    B1, = p1.plot(Sx[0],Sx[1], label='Sparnadur')

    l = p1.legend([A1, B1], ['Lan', 'Sparnadur'], loc=1)
    
    #Case2: Borgum inn a sparnadarreikning.
    Lx = L.datLoanDebt(0,m)
    n = len(L.payProgression(0,m))
    Sx = S.datSavings(monthly, m, n)
    A2,= p2.plot(Lx[0],Lx[1])
    B2,= p2.plot(Sx[0],Sx[1])
    m = p2.legend([A2, B2], ['Lan', 'Sparnadur'], loc=1)
    
    show()
