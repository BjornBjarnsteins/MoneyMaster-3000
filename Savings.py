# -*- coding: cp1252 -*-
import math
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')

class Savings:
    
    #Notkun: r = Savings(name, amount, interest, index, bound)
    #Fyrir: name er strengur, amount,interest,bound>=0 raunt�lur, index boolean
    #Eftir: r er reikningur me� heiti� name, upphaflega innist��u amount, vexti interest%, ver�trygg�ur ef index=True, annars �ver�trygg�ur og bindit�ma bound m�nu�ir. 
    def __init__(self, name, amount, interest, index, bound):
        self.n = name
        self.a = amount
        self.p = interest/100.0
        self.dex = index
        self.b = bound
        self.influx = 0.0435  #Me�alver�b�lga 2011-2013
        self.minflux = 0.0435/12.0
        self.mrates = self.p/12.0 #m�na�arlegir vextir reikna�ir �t fr� �rsv�xtum

        if(index):
            self.adjustedp = self.mrates*self.minflux
        else:
            self.adjustedp = self.mrates
    

    #Notkun: print s e�a a = str(s)
    #Fyrir: Savings hlutur, M�nu�ur er 30 dagar
    #Eftir: a er strengur sem heldur utan um allar uppl�singar um s
    def __str__(self):

        if self.dex:
            indexed = 'J�'
        else:
            indexed = 'Nei'

        interest = self.p*100

        bound = ""
        if(self.b%12 != self.b):
            years = int(self.b/12-self.b%12)
            rest = self.b-years*12
            months = int(math.floor(rest))
            days = int((rest-months)*30)
            bound = '%d �r, %d m�nu�ir, %d dagar' %(years, months, days)
        elif(math.floor(self.b) != 0):
            months = int(math.floor(self.b))
            days = int((self.b-months)*30)
            bound = '%d m�nu�ir, %d dagar' %(months, days)
        else: 
            days = int(self.b*30)
            bound = str(days)+' dagar'
        
        amount = locale.currency(self.a, grouping = True)
        
        return 'Sparna�arreikningur: %s \nSta�a: %s \n�rsvextir: %0.2f%s \nVer�trygging: %s \nBindit�mi: %s' %(self.n, amount, interest,'%', indexed, bound)

    #Notkun: data = progression(monthly,M)
    #Fyrir: monthly>=0 rauntala, M>0 heiltala G.r.f. a� �a� s� jan�ar
    #Eftir: data heldur utan um st��u sparna�arreiknings fr� upphafsst��u og n�stu M m�nu�i �ar a eftir
    #       �ar sem upph�� monthly hefur veri� l�g� inn hvern m�nu�.
    def progression(self, monthly, m, M):

        total = self.a
        collectedInt = 0
        prog = [[total,0]] #setjum inn upphafsst��u reiknings � fyrsta s�ti� og uppsafna�a vexti
        for i in range(0,m): #n�stu m m�nu�ina leggjum vi� upph�� monthly inn a reikninginn.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            total = (total+monthly)
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])

        for i in range(m,M): #s��ustu M-m m�nu�ina leggjum vi� ekkert inn � reikninginn og sj�um hvernig hann �r�ast a�eins a v�xtum.
            if(i%12 == 0):
                total = total+collectedInt
                collectedInt = 0
            
            collectedInt += total*self.adjustedp
            prog.append([int(math.floor(total)), collectedInt])
            
        return prog

    def printProgression(self, monthly, m, M):
        prog = self.progression(monthly, m, M)
        s = ''
        print 'Upphafssta�a: %s' %(locale.currency(prog[0][0], grouping=True))
        for i in range(1,len(prog)):
            amount = locale.currency(prog[i][0], grouping = True)
            collectedInt = locale.currency(prog[i][1], grouping = True)
            print 'M�nu�ur %d: \n Sta�a: %s Uppsafna�ir vextir: %s' %(i, amount, collectedInt)

    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 raunt�lur
    #Eftir: m er upph�� sem tekist hefur a� safna � M m�nu�um me� monthly sparna�i � m�nu�i og m� taka �t strax.
    def saveforM(self, monthly, M):
        m = max(int(math.floor(M-self.b)),0) #spara me� �v� a� leggja fyrir reglulega � m m�n
        prog = self.progression(monthly, m, M)
        return prog[M][0]


    #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 raunt�lur
    #Eftir: m er fj�ldi m�na�a sem �a� tekur a� safna upp X pening a reikning �.a. �a� megi taka hann �t strax.
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
    # Fyrir:  payment, m og M eru j�kv��ar heilt�lur (e�a 0)
    # Eftir:  a[1][n] er sta�a reiknings+uppsafna�ir vextir � m�nu�i a[0][n] m.v. payment aukaframlag n�stu m m�nu�ina liti� til M m�nu�a
    def datSavings(self, payment, m, M):
        month = range(1,M+1)
        status = self.progression(payment, m, M)[1:]
        amount = []
        for i in status:
            amount.append(sum(i))
        return [month, amount]
        

   


    


    
