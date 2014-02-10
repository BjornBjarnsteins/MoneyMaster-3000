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
        self.mrates = pow(1+self.p,1.0/12) - 1 #mánaðarlegir vextir reiknaðir út frá ársvöxtum

        if(index):
            self.adjustedp = pow((1+self.p)*(1+self.influx), 1.0/12)
        else:
            self.adjustedp = 1+self.mrates
    

    #Notkun: print s eða a = str(s)
    #Fyrir: Savings hlutur, Mánuður er 30 dagar
    #Eftir: a er strengur sem heldur utan um allar upplýsingar um s
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
            bound = '%d ar, %d manuðir, %d dagar' %(years, months, days)
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
    #Eftir: data heldur utan um stöðu sparnaðarreiknings frá upphafsstöðu og næstu M mánuði þar a eftir
    #       þar sem upphæð monthly hefur verið lögð inn hvern mánuð.
    def progression(self, monthly, m, M):

        total = self.a  
        prog = [total] #setjum inn upphafsstöðu reiknings í fyrsta sætið
        for i in range(0,m): #næstu m mánuðina leggjum við upphæð monthly inn a reikninginn.
            total = (total+monthly)*(self.adjustedp)
            prog.append(int(math.floor(total)))

        for i in range(m,M): #síðustu M-m mánuðina leggjum við ekkert inn á reikninginn og sjáum hvernig hann þróast aðeins a vöxtum.
            total = total*self.adjustedp
            prog.append(int(math.floor(total)))
            
        return prog

    def printProgression(self, monthly, m, M):
        prog = self.progression(monthly, m, M)
        s = ''
        print 'Upphafsstaða: %s' %(locale.currency(prog[0], grouping=True))
        for i in range(1,len(prog)):
            amount = locale.currency(prog[i], grouping = True)
            print 'Mánuður %d: %s' %(i, amount)

    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 rauntölur
    #Eftir: m er upphæð sem tekist hefur að safna á M mánuðum með monthly sparnaði á mánuði og má taka út strax.
    def saveforM(self, monthly, M):
        m = max(int(math.floor(M-self.b)),0) #spara með því að leggja fyrir reglulega í m mán
        prog = self.progression(monthly, m, M)
        return prog[M]


    #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 rauntölur
    #Eftir: m er fjöldi mánaða sem það tekur að safna upp X pening a reikning þ.a. það megi taka hann út strax.
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