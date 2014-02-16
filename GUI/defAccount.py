#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Loan
import Savings
import storage

import gettext
class TabPanel(wx.Panel):
    def __init__(self, parent):
        """"""
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        sizer = wx.BoxSizer(wx.VERTICAL)

        right = -70
        down = -130
        label1 = wx.StaticText(self, -1, 'Nafn reiknings',pos=(100+right,202+down))
        self.inputTxt1 = wx.TextCtrl(self, -1, '',pos=(240+right,200+down),size=(140,-1))
  
        label2 = wx.StaticText(self, -1, 'Upphafleg innistæða',pos=(100+right,232+down))
        self.inputTxt2 = wx.TextCtrl(self, -1, '',pos=(240+right,230+down),size=(140,-1))
        
        label3 = wx.StaticText(self, -1, 'Ársvextir',pos=(100+right,260+down))
        self.inputTxt3 = wx.TextCtrl(self, -1, '',pos=(240+right,262+down),size=(140,-1))
        
        label4 = wx.StaticText(self, -1, 'Verðtrygging',pos=(100+right,294+down))
        
        self.input41 = wx.RadioButton(self, -1, 'Já',pos=(244+right,295+down),style=wx.RB_GROUP)
        self.input42 = wx.RadioButton(self, -1, 'Nei',pos=(290+right,295+down))

        label5 = wx.StaticText(self, -1, 'Binditími',pos=(100+right,327+down))
        self.inputTxt5 = wx.TextCtrl(self, -1, '',pos=(240+right,323+down),size=(140,-1))
       
        self.btnSparnadur = wx.Button(self,label="Vista reikning",pos=(240+right,355+down),size=(111,-1))
        self.color=self.GetBackgroundColour()

        self.Bind(wx.EVT_PAINT, self.on_paint)
        # set frame size to fit panel
        self.Fit()
        title1 = wx.StaticText(self,-1,'Skilgreina reikning',pos=(28,10))
        title1.SetFont(wx.Font(24, family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans Narrow",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self,-1,piggy,pos=(355,60))
        self.SetSizer(sizer)
        
        self.btnSparnadur.Bind(wx.EVT_BUTTON, self.saveAccount)
    
    def saveAccount(self,event):
        input1 = self.inputTxt1.GetValue()
        input2 = self.inputTxt2.GetValue()
        input3 = self.inputTxt3.GetValue()
        if self.input41.GetValue():
            input4 = True
        else:
            input4 = False
        input5 = self.inputTxt5.GetValue()
        spar = Savings.Savings(input1,float(input2),float(input3)*100,input4,float(input5)) 
        storage.storeSAcct(spar)
        

        
    def on_paint(self, event):
        # establish the painting canvas
        dc = wx.PaintDC(self)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y, w/3, h), 'white', self.color)
                 
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Define account")
       
        panel = TabPanel(self)
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

