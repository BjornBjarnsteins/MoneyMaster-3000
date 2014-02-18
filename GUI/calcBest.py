#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Calculator
import Loan
import Savings
import storage
from bs4 import BeautifulSoup
#ATTENTION! YOU NEED TO DOWNLOAD THE BEAUTIFULSOUP LIBRARY BEFORE RUNNING THIS CODE
import gettext

class TabPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        sizer = wx.BoxSizer(wx.VERTICAL)

        title1 = wx.StaticText(self,-1,'Besta sparnaðarleiðin',pos=(28,10))
        title1.SetFont(wx.Font(24, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60))

        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))

        up = -62
        self.txt2 = wx.StaticText(self,-1,'Sparnaður á mánuði',pos=(28,125+up))
        self.inputTxt1 = wx.TextCtrl(self, -1, '',pos=(28,150+up))

        self.txt3 = wx.StaticText(self,-1,'Sparnaðartímabil',pos=(28,183+up))
        self.inputTxt2 = wx.TextCtrl(self, -1, '' ,pos=(28,203+up))
        self.txt4 = wx.StaticText(self,-1,'Viðmiðunartími',pos=(28,242+up-4))
        self.inputTxt3 = wx.TextCtrl(self, -1, '' ,pos=(28,263+up-4))

        self.btn = wx.Button(self,label="Reikna!",pos=(28,300+up-4),size=(-1,-1))
        
        self.color=self.GetBackgroundColour()

        self.Bind(wx.EVT_PAINT, self.on_paint)
        
        self.btn.Bind(wx.EVT_BUTTON, self.calculate)
        self.Fit()
        
        self.SetSizer(sizer)

    def calculate(self,event):
        savings = storage.loadSAccts()
        text = "Hagstæðasti sparnaðarreikningur af öllum reikningum:\n"
        monthly = self.inputTxt1.GetValue()
        m = self.inputTxt2.GetValue()
        M = self.inputTxt3.GetValue()
        S = Calculator.compareAllSavings(savings,float(monthly),int(m),int(M))
        someInfo1 = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,text,pos=(15,10),size=(800,20))
        someInfo2 = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,str(S),pos=(15,29),size=(800,200))
        someInfo1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD))
        someInfo2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL))
        someInfo1.SetForegroundColour("black")
        someInfo2.SetForegroundColour("blue")

    
    def on_paint(self, event):
        # establish the painting canvas
        dc = wx.PaintDC(self)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y+h*0.66-1, w, h/3), 'white', self.color,nDirection = wx.NORTH)

            
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Reiknivel sparnadur")
       
        panel = TabPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

