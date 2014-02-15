#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Loan
import Savings
import storage


#Notkun: t = compareLS(l,s,monthly,M)
#Fyrir: l er Loan hlutur, s er Savings hlutur, monthly>=0 rauntala, M>=0 heiltala
#Eftir: t = l ef hagstæðara er fyrir notanda að greiða upphæð monthly inn á l í M mánuði, t = s annars
#       'hagstæðara' telst vera meiri eignir að M mánuðum loknum.

a = storage.loadLoans()
dictLoans = {}
for i in a:
    dictLoans[str(i.name)]=str(i)

import gettext
class TabPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja lan"), ""], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY,pos=(28,70),size=(230, 25))
        self.SetFont(wx.Font(10,family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        populateComboBox(self)

        self.combo_box_2.SetSelection(0)
        
        title1 = wx.StaticText(self,-1,'Lánareiknivél',pos=(28,10))
        title1.SetFont(wx.Font(24, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60)) 
        self.combo_box_2.Bind(wx.EVT_TEXT,self.values)
        plot_icon = wx.Image('graf.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        plot = wx.StaticBitmap(self,-1,plot_icon,pos=(325,230))

        self.Fit()

        self.SetSizer(sizer)


    def values(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,str(dictLoans[self.combo_box_2.GetValue()]),pos=(15,10))
        someInfo.SetFont(wx.Font(14, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        someInfo.SetForegroundColour("blue")
        
    def cleanPanel(self,window):
            for child in window.GetChildren():
                if type(child) != wx._controls.StaticBitmap:
                    child.Destroy()
        
def populateComboBox(self):
    a = storage.loadLoans()
    k = 1
    for i in a:
        self.combo_box_2.Insert(i.name,k)
        k += 1
             

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Reiknivél lán")
       
        panel = TabPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

