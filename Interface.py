# -*- coding: utf-8 -*-
#Markús 02.02.14
#Þessi skrá á að hegða sér eins og einfalt command line interface
import Loan;
import storage;
#import Savings;
from Savings import *;
import Calculator;
locale.setlocale( locale.LC_ALL, 'is_IS.UTF-8')

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
    
val = "y"
lanalisti = [];
while (val=="y"):
    print "Sláðu inn lán";

    #Kóði sem biður notanda um nauðsynlegar breytur til að vinna með lán og athugar hvort þær séu löglegar
    Name = raw_input('Sláðu inn nafn láns: ');
    while (not Name):   #not Name er True þþaa Name sé tómi strengurinn
        Name = raw_input('Nafn má ekki vera tómt: ');
    
    Amount = raw_input('Sláðu inn höfuðstól: ');
    while (not isint(Amount)):
        Amount = raw_input('Höfuðstóll þarf að vera heiltala: ');
    Amount = int(Amount);
        
    Interest = raw_input('Sláðu inn vexti í prósentum: ');
    while(not isfloat(Interest)):
        Interest = raw_input('Vextir þurfa að vera gefnir í prósentum, t.d. 4.5 eða 4: ');
    Interest = float(Interest);
     
    #!!!Ath: Notkunarskilyrðin hjá Leó segja að Interest eigi að vera heiltala sem er ekki rétt!!! Þurfum að ráða við t.d. 4.5% vexti væntanlega
    
    Months = raw_input('Sláðu inn fjölda mánaða: ');
    while (not isint(Months)):
        Months = raw_input('Fjöldi mánaða þarf að vera gefinn sem heiltala: ');
    Months = int(Months);

    Index = raw_input('Sláðu inn hvort lánið sé verðtryggt (y/n): ');
    while (not (Index=='y' or Index=='n')):
        Index = raw_input('Sláðu inn hvort lánið sé verðtryggt (y/n): ');
    if (Index == "y"):
        Index = True;
    elif (Index == "n"):
        Index = False;
    #else:
    #    print 'Ólöglegt gildi';
    #    break

    #Bý til lán hlut og bæti honum við lánalistann
    #Ath að þetta er aðeins framkvæmt ef öll gildin frá notanda voru lögleg
    lan = Loan.Loan(Name,int(Amount),float(Interest),int(Months),Index);
    lanalisti.append(lan);
                    
    val = raw_input("Vilt þú slá inn annað lán? (y/n): ");

#Vista öll lánin úr listanum lánalisti í skránna loans.txt
#Ath þetta eyðir öllu sem var fyrir í skránni
#Þarf að geta nálgast fyrirframskilgreindu lánin. Breyta storage.py og hafa 2 lánaskrár?
storage.storeAllLoans(lanalisti);

Sparife = raw_input("Sláðu inn sparifé: ");                                         #(upphæðin sem á að setja inn á heppilega sparnaðarleið)
while (not isint(Sparife)):
    Sparife = raw_input('Sparifé þarf að vera heiltala: ');
Sparife = int(Sparife);
    
Man_sparn = raw_input("Sláðu inn mánaðarlegan sparnað: ");
while (not isint(Man_sparn)):
    Man_sparn = raw_input('Mánaðarlegur sparnaður þarf að vera heiltala: ');
Man_sparn = int(Man_sparn);
    
Vidm_timi = raw_input("Sláðu inn viðmiðunartíma í mánuðum: ");                      #Geri ráð fyrir að þetta sé hve lengi notandi hyggst geyma upphæð inn á reikningi
while (not isint(Vidm_timi)):
    Vidm_timi = raw_input('Viðmiðunartími þarf að vera heiltala: ');
Vidm_timi = int(Vidm_timi);
    
Sparnadarmarkmid = raw_input("Sláðu inn sparnaðarmarkmið (-1 ef á ekki við): ");    #Þarf að bæta við að geta tekið við -1
while (not isint(Sparnadarmarkmid)):
    Sparnadarmarkmid = raw_input('Sparnaðarmarkmið þarf að vera heiltala: ');
Sparnadarmarkmid = int(Sparnadarmarkmid);

Sparnadartimi = raw_input("Sláðu inn sparnaðartíma í mánuðum: (-1 ef á ekki við): ");         #Geri ráð fyrir að þetta sé hve lengi notandi ætlar að leggja fyrir mánaðarlega
while (not isint(Sparnadartimi)):
    Sparnadartimi = raw_input('Sparnaðartími þarf að vera heiltala: ');
Sparnadartimi = int(Sparnadartimi);

Fj_man = raw_input("Sláðu inn fjölda mánaða sem þú vilt fá ráðleggingar um (-1 ef á ekki við): ");
while (not isint(Fj_man)):
    Fj_man = raw_input('fjöldi mánaða þarf að vera heiltala: ');
Fj_man = int(Fj_man);


#Sæki upplýsingar um öll lán úr skránni loans.txt
loans = storage.loadLoans();

#Vel hagkvæmasta lánið - í vinnslu
#L = Calculator.compareAllLoans(loans, Man_sparn, Sparnadartimi);
#print L;

                                                           
#Sæki upplýsingar um alla reikninga
#accts = storage.loadSAccts()
#Virkar ekki því það vantar skránna eins og er


#Finn hvaða reikningur er hagkvæmastur fyrir notanda:
#Nota bull reikning tímabundið
Reikningur = Savings('Jonas', 1000, 5.5, 0, 0);
#Vista þann reikning sem Savings hlutinn Reikningur


#Finn hvað notandi er lengi að safna fyrir Sparnadarmarkmid m.v. Man_sparn lagt til hliðar á mánuði
if ((not Sparnadarmarkmid == -1) and (not Man_sparn == -1)):
    m = Reikningur.saveuptoX(Man_sparn,Sparnadarmarkmid);    
    print 'Það tekur þig ', m, ' mánuði að safna ', locale.currency(Sparnadarmarkmid, grouping = True), ' með því að leggja fyrir ', locale.currency(Man_sparn, grouping = True), ' á mánuði' ;

#Birti hvað notandi nær að safna miklu á Sparnadartimi mánuðum m.v. Man_sparn lagt til hliðar á mánuði
if ((not Sparnadartimi == -1) and (not Man_sparn == -1)):
    M = Reikningur.saveforM(Man_sparn, Sparnadartimi);
    #Ath: Notkunarskilyrði fallsins eru röng. Biður um Rauntölu en verður að vera heiltala fyrir seinni breytu.  
    print 'Þú nærð að safna ', locale.currency(M, grouping = True), ' með því að leggja fyrir ', locale.currency(Man_sparn, grouping = True), ' á mánuði í ', Sparnadartimi, ' mánuði';


    #Vista sparnaðinn:
    #storage.storeSAcct(spar);
    #Þetta virkar ekki, held að ástæðan sé að fyrir og eftirskilyrði í storage og Savings eru ekki í samræmi


#Næstu verkefni:
    
#Nota load all savings til að ná í uppl um alla reikninga - laga
#Calculator klasinn. Láta hann velja hagstæðasta lán
#Í klasanum er reiknivél til að finna hvað ég er lengi að safan X miklu

#Seinna:
#Bæta við möguleikanum á að geta skilgreint reikninga og láta vélina segja til um hvaða reikningur er bestur
