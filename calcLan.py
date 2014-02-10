# -*- coding: cp1252 -*-
import wx
import Loan
import Savings
import storage

# Eftir:  L er lán sem heitir Name, með höfuðstól Amount, Interest ársvexti, Months tíma eftir og Index segir til um verðtryggingu.

a = storage.loadLoans()
dictLoans = {}
for i in a:
    dictLoans[str(i.name)]=str(i)

import gettext
class TabPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        sizer = wx.BoxSizer(wx.VERTICAL)
        font2 = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.BOLD)

        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=[_("Velja lan"), ""], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY,pos=(28,70),size=(230, 25))
        self.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        populateComboBox(self)

        self.combo_box_2.SetSelection(0)
        
        title1 = wx.StaticText(self,-1,'Lánareiknivél',pos=(28,10))
        title1.SetFont(wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans Narrow"))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(345,60)) 
        self.combo_box_2.Bind(wx.EVT_COMBOBOX, self.reikna)
        self.combo_box_2.Bind(wx.EVT_TEXT,self.values)

        self.Fit()

        self.SetSizer(sizer)

    
    def reikna(self,event):
        print "ups"
    def values(self,event):
        someInfo = wx.StaticText(self.GetParent().GetParent().GetParent().bottomwindow,
                                 -1,str(dictLoans[self.combo_box_2.GetValue()]),pos=(15,10),size=(800,200))
        someInfo.SetFont(wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
        someInfo.SetForegroundColour("blue")
        self.GetParent().GetParent().GetParent().bottomwindow.SetScrollRate(10,10)
        self.GetParent().GetParent().GetParent().bottomwindow.SetVirtualSize(someInfo.GetVirtualSize())
        
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

