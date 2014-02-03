
# -*- coding: utf-8 -*-
import math
#import locale
#locale.setlocale( locale.LC_ALL, 'icelandic')

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
    #Fyrir: monthly>=0 rauntala, M>0 heiltala
    #Eftir: data heldur utan um stöðu sparnaðarreiknings frá upphafsstöðu og næstu M mánuði þar a eftir
    #       þar sem upphæð monthly hefur verið lögð inn hvern mánuð.
    def progression(self, monthly, M):

        total = self.a
        prog = [total]
        for i in range(0,M):
            total = (total+monthly)*(self.adjustedp)
            prog.append(int(math.floor(total)))

        return prog

    def printProgression(self, monthly, M):
        return null
    #á eftir að útfæra^
    
    #Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 rauntölur
    #Eftir: m er upphæð sem tekist hefur að safna á M mánuðum með monthly sparnaði á mánuði og má taka út strax.
    def saveforM(self, monthly, M):
   
        m = max(int(math.floor(M-self.b)),0) #spara með því að leggja fyrir reglulega í m mán
        n = int(math.floor(M-m)) #=int(math.ceil(self.b))
        prog1 = self.progression(monthly, m)
        
        total = prog1[m]
        temp = Savings('temp', total, self.p*100, self.dex, self.b)
        prog2 = temp.progression(0,n)
        total = prog2[n]
        
        return total

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
        

   


    


    
