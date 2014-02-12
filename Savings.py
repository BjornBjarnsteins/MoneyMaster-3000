# -*- coding: cp1252 -*-
import math
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')

class Savings:
    
    #Notkun: r = Savings(name, amount, interest, index, bound)
    #Fyrir: name er strengur, amount,interest,bound>=0 rauntolur, index boolean
    #Eftir: r er reikningur med heitid name, upphaflega innistaedu amount, vexti interest%, verdtryggdur ef index=True, annars overdtryggdur og binditima bound manudir. 
    def __init__(self, name, amount, interest, index, bound):
        self.n = name
        self.a = amount
        self.p = interest/100.0
        self.dex = index
        self.b = bound
        self.influx = 0.0435  #Medalverdbolga 2011-2013
        self.minflux = 0.0435/12.0
        self.mrates = self.p/12.0 #manadarlegir vextir reiknadir ut fra arsvoxtum

        if(index):
            self.adjustedp = (1+self.mrates)*(1+self.minflux)-1
        else:
            self.adjustedp = self.mrates
    

    #Notkun: print s eda a = str(s)
    #Fyrir: Savings hlutur, Manudur er 30 dagar
    #Eftir: a er strengur sem heldur utan um allar upplysingar um s
    def __str__(self):

        if self.dex:
            indexed = 'Ja'
        else:
            indexed = 'Nei'

        interest = self.p*100

        bound = ""
        if(self.b%12 != self.b):
            years = int(self.b/12-self.b%12)
            rest = self.b-years*12
            months = int(math.floor(rest))
            days = int((rest-months)*30)
            bound = '%d ar, %d manudir, %d dagar' %(years, months, days)
        elif(math.floor(self.b) != 0):
            months = int(math.floor(self.b))
            days = int((self.b-months)*30)
            bound = '%d manudir, %d dagar' %(months, days)
        else: 
            days = int(self.b*30)
            bound = str(days)+' dagar'
        
        amount = locale.currency(self.a, grouping = True)
        
        return 'Sparnadarreikningur: %s \nStada: %s \nÁrsvextir: %0.2f%s \nVerdtrygging: %s \nBinditimi: %s' %(self.n, amount, interest,'%', indexed, bound)

    #Notkun: data = progression(monthly,M)
    #Fyrir: monthly>=0 rauntala, M>0 heiltala G.r.f. ad tad se januar
    #Eftir: data heldur utan um stodu sparnadarreiknings fra upphafsstodu og naestu M manudi tar a eftir
    #       tar sem upphaed monthly hefur verid logd inn hvern manud.
    def progression(self, monthly, m, M):

        total = self.a
        collectedInt = 0
        prog = [[total,0]] #setjum inn upphafsstodu reiknings i fyrsta saetid og uppsafnada vexti
        for i in range(0,m): #naestu m manudina leggjum vid upphaed monthly inn a reikninginn.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            total = (total+monthly)
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])

        for i in range(m,M): #sidustu M-m manudina leggjum vid ekkert inn a reikninginn og sjaum hvernig hann troast adeins a voxtum.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])
            
        return prog

    #Útgafa af progression fallinu tar sem reikning er leyft ad avaxtast i n-1 manudi, og a n-ta manudi er byrjad ad borga inn upphaed monthly naestu m manudina. Skodum stoduna eftir M manudi.
    def progression2(self, loanFee, monthly, n, m, M):
        prog1 = self.progression(0, M, M)
        temp = Savings('Temp', 0, self.p*100, self.dex, self.b)
        prog2 = temp.progression(monthly+loanFee, m, M-n+1)
        prog3 = temp.progression(loanFee,M-n+1-m,M-n+1-m)
        prog = []
        for element in prog1:
            prog.append(element)

        for i in range(0,len(prog2)):
            prog[n-1+i][0] += prog2[i][0]
            prog[n-1+i][1] += prog2[i][1]

        for i in range(0,len(prog3)):
            prog[n-1+m+i][0] += prog3[i][0]
            prog[n-1+m+i][1] += prog3[i][1]
            
        return prog
        
    def printProgression(self, monthly, m, M):
        prog = self.progression(monthly, m, M)
        s = ''
        print 'Upphafsstada: %s' %(locale.currency(prog[0][0], grouping=True))
        for i in range(1,len(prog)):
            amount = locale.currency(prog[i][0], grouping = True)
            collectedInt = locale.currency(prog[i][1], grouping = True)
            print 'Manudur %d: \n Stada: %s Uppsafnadir vextir: %s' %(i, amount, collectedInt)

    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 rauntolur
    #Eftir: m er upphaed sem tekist hefur ad safna a M manudum med monthly sparnadi a manudi og ma taka ut strax.
    def saveforM(self, monthly, M):
        m = max(int(math.floor(M-self.b)),0) #spara med tvi ad leggja fyrir reglulega i m man
        prog = self.progression(monthly, m, M)
        return prog[M][0]


    #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 rauntolur
    #Eftir: m er fjoldi manada sem tad tekur ad safna upp X pening a reikning t.a. tad megi taka hann ut strax.
    def saveuptoX(self, monthly, X):

        total = self.a
        n = int(math.ceil(self.b))
        Y = X/math.pow(1+self.adjustedp,n)

        m = 0
        while(total < Y):
            total = (total+monthly)*(1+self.adjustedp)
            m = m+1

        return m+n
		
    # Notkun: a = plotSavings(payment, m, M)
    # Fyrir:  payment, m og M eru jakvaedar heiltolur (eda 0)
    # Eftir:  a[1][n] er stada reiknings+uppsafnadir vextir a manudi a[0][n] m.v. payment aukaframlag naestu m manudina litid til M manuda
    def datSavings(self, monthly, m, M):
        month = range(1,M+1)
        status = self.progression(monthly, m, M)[1:]
        amount = []
        for i in status:
            amount.append(sum(i))
        return [month, amount]

    def datSavings2(self, baseFee, monthly, n, m, M):
        prog = self.progression2(baseFee, monthly, n, m, M)[1:]
        
        month = range(1,M+1)
        amount = []
        for i in prog:
            amount.append(sum(i))
        return [month, amount]
