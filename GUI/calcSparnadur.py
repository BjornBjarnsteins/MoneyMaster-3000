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
        self.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        sizer = wx.BoxSizer(wx.VERTICAL)
        font2 = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        title1 = wx.StaticText(self,-1,'Sparnaðarreiknivél',pos=(28,10))
        title1.SetFont(wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans Narrow"))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60))
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja reikning"), ""], 
                                       style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | 
                                       wx.CB_READONLY,pos=(28,70),size=(230, 25))
        populateComboBox(self)
        self.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))

        self.combo_box_1.SetSelection(0)
        
        self.combo_box_1.Bind(wx.EVT_COMBOBOX, self.reikna)
        self.combo_box_1.Bind(wx.EVT_TEXT,self.values)
        self.Fit()

        self.SetSizer(sizer)

    
    def reikna(self,event):
        print "ups"
        
    def values(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,dictLoans[self.combo_box_1.GetValue()],pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("red")
        self.GetParent().GetParent().GetParent().bottomwindow.SetScrollRate(10,10)
        self.GetParent().GetParent().GetParent().bottomwindow.SetVirtualSize(someInfo.GetVirtualSize())      
        
def populateComboBox(self):
    a = storage.loadSAccts()
    k = 1
    for i in a:
        self.combo_box_1.Insert(i.n,k)
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

