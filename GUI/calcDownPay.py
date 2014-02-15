#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Loan
import Savings
import storage
import Calculator
import gettext

a = storage.loadSAccts()
dictLoansS = {}
for i in a:
    dictLoansS[str(i.n)]=str(i)


b = storage.loadLoans()
dictLoansL = {}
for i in b:
    dictLoansL[str(i.name)]=str(i)


class TabPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        sizer = wx.BoxSizer(wx.VERTICAL)

        title1 = wx.StaticText(self,-1,'Niðurgreiðslur lána',pos=(28,10))
        title1.SetFont(wx.Font(24, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60))
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja reikning")], 
                                       style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | 
                                       wx.CB_READONLY,pos=(28,70),size=(230, 25))
        populateComboBoxSavings(self)
        
        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja lán")],style= wx.CB_READONLY,pos=(28,105),size=(230, 125))
        self.combo_box_2.SetSelection(0)
        self.SetFont(wx.Font(10,family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        
        populateComboBoxLoans(self)
        
        self.combo_box_1.SetSelection(0)
        
        up = -57

#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstæðara er fyrir notanda að greiða upphæð monthly inn á l í M mánuði, t = s annars
#       'hagstæðara' telst vera meiri eignir að M mánuðum loknum.

        self.txt3 = wx.StaticText(self,-1,'Fjöldi mánuða',pos=(28,200+up))
        self.inputTxt2 = wx.TextCtrl(self, -1, '' ,pos=(28,220+up))


        self.txt4 = wx.StaticText(self,-1,'Peningaupphæð',pos=(28,255+up))
        self.inputTxt3 = wx.TextCtrl(self, -1, '' ,pos=(28,274+up))
        
        self.btn = wx.Button(self,label="Reikna!",pos=(28,330+up-16),size=(-1,-1))
        
        self.combo_box_1.Bind(wx.EVT_TEXT,self.valuesS)
        self.combo_box_2.Bind(wx.EVT_TEXT,self.valuesL)

        self.btn.Bind(wx.EVT_BUTTON, self.calculate)
        
        plot_icon = wx.Image('graf.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        plot = wx.StaticBitmap(self,-1,plot_icon,pos=(330,230))
        
        self.Fit()
        
        self.SetSizer(sizer)
    
    def calculate(self,event):
        nameS = self.combo_box_1.GetValue()
        nameL = self.combo_box_2.GetValue()
#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstæðara er fyrir notanda að greiða upphæð monthly inn á l í M mánuði, t = s annars
#       'hagstæðara' telst vera meiri eignir að M mánuðum loknum.
        text = ""
        monthly = self.inputTxt3.GetValue()
        M = self.inputTxt2.GetValue()
        for i in a:
            if i.n == nameS:
                for j in b:
                    if j.name == nameL:
                        val = Calculator.compareLS(j, i,float(monthly), int(M))
                        if isinstance(val, Savings.Savings):
                            text = "Hagstaedara er fyrir notanda ad greida upphaed \n" + monthly + " inn a "+ i.n+" i " + M +" manudi,\n\'hagstaedara\' telst vera meiri eignir ad "+M + " manudum loknum"
                        else:
                            text = "Hagstaedara er fyrir notanda ad greida upphaed \n" + monthly + " inn a "+ j.name +" i " + M +" manudi,\n\'hagstaedara\' telst vera meiri eignir ad "+M + " manudum loknum"                       
        if text != "":
            someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,-1,text,pos=(15,10),size=(800,200))
            someInfo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
            someInfo.SetForegroundColour("blue")
    
    def valuesS(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoansS[self.combo_box_1.GetValue()],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("red")
    
    def valuesL(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoansL[self.combo_box_2.GetValue()],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("red")
        
def populateComboBoxSavings(self):
    a = storage.loadSAccts()
    k = 1
    for i in a:
        self.combo_box_1.Insert(i.n,k)
        k += 1

def populateComboBoxLoans(self):
    b = storage.loadLoans()
    k = 1
    for i in b:
        self.combo_box_2.Insert(i.name,k)
        k += 1
        
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Reiknivél sparnadur")
       
        panel = TabPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

