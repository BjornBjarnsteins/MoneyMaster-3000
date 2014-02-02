# -*- coding: cp1252 -*-
#Markús 02.02.14
#Þessi skrá á að hegða sér eins og einfalt command line interface
import Loan;
import storage;
import Savings;

print "Þú getur valið um að:";
print "1, Slá inn lán";
print "2, Slá inn sparnað";
#print "3, Slá inn ráðstöfunarfé";

val = raw_input('Veldu möguleika (1/2/3): ')
print (val)

while (val=="1"):
    print "Þú hefur valið að slá inn lán";
    s = raw_input("Sláðu inn lán: (Name,Amount,Interest,Months,Index): ").split(',');

    lan = Loan.Loan(s[0],int(s[1]),int(s[2]),int(s[3]),int(s[4]));

    #Vista nú lánið:
    storage.storeLoan(lan);    
                    
    val = raw_input("Viltu slá inn annað lán? (1/0): ");

if (val=="2"):
    print "Þú hefur valið að skrá inn uppsafnaðan sparnað";
    s = raw_input("Sláðu inn uppsafnaðan sparnað: (name, amount, interest, index, bound): ").split(',');

    spar = Savings.Savings(s[0],float(s[1]),float(s[2]),int(s[3]),float(s[4]));

    #Vista sparnaðinn:
    #storage.storeSAcct(spar);
    #Þetta virkar ekki, held að ástæðan sé að fyrir og eftirskilyrði í storage og Savings eru ekki í samræmi

    man_sp = raw_input("Sláðu inn mánaðarlegan sparnað: ");
    vidm_timi = raw_input("Sláðu inn viðmiðunartíma");
    sp_markm = raw_input("Sláðu inn sparnaðarmarkmið: (-1 ef á ekki við)");
    sp_timi = raw_input("Sláðu inn sparnaðartíma: (-1 ef á ekki við)" );
    fj_man = raw_input("Sláðu inn fjölda mánaða: (-1 ef á ekki við)");


#elif (val=="3"):
#    print "Þú hefur valið að slá inn ráðstöfunarfé";

elif (val=="0"):
    print "Þú hefur valið að hætta";
