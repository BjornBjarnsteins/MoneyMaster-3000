#! /usr/bin/env python
# -*- coding: cp1252 -*-
import wx
import Loan
import Savings
import storage

import gettext
a = storage.loadSAccts()
dictLoans = {}
for i in a:
    dictLoans[str(i.n)]=str(i)
    
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
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja reikning"), ""], 
                                       style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | 
                                       wx.CB_READONLY,pos=(28,70),size=(230, 25))
        populateComboBox(self)
        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        
        self.combo_box_1.SetSelection(0)
        
        up = -13
        self.txt2 = wx.StaticText(self,-1,'Sparna�armarkmi�',pos=(28,125+up))
        self.inputTxt1 = wx.TextCtrl(self, -1, '',pos=(28,145+up))

        self.txt3 = wx.StaticText(self,-1,'Sparna�ur � m�nu�i',pos=(28,186+up))
        self.inputTxt2 = wx.TextCtrl(self, -1, '' ,pos=(28,212+up))
        
        self.btn = wx.Button(self,label="Reikna sparna�armarkmi�",pos=(28,280+up-25),size=(-1,-1))
        
        self.combo_box_1.Bind(wx.EVT_TEXT,self.values)
        
        self.btn.Bind(wx.EVT_BUTTON, self.calculate)
        plot_icon = wx.Image('graf.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        plot = wx.StaticBitmap(self,-1,plot_icon,pos=(325,230))
        
        self.Fit()
        
        self.SetSizer(sizer)
        #Notkun: m = saveuptoX(monthly,X)
    #Fyrir: monthly,X>=0 raunt�lur
    #Eftir: m er fj�ldi m�na�a sem �a� tekur a� safna upp X pening a reikning �.a. �a� megi taka hann �t strax.
    def calculate(self,event):
        name = self.combo_box_1.GetValue()
        savings = storage.loadSAccts()
        monthly = self.inputTxt2.GetValue()
        X = self.inputTxt1.GetValue()
        #Eftir: m er fj�ldi m�na�a sem �a� tekur a� safna upp X pening a reikning �.a. �a� megi taka hann �t strax.
        text = ""
        for i in savings:
            if i.n == name:
                acct = i
                val = acct.saveuptoX(float(monthly),float(X))
                text = str(val)+ " er fjoldi manada sem tekur ad safna upp "+X+" pening \na reikning th.a. thad megi taka hann ut strax."
        if text != "":
            someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,text,pos=(15,10),size=(800,200))
            someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
            someInfo.SetForegroundColour("red")
    
    def values(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoans[self.combo_box_1.GetValue()],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("red")
   
        
def populateComboBox(self):
    a = storage.loadSAccts()
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

