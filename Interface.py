# -*- coding: cp1252 -*-
#Markús 02.02.14
#Þessi skrá á að hegða sér eins og einfalt command line interface
import Loan;
import storage;
import Savings;
import Calculator;

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
    Name = raw_input('Sláðu inn nafn á láni sem þú hefur tekið: ');
    while (not Name):   #not Name er True þþaa Name sé tómi strengurinn
        Name = raw_input('Nafn má ekki vera tómt: ');
    
    Amount = raw_input('Sláðu inn höfuðstól: ');
    while (not isint(Amount)):
        Amount = raw_input('Höfuðstóll þarf að vera heiltala: ');
        
    Interest = raw_input('Sláðu inn vexti í prósentum: ');
    while(not isfloat(Interest)):
        Interest = raw_input('Vextir þurfa að vera gefnir í prósentum, t.d. 4.5 eða 4: ');
        
    #!!!Ath: Notkunarskilyrðin hjá Leó segja að Interest eigi að vera heiltala sem er ekki rétt!!! Þurfum að ráða við t.d. 4.5% vexti væntanlega
    
    Months = raw_input('Sláðu inn fjölda mánaða: ');
    while (not isint(Months)):
        Months = raw_input('Fjöldi mánaða þarf að vera gefinn sem heiltala: ');
        
    Index = raw_input('Sláðu inn hvort lánið sé verðtryggt (y/n): ');
    if (Index == "y"):
        Index = True;
    elif (Index == "n"):
        Index = False;
    else:
        print 'Ólöglegt gildi';
        break

    #Bý til lán hlut og bæti honum við lánalistann
    #Ath að þetta er aðeins framkvæmt ef öll gildin frá notanda voru lögleg
    lan = Loan.Loan(Name,int(Amount),float(Interest),int(Months),Index);
    lanalisti.append(lan);
                    
    val = raw_input("Vilt þú slá inn annað lán? (y/n): ");

#Vista öll lánin úr listanum lánalisti
storage.storeAllLoans(lanalisti);

Sparife = raw_input("Sláðu inn sparifé: ");                                         #(upphæðin sem á að setja inn á heppilega sparnaðarleið)
while (not isint(Sparife)):
    Sparife = raw_input('Sparifé þarf að vera heiltala: ');
    
Man_sparn = raw_input("Sláðu inn mánaðarlegan sparnað: ");
while (not isint(Man_sparn)):
    Man_sparn = raw_input('Mánaðarlegur sparnaður þarf að vera heiltala: ');
    
Vidm_timi = raw_input("Sláðu inn viðmiðunartíma í mánuðum: ");                      #Notaður til að finna bestu sparnaðarleiðina
while (not isint(Vidm_timi)):
    Vidm_timi = raw_input('Viðmiðunartími þarf að vera heiltala: ');
    
Sparnadarmarkmid = raw_input("Sláðu inn sparnaðarmarkmið (-1 ef á ekki við): ");    #Þarf að bæta við að geta tekið við -1
while (not isint(Sparnadarmarkmid)):
    Sparnadarmarkmid = raw_input('Sparnaðarmarkmið þarf að vera heiltala: ');

Sparnadartimi = raw_input("Sláðu inn sparnaðartíma: (-1 ef á ekki við): ");
while (not isint(Sparnadartimi)):
    Sparnadartimi = raw_input('Sparnaðartími þarf að vera heiltala: ');

Fj_man = raw_input("Sláðu inn fjölda mánaða sem þú vilt fá ráðleggingar um (-1 ef á ekki við): ");
while (not isint(Fj_man)):
    Fj_man = raw_input('fjöldi mánaða þarf að vera heiltala: ');

                                                                #Sláðu inn fjölda mánaða er notað til að vita hvort maður eigi að borga inn á lán/sparnað
                                                                #svo myndi forritið skila niðurstöðum úr þeim innsláttum þar sem notandi sló ekki inn -1
                                                                #eins og ef hann hefði aldrei slegið inn -1 kæmi:
                                                                #"Besta sparnaðarleiðin fyrir þig er: "
                                                                #"Það tekur þig X mánuði að safna þessari upphæð"
                                                                #"Á þessum tíma nærðu að safna: "
                                                                #"Á næstu X mánuðum er best fyrir þig að borga niður lán Y/leggja inn á sparnað Z"
                                                                #og hugmyndin er að skila líklegast þessu interfacei núna á miðvikudaginn frekar heldur en
                                                                #graphical interface-inu, það má koma síðar

#Sæki upplýsingar um alla reikninga
#accts = storage.loadSAccts()
#Virkar ekki því það vantar skránna

#m = Savings.saveuptoX(float(Man_sparn),float(Sparnadarmarkmid));
#print 'Það tekur þig %i mánuði að safna %i kr',m,Sparnadarmarkmid;
#Fatta ekki af hverju þetta virkar ekki



#Notkun: m = saveforM(monthly, M)
    #Fyrir: monthly,M>=0 rauntölur
    #Eftir: m er upphæð sem tekist hefur að safna á M mánuðum með monthly sparnaði á mánuði og má taka út strax.
    #def saveforM(self, monthly, M):

#Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 rauntölur
    #Eftir: m er fjöldi mánaða sem það tekur að safna upp X pening a reikning þ.a. það megi taka hann út strax.
    #def saveuptoX(self, monthly, X):







    #name, amount, interest, index, bound
    #spar = Savings.Savings(s[0],float(s[1]),float(s[2]),int(s[3]),float(s[4]));

    #Vista sparnaðinn:
    #storage.storeSAcct(spar);
    #Þetta virkar ekki, held að ástæðan sé að fyrir og eftirskilyrði í storage og Savings eru ekki í samræmi



#Nota load all savings til að ná í uppl um alla reikninga - laga

#Calculator klasinn. Láta hann vinna með tölurnar sem koma a eftir lánum
#Í klasanum er reiknivél til að finna hvað ég er lengi að safan X miklu

#Seinna:
#Bæta við möguleikanum á að geta skilgreint reikninga og láta vélina segja til um hvaða reikningur er bestur











