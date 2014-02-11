# -*- coding: cp1252 -*-
import math
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')

class Savings:
    
    #Notkun: r = Savings(name, amount, interest, index, bound)
    #Fyrir: name er strengur, amount,interest,bound>=0 rauntölur, index boolean
    #Eftir: r er reikningur með heitið name, upphaflega innistæðu amount, vexti interest%, verðtryggður ef index=True, annars óverðtryggður og binditíma bound mánuðir. 
    def __init__(self, name, amount, interest, index, bound):
        self.n = name
        self.a = amount
        self.p = interest/100.0
        self.dex = index
        self.b = bound
        self.influx = 0.0435  #Meðalverðbólga 2011-2013
        self.minflux = 0.0435/12.0
        self.mrates = self.p/12.0 #mánaðarlegir vextir reiknaðir út frá ársvöxtum

        if(index):
            self.adjustedp = (1+self.mrates)*(1+self.minflux)-1
        else:
            self.adjustedp = self.mrates
    

    #Notkun: print s eða a = str(s)
    #Fyrir: Savings hlutur, Mánuður er 30 dagar
    #Eftir: a er strengur sem heldur utan um allar upplýsingar um s
    def __str__(self):

        if self.dex:
            indexed = 'Já'
        else:
            indexed = 'Nei'

        interest = self.p*100

        bound = ""
        if(self.b%12 != self.b):
            years = int(self.b/12-self.b%12)
            rest = self.b-years*12
            months = int(math.floor(rest))
            days = int((rest-months)*30)
            bound = '%d ár, %d mánuðir, %d dagar' %(years, months, days)
        elif(math.floor(self.b) != 0):
            months = int(math.floor(self.b))
            days = int((self.b-months)*30)
            bound = '%d mánuðir, %d dagar' %(months, days)
        else: 
            days = int(self.b*30)
            bound = str(days)+' dagar'
        
        amount = locale.currency(self.a, grouping = True)
        
        return 'Sparnaðarreikningur: %s \nStaða: %s \nÁrsvextir: %0.2f%s \nVerðtrygging: %s \nBinditími: %s' %(self.n, amount, interest,'%', indexed, bound)

    #Notkun: data = progression(monthly,M)
    #Fyrir: monthly>=0 rauntala, M>0 heiltala G.r.f. að það sé janúar
    #Eftir: data heldur utan um stöðu sparnaðarreiknings frá upphafsstöðu og næstu M mánuði þar a eftir
    #       þar sem upphæð monthly hefur verið lögð inn hvern mánuð.
    def progression(self, monthly, m, M):

        total = self.a
        collectedInt = 0
        prog = [[total,0]] #setjum inn upphafsstöðu reiknings í fyrsta sætið og uppsafnaða vexti
        for i in range(0,m): #næstu m mánuðina leggjum við upphæð monthly inn a reikninginn.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            total = (total+monthly)
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])

        for i in range(m,M): #síðustu M-m mánuðina leggjum við ekkert inn á reikninginn og sjáum hvernig hann þróast aðeins a vöxtum.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])
            
        return prog

    #Útgáfa af progression fallinu þar sem reikning er leyft að ávaxtast í n-1 mánuði, og á n-ta mánuði er byrjað að borga inn upphæð monthly næstu m mánuðina. Skoðum stöðuna eftir M mánuði.
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
        print 'Upphafsstaða: %s' %(locale.currency(prog[0][0], grouping=True))
        for i in range(1,len(prog)):
            amount = locale.currency(prog[i][0], grouping = True)
            collectedInt = locale.currency(prog[i][1], grouping = True)
            print 'Mánuður %d: \n Staða: %s Uppsafnaðir vextir: %s' %(i, amount, collectedInt)

    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 rauntölur
    #Eftir: m er upphæð sem tekist hefur að safna á M mánuðum með monthly sparnaði á mánuði og má taka út strax.
    def saveforM(self, monthly, M):
        m = max(int(math.floor(M-self.b)),0) #spara með því að leggja fyrir reglulega í m mán
        prog = self.progression(monthly, m, M)
        return prog[M][0]


    #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 rauntölur
    #Eftir: m er fjöldi mánaða sem það tekur að safna upp X pening a reikning þ.a. það megi taka hann út strax.
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
    # Fyrir:  payment, m og M eru jákvæðar heiltölur (eða 0)
    # Eftir:  a[1][n] er staða reiknings+uppsafnaðir vextir á mánuði a[0][n] m.v. payment aukaframlag næstu m mánuðina litið til M mánuða
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
