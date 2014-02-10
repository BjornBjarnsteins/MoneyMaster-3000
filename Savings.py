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
        self.mrates = pow(1+self.p,1.0/12) - 1 #m�na�arlegir vextir reikna�ir �t fr� �rsv�xtum

        if(index):
            self.adjustedp = pow((1+self.p)*(1+self.influx), 1.0/12)
        else:
            self.adjustedp = 1+self.mrates
    

    #Notkun: print s e�a a = str(s)
    #Fyrir: Savings hlutur, M�nu�ur er 30 dagar
    #Eftir: a er strengur sem heldur utan um allar uppl�singar um s
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
            bound = '%d ar, %d manu�ir, %d dagar' %(years, months, days)
        elif(math.floor(self.b) != 0):
            months = int(math.floor(self.b))
            days = int((self.b-months)*30)
            bound = '%d manudir, %d dagar' %(months, days)
        else: 
            days = int(self.b*30)
            bound = str(days)+' dagar'
        
        amount = locale.currency(self.a, grouping = True)
        
        return 'Sparnadarreikningur: %s \nStada: %s \nArsvextir: %0.2f%s \nVerdtrygging: %s \nBinditimi: %s' %(self.n, amount, interest,'%', indexed, bound)

    #Notkun: data = progression(monthly,M)
    #Fyrir: monthly>=0 rauntala, M>0 heiltala
    #Eftir: data heldur utan um st��u sparna�arreiknings fr� upphafsst��u og n�stu M m�nu�i �ar a eftir
    #       �ar sem upph�� monthly hefur veri� l�g� inn hvern m�nu�.
    def progression(self, monthly, m, M):

        total = self.a  
        prog = [total] #setjum inn upphafsst��u reiknings � fyrsta s�ti�
        for i in range(0,m): #n�stu m m�nu�ina leggjum vi� upph�� monthly inn a reikninginn.
            total = (total+monthly)*(self.adjustedp)
            prog.append(int(math.floor(total)))

        for i in range(m,M): #s��ustu M-m m�nu�ina leggjum vi� ekkert inn � reikninginn og sj�um hvernig hann �r�ast a�eins a v�xtum.
            total = total*self.adjustedp
            prog.append(int(math.floor(total)))
            
        return prog

    def printProgression(self, monthly, m, M):
        prog = self.progression(monthly, m, M)
        s = ''
        print 'Upphafssta�a: %s' %(locale.currency(prog[0], grouping=True))
        for i in range(1,len(prog)):
            amount = locale.currency(prog[i], grouping = True)
            print 'M�nu�ur %d: %s' %(i, amount)

    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 raunt�lur
    #Eftir: m er upph�� sem tekist hefur a� safna � M m�nu�um me� monthly sparna�i � m�nu�i og m� taka �t strax.
    def saveforM(self, monthly, M):
        m = max(int(math.floor(M-self.b)),0) #spara me� �v� a� leggja fyrir reglulega � m m�n
        prog = self.progression(monthly, m, M)
        return prog[M]


    #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 raunt�lur
    #Eftir: m er fj�ldi m�na�a sem �a� tekur a� safna upp X pening a reikning �.a. �a� megi taka hann �t strax.
    def saveuptoX(self, monthly, X):

        total = self.a
        n = int(math.ceil(self.b))
        Y = X/math.pow(self.adjustedp,n)

        m = 0
        while(total < Y):
            total = (total+monthly)*(self.adjustedp)
            print total
            m = m+1
            print m

        return m+n
        
if __name__ == '__main__':
    a = Savings("sigga",5,1.2,True,2)

    print a.b