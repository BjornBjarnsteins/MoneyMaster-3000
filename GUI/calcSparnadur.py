#! /usr/bin/env python
# -*- coding: utf-8 -*-
#ATTENTION! YOU NEED TO DOWNLOAD THE BEAUTIFULSOUP LIBRARY BEFORE RUNNING THIS CODE

import wx
import Loan
import Savings
import storage
from bs4 import BeautifulSoup
import gettext
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')
a = storage.loadSAccts()
dictS = {}
for i in a:
    dictS[BeautifulSoup(i.n)]=str(i)
    
class TabPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        sizer = wx.BoxSizer(wx.VERTICAL)
        title1 = wx.StaticText(self,-1,'Sparna�armarkmi�',pos=(28,10))
        title1.SetFont(wx.Font(24, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60))
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja reikning")], 
                                       style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | 
                                       wx.CB_READONLY,pos=(28,70),size=(230, 25))
        populateComboBox(self)
        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        
        self.combo_box_1.SetSelection(0)
        
        up = -10
        self.txt3 = wx.StaticText(self,-1,'Sparna�ur � m�nu�i',pos=(28,125+up))
        self.inputTxt2 = wx.TextCtrl(self, -1, '',pos=(28,150+up))

        self.txt2 = wx.StaticText(self,-1,'Sparna�armarkmi�',pos=(28,190+up))
        self.inputTxt1 = wx.TextCtrl(self, -1, '' ,pos=(28,210+up))
        
        self.btn = wx.Button(self,label="Reikna t�ma",pos=(28,260+up-4),size=(-1,-1))
        
        self.combo_box_1.Bind(wx.EVT_TEXT,self.values)
        
        self.btn.Bind(wx.EVT_BUTTON, self.calculate)
        self.color=self.GetBackgroundColour()

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Fit()
        
        self.SetSizer(sizer)

    def refreshList(self):
        a = storage.loadSAccts()
        dictSS = {}
        for i in a:
            dictSS[BeautifulSoup(i.n)]=str(i)
        populateComboBox(self)
    def calculate(self,event):
        for child in self.GetParent().GetParent().GetParent().bottomwindow.GetChildren():
            child.Destroy()
        name = self.combo_box_1.GetValue()
        savings = storage.loadSAccts()
        monthly = self.inputTxt2.GetValue()
        X = self.inputTxt1.GetValue()
        #Eftir: m er fj�ldi m�na�a sem �a� tekur a� safna upp X pening a reikning �.a. �a� megi taka hann �t strax.
        text = ""
        for i in savings:
            if unicode(BeautifulSoup(i.n)) == name:
                acct = i
                val = acct.saveuptoX(float(monthly),float(X))
                amount = locale.currency(int(X), grouping=True)
                text = unicode(BeautifulSoup("Eftir "))+str(val)+ unicode(BeautifulSoup(" m�nu�i ver�ur innist��a � reikningnum or�in meiri en \n"))+amount+unicode(BeautifulSoup(" og upph��ina m� taka �t strax �t strax."))
        if text != "":
            someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,text,pos=(15,10),size=(800,200))
            someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
            someInfo.SetForegroundColour("blue")
			
    def on_paint(self, event):
        # establish the painting canvas
        dc = wx.PaintDC(self)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y+h*0.66-1, w, h/3), 'white', self.color,nDirection = wx.NORTH)
		
    def values(self,event):
        a = storage.loadSAccts()
        if dictS.get(BeautifulSoup(a[-1].n))==None:
            dictS[BeautifulSoup(a[-1].n)]=str(a[-1])
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictS[BeautifulSoup(self.combo_box_1.GetValue())],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("black")
   
        
def populateComboBox(self):
    a = storage.loadSAccts()
    self.combo_box_1.Clear()
    self.combo_box_1.Insert("Velja reikning",0)
    self.combo_box_1.SetSelection(0)
    k = 1
    for i in a:
        self.combo_box_1.Insert(i.n,k)
        k += 1
            
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Reikniv�l sparnadur")
       
        panel = TabPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

