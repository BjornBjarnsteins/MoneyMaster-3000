#! /usr/bin/env python
# -*- coding: utf-8 -*-
#ATTENTION! YOU NEED TO DOWNLOAD THE BEAUTIFULSOUP LIBRARY BEFORE RUNNING THIS CODE

import wx
import Loan
import Savings
import storage
import Calculator
import gettext
import plot
from bs4 import BeautifulSoup
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')

a = storage.loadSAccts()
dictLoansS = {}
for i in a:
    dictLoansS[BeautifulSoup(i.n)]=str(i)


b = storage.loadLoans()
dictLoansL = {}
for i in b:
    dictLoansL[BeautifulSoup(i.name)]=str(i)


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

        self.txt3 = wx.StaticText(self,-1,'Fjöldi mánuða',pos=(28,200+up))
        self.inputTxt2 = wx.TextCtrl(self, -1, '' ,pos=(28,220+up))


        self.txt4 = wx.StaticText(self,-1,'Sparnaður á mánuði',pos=(28,255+up))
        self.inputTxt3 = wx.TextCtrl(self, -1, '' ,pos=(28,274+up))
        
        self.btn = wx.Button(self,label="Reikna!",pos=(28,330+up-16),size=(-1,-1))
        
        self.combo_box_1.Bind(wx.EVT_TEXT,self.valuesS)
        self.combo_box_2.Bind(wx.EVT_TEXT,self.valuesL)

        self.btn.Bind(wx.EVT_BUTTON, self.calculate)
        
        self.plotBtn = wx.BitmapButton(self,-wx.ID_ANY,wx.Image('graf.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),pos=(325,230),style=wx.NO_BORDER)
        self.plotBtn.Bind(wx.EVT_BUTTON,self.plot) 
        self.plotBtn.SetBitmapHover(wx.Image('grafhover.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        self.color=self.GetBackgroundColour()

        self.Bind(wx.EVT_PAINT, self.on_paint)        
        self.Fit()
        
        self.SetSizer(sizer)
		
    def plot(self,event):
        a = storage.loadSAccts()
        b = storage.loadLoans()

        nameS = BeautifulSoup(self.combo_box_1.GetValue())
        nameL = BeautifulSoup(self.combo_box_2.GetValue())
        monthly = self.inputTxt3.GetValue()
        M = self.inputTxt2.GetValue()
        for i in a:
            if BeautifulSoup(i.n) == nameS:
                for j in b:
                    if BeautifulSoup(j.name) == nameL:
                        plot.plotLS(j,i,int(monthly),int(M))

    def refreshList(self):
        a = storage.loadSAccts()
        dictLoansS = {}
        for i in a:
            dictLoansS[BeautifulSoup(i.n)]=str(i)
        b = storage.loadLoans()
        dictLoansL = {}
        for i in b:
            dictLoansL[BeautifulSoup(i.name)]=str(i)
        populateComboBoxLoans(self)
        populateComboBoxSavings(self)

    def on_paint(self, event):
        # establish the painting canvas
        dc = wx.PaintDC(self)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y+h*0.66-1, w, h/3), 'white', self.color,nDirection = wx.NORTH)
		
    def calculate(self,event):
        a = storage.loadSAccts()
        b = storage.loadLoans()
        nameS = BeautifulSoup(self.combo_box_1.GetValue())
        nameL = BeautifulSoup(self.combo_box_2.GetValue())
        text = ""
        monthly = self.inputTxt3.GetValue()
        M = self.inputTxt2.GetValue()
        for i in a:
            if BeautifulSoup(i.n) == nameS:
                for j in b:
                    if BeautifulSoup(j.name) == nameL:
                        val = Calculator.compareLS(j, i,float(monthly), int(M))
                        if isinstance(val, Savings.Savings):
                            text = BeautifulSoup(i.n)
                        else:
                            text = BeautifulSoup(j.name)
                            #text = "Hagstaedara er fyrir notanda ad greida upphaed \n" + monthly + " inn a "+ BeautifulSoup(j.name).encode('ascii') +" i" + M +" manudi,\n\'hagstaedara\' telst vera meiri eignir ad "+M + " manudum loknum"
        if text != "":
				first= unicode(BeautifulSoup("Hagstæðara er fyrir notanda að greiða upphæð "))
				M1 = unicode(BeautifulSoup(M))
				amount = locale.currency(int(monthly), grouping = True)
				monthly1 = unicode(BeautifulSoup(amount))
				second = unicode(BeautifulSoup("\ninn á "))
				third = unicode(BeautifulSoup(" í "))
				fourth = unicode(BeautifulSoup(" mánuði."))
				text = unicode(text)
				someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,-1,first+monthly1+second+text+third+M1+fourth,pos=(15,10),size=(800,200))
				someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
				someInfo.SetForegroundColour("blue")
    
    def valuesS(self,event):
        a = storage.loadSAccts()
        if dictLoansS.get(BeautifulSoup(a[-1].n))==None:
            dictLoansS[BeautifulSoup(a[-1].n)]=str(a[-1])
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoansS[BeautifulSoup(self.combo_box_1.GetValue())],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("black")
    
    def valuesL(self,event):
        b = storage.loadLoans()
        if dictLoansL.get(BeautifulSoup(b[-1].name))==None:
            dictLoansL[BeautifulSoup(b[-1].name)]=str(b[-1])
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoansL[BeautifulSoup(self.combo_box_2.GetValue())],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("black")
        
def populateComboBoxSavings(self):
    a = storage.loadSAccts()
    self.combo_box_1.Clear()
    self.combo_box_1.Insert("Velja reikning",0)
    self.combo_box_1.SetSelection(0)
    k = 1
    for i in a:
        self.combo_box_1.Insert(i.n,k)
        k += 1

def populateComboBoxLoans(self):
    b = storage.loadLoans()
    self.combo_box_2.Clear()
    self.combo_box_2.Insert("Velja lán",0)
    self.combo_box_2.SetSelection(0)
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

