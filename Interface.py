# -*- coding: cp1252 -*-
#Markús 02.02.14
#Þessi skrá á að hegða sér eins og einfalt command line interface
import Loan;
import storage;
import Savings;

val = "y"
lanalisti = [];
while (val=="y"):
    print "Sláðu inn lán";
    Name = raw_input('Sláðu inn nafn á láni sem þú hefur tekið: ');
    Amount = raw_input('Sláðu inn höfuðstól: ');
    Interest = raw_input('Sláðu inn vexti í prósentum: ');
    Months = raw_input('Sláðu inn fjölda mánaða: ');
    Index = raw_input('Sláðu inn hvort lánið sé verðtryggt (y/n): ');
    #Breyti Index í Boolean gildi
    if (Index == "y"):
        Index = True;
    elif (Index == "n"):
        Index = False;
    else:
        print 'Ólöglegt gildi';
        break

    #Bý til lán hlut og bæti honum við lánalistann
    lan = Loan.Loan(Name,int(Amount),int(Interest),int(Months),Index);
    lanalisti.append(lan);

    #Vista lánið í skránna loans.txt:
    #storage.storeLoan(lan);
                    
    val = raw_input("Vilt þú slá inn annað lán? (y/n): ");


    #Name = raw_input('Sláðu inn nafn á reikningi: ');
    #Amount = raw_input('Sláðu inn sparifé: ');
    #Interest = raw_input('Sláðu inn vexti: ');
    #Months = raw_input('Sláðu inn fjölda mánaða: ');
    #Index = raw_input('Sláðu inn hvort lánið sé verðtryggt (y/n): ');

#Hér ætla ég að vista öll lánin úr listanum lánalisti
storage.storeAllLoans(lanalisti);

Sparife = raw_input("Sláðu inn sparifé: ");                     #(upphæðina sem á að setja inn á heppilega sparnaðarleið)
Man_sparn = raw_input("Sláðu inn mánaðarlegan sparnað: ");
Vidm_timi = raw_input("Sláðu inn viðmiðunartíma í mánuðum: ");            #hann er þá notaður til að finna bestu sparnaðarleiðina
Sparnadarmarkmid = raw_input("Sláðu inn sparnaðarmarkmið (-1 ef á ekki við): ");
Sparnadartimi = raw_input("Sláðu inn sparnaðartíma: (-1 ef á ekki við): ");
Fj_man = raw_input("Sláðu inn fjölda mánaða sem þú vilt fá ráðleggingar um (-1 ef á ekki við): ");
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
accts = loadSAccts()



    #name, amount, interest, index, bound
    #spar = Savings.Savings(s[0],float(s[1]),float(s[2]),int(s[3]),float(s[4]));

    #Vista sparnaðinn:
    #storage.storeSAcct(spar);
    #Þetta virkar ekki, held að ástæðan sé að fyrir og eftirskilyrði í storage og Savings eru ekki í samræmi

#Nota load all savings til að ná í uppl um alla reikninga - laga
#Lagfæra innsláttartexta í samræmi við skrá - búið
#Búa til lista yfir lán og vista alla í einu. Til að það sé ekki neitt annað í skránni og það nýja eyðist ekki óvart - búið

#Debugga
#Calculator klasinn. Láta hann vinna með tölurnar sem koma a eftir lánum
#Í klasanum er reiknivél til að finna hvað ég er lengi að safan X miklu


#Bæta við möguleikanum á að geta skilgreint reikninga og láta vélina segja til um hvaða reikningur er bestur











