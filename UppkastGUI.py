# -*- coding: cp1252 -*-
import wx
import wx.lib.platebtn as platebtn
import Loan
import storage
import Savings
#Ath, �a� �arf a� downloada wxPython til a� geta keyrt forriti�,
#fari� � wxpython.org til a� dla
#Ekkert komment � �essum sullk��a :/
# �etta er enn�� uppkast og fullt sem vantar, t.d. input fyrir l�n ofl.
class MainFrame(wx.Frame):

    def __init__(self,parent,id,title,position,size):
        coin = wx.Icon('coins.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.__init__(self, parent, id, title, position, size)
        wx.Frame.SetIcon(self,coin)
        self.split1 = wx.SplitterWindow(self)
        self.split2 = wx.SplitterWindow(self.split1)
        self.bottompanel = wx.Panel (self.split1)
        self.bottompanel.SetBackgroundColour('white')
        self.topleftpanel = wx.Panel (self.split2)
        self.topleftpanel.SetBackgroundColour('white')
        self.toprightpanel = wx.Panel(self.split2)
        

        self.split1.SplitHorizontally(self.split2, self.bottompanel)
        self.split2.SplitVertically(self.topleftpanel, self.toprightpanel)
        self.split1.SetMinimumPaneSize(380)
        self.split2.SetMinimumPaneSize(240)
        self.Center()
        
        menuBar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        exit = file.Append(wx.ID_EXIT,'Exit','k')
        menuBar.Append(file,'File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.Quit,exit)
        self.SetTitle("MoneyMaster-3000")
        
        text = wx.StaticText(self.topleftpanel, -1, '�g vil reikna', (16, 25))
        font = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.NORMAL,underline=False)
        text.SetFont(font)
        text.SetForegroundColour("Steel blue")
        c1 =  wx.StaticText(self.topleftpanel, -1, 'Sparna�', (43, 55))
        font2 = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        c1.SetFont(font2)
        btn1 = platebtn.PlateButton(self.topleftpanel, label="Uppsafna�ur sparna�ur", style=platebtn.PB_STYLE_SQUARE,pos=(55, 80),size=(-1,-1))
        btn2 = platebtn.PlateButton(self.topleftpanel, label="T�mi sparna�ar", style=platebtn.PB_STYLE_SQUARE,pos=(55, 103),size=(-1,-1))
        btn3 = platebtn.PlateButton(self.topleftpanel, label="Sparna�artakmark", style=platebtn.PB_STYLE_SQUARE,pos=(55, 128),size=(-1,-1))        
        c2 =  wx.StaticText(self.topleftpanel, -1, 'L�n', (43, 153))
        c2.SetFont(font2)
        btn4 = platebtn.PlateButton(self.topleftpanel, label="Ver�trygg� l�n", style=platebtn.PB_STYLE_SQUARE,pos=(55, 178),size=(-1,-1))
        btn5 = platebtn.PlateButton(self.topleftpanel, label="�ver�trygg� l�n", style=platebtn.PB_STYLE_SQUARE,pos=(55, 201),size=(-1,-1))
        c3 =  wx.StaticText(self.topleftpanel, -1, 'Tekjur', (43, 226))
        c3.SetFont(font2)
        btn5 = platebtn.PlateButton(self.topleftpanel, label="R��st�funartekjur", style=platebtn.PB_STYLE_SQUARE,pos=(55, 251),size=(-1,-1))
        
        
        
        title1 = wx.StaticText(self.toprightpanel,-1,'Skr��u inn uppsafna�an sparna�',pos=(28,25))
        title1.SetFont(font2)
        right = -70
        down = -140
        label1 = wx.StaticText(self.toprightpanel, -1, 'M�na�arlegur sparna�ur',pos=(100+right,202+down))
        self.inputTxt1 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,200+down))

        
        label2 = wx.StaticText(self.toprightpanel, -1, 'Vi�mi�unart�mi',pos=(100+right,232+down))
        self.inputTxt2 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,230+down))
        
        label3 = wx.StaticText(self.toprightpanel, -1, 'Sparna�armarkmi� *',pos=(100+right,260+down))
        self.inputTxt3 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,262+down))
        
        label4 = wx.StaticText(self.toprightpanel, -1, 'Sparna�art�mi *',pos=(100+right,290+down))
        self.inputTxt4 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,292+down))
        
        label5 = wx.StaticText(self.toprightpanel, -1, 'Fj�ldi m�na�a *',pos=(100+right,320+down))
        self.inputTxt5 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,322+down))
       
        note = wx.StaticText(self.toprightpanel,-1,'* : -1 ef ekki � vi�',pos=(101+right,320+down+38))
        font = wx.Font(8, wx.ROMAN, wx.NORMAL, wx.BOLD,underline=False)
        note.SetForegroundColour("red")
        note.SetFont(font)
       
        piggy = wx.Image('piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self.toprightpanel,-1,piggy,pos=(345,60))
        
        sedlabanki = wx.Image('sedlabanki.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        logoGraphic = wx.StaticBitmap(self.bottompanel,-1,sedlabanki,pos=(640,20)) 
        
        plot = wx.StaticText(self.toprightpanel,-1,'Plot (matplotlib � framt��inni)',pos=(440+right,490+down))
        plotGraphic = wx.Image('chart_line.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        plot = wx.StaticBitmap(self.toprightpanel,-1,plotGraphic,pos=(413+right,490+down)) 
        
        btnSparnadur = wx.Button(self.toprightpanel,label="�fram",pos=(240+right,322+down+30),size=(111,-1))
        btnSparnadur.Bind(wx.EVT_BUTTON, self.displaySparnadur)
        

    def displaySparnadur(self,event):
        input1 = self.inputTxt1.GetValue()
        input2 = self.inputTxt2.GetValue()
        input3 = self.inputTxt3.GetValue()
        input4 = self.inputTxt4.GetValue()
        input5 = self.inputTxt5.GetValue()
        spar = Savings.Savings(int(input1),float(input2),float(input3),float(input4),float(input5))
        someInfo = wx.StaticText(self.bottompanel, -1, str(spar),(15,10))
        font = wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD,underline=False)
        someInfo.SetFont(font)
        someInfo.SetForegroundColour("blue")
  
        
    
    def Quit(self,event):
        self.Close()

app = wx.App(0)
win = MainFrame(None, -1, "Moneys", (50, 50), (800, 600))
win.Show()
app.MainLoop()