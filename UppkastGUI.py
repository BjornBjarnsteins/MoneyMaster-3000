# -*- coding: cp1252 -*-
import wx
import wx.lib.platebtn as platebtn
import Loan
import storage
import Savings  
import locale
locale.setlocale( locale.LC_ALL, 'icelandic')
import wx.lib.scrolledpanel as scrolled

#Ath, það þarf að downloada wxPython til að geta keyrt forritið,
#farið á wxpython.org til að dla

class MainFrame(wx.Frame):

    def __init__(self,parent,id,title,position,size):
        coin = wx.Icon('coins.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.__init__(self, parent, id, title, position, size)
        wx.Frame.SetIcon(self,coin)
        self.split1 = wx.SplitterWindow(self)
        self.split2 = wx.SplitterWindow(self.split1)
        self.bottompanel = wx.PyScrolledWindow(self.split1, -1, style=wx.TAB_TRAVERSAL)
        self.bottompanel.SetBackgroundColour('white')
        self.topleftpanel = wx.Panel (self.split2)
        self.topleftpanel.SetBackgroundColour('white')
        self.toprightpanel = wx.Panel(self.split2)

        self.split1.SplitHorizontally(self.split2, self.bottompanel)
        self.split2.SplitVertically(self.topleftpanel, self.toprightpanel)
        self.split1.SetMinimumPaneSize(480)
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
        
        text = wx.StaticText(self.topleftpanel, -1, 'SIDEBAR', (16, 25))
        font = wx.Font(12, wx.SCRIPT, wx.ITALIC, wx.NORMAL,underline=False)
        text.SetFont(font)
        text.SetForegroundColour("Steel blue")
        c1 =  wx.StaticText(self.topleftpanel, -1, 'Reiknivél', (43, 55))
        font2 = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        c1.SetFont(font2)
        btn1 = platebtn.PlateButton(self.topleftpanel, label="Sparnaður", style=platebtn.PB_STYLE_SQUARE,pos=(55, 80),size=(-1,-1))
        btn2 = platebtn.PlateButton(self.topleftpanel, label="Lán", style=platebtn.PB_STYLE_SQUARE,pos=(55, 103),size=(-1,-1))
        btn3 = platebtn.PlateButton(self.topleftpanel, label="Ráðstöfunartekjur", style=platebtn.PB_STYLE_SQUARE,pos=(55, 128),size=(-1,-1))        
        
        title1 = wx.StaticText(self.toprightpanel,-1,'Fyrst þarf að skilgreina reikning',pos=(28,20))
        title1.SetFont(font2)
        right = -70
        down = -150
        label1 = wx.StaticText(self.toprightpanel, -1, 'Nafn reiknings',pos=(100+right,202+down))
        self.inputTxt1 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,200+down))

        
        label2 = wx.StaticText(self.toprightpanel, -1, 'Upphafleg innistæða',pos=(100+right,232+down))
        self.inputTxt2 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,230+down))
        
        label3 = wx.StaticText(self.toprightpanel, -1, 'Ársvextir',pos=(100+right,260+down))
        self.inputTxt3 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,262+down))
        
        label4 = wx.StaticText(self.toprightpanel, -1, 'Verðtrygging',pos=(100+right,294+down))
        
        self.input41 = wx.RadioButton(self.toprightpanel, -1, 'Já',pos=(244+right,295+down),style=wx.RB_GROUP)
        self.input42 = wx.RadioButton(self.toprightpanel, -1, 'Nei',pos=(290+right,295+down))

        label5 = wx.StaticText(self.toprightpanel, -1, 'Binditími',pos=(100+right,327+down))
        self.inputTxt5 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(240+right,323+down))
       
        note = wx.StaticText(self.toprightpanel,-1,'Smellið á litla graf-hnappann til\nað teikna niðurstöður á línuriti',pos=(388+right,317+down+38))
        font = wx.Font(8, wx.ROMAN, wx.NORMAL, wx.BOLD,underline=False)
        note.SetForegroundColour("red")
        note.SetFont(font)
        
        btnSparnadur = wx.Button(self.toprightpanel,label="Prenta upplýsinga",pos=(240+right,355+down),size=(111,-1))
        btnSparnadur.Bind(wx.EVT_BUTTON, self.displaySparnadur)
        
        title2 = wx.StaticText(self.toprightpanel,-1,'Velja svo aðgerð til að framkvæma',pos=(96+right,359+down+46))
        title2.SetFont(font2)
        
        
        label61 = wx.StaticText(self.toprightpanel, -1, 'Staða reiknings eftir',pos=(96+right,347+down+90),size=(-1,-1))
        label62 = wx.StaticText(self.toprightpanel, -1, 'i til j mánuði, þar sem',pos=(249+right,347+down+90),size=(-1,-1))
        label63 = wx.StaticText(self.toprightpanel, -1, 'upphæð',pos=(96+right,372+down+86),size=(-1,-1))
        label64 = wx.StaticText(self.toprightpanel, -1, 'hefur verið lögð inn hvern mánuð',pos=(203+right,372+down+86),size=(-1,-1)) 
        
        self.inputTxt61 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(207+right,355+down+78),size=(35,20))
        self.inputTxt61.SetValue('i-j')
        self.inputTxt62 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(150+right,347+down+106),size=(45,20))
        
        
        btnframvinda = wx.Button(self.toprightpanel,label="Reikna út framvindu",pos=(430+right,346+down+103),size=(-1,-1))
        #btnSparnadur.Bind(wx.EVT_BUTTON, self.displaySparnadur)
        btnframvinda.Bind(wx.EVT_BUTTON, self.displayProgression)
        
        plotGraphic = wx.Image('chart_line.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        plot1 = wx.StaticBitmap(self.toprightpanel,-1,plotGraphic,pos=(571+right,344+down+110)) 

    #Eftir: m er upphæð sem tekist hefur að safna á M mánuðum með monthly sparnaði á mánuði og má taka út strax.

        label71 = wx.StaticText(self.toprightpanel, -1, 'Reikna upphæð sem tekist hefur að safna á ',pos=(96+right,354+down+145),size=(-1,-1))
        label72 = wx.StaticText(self.toprightpanel, -1, 'með',pos=(96+right,354+down+167),size=(-1,-1))
        label73 = wx.StaticText(self.toprightpanel, -1, 'sparnaði á mánuði og má taka út strax',pos=(183+right,354+down+167),size=(-1,-1)) 
        
        self.inputTxt71 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(332+right,354+down+144),size=(35,20))
        self.inputTxt72 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(130+right,354+down+165),size=(45,20))
        btnsave = wx.Button(self.toprightpanel,label="Reikna út sparnað",pos=(430+right,354+down+160),size=(-1,-1))

    #Eftir: m er fjöldi mánaða sem það tekur að safna upp X pening a reikning þ.a. það megi taka hann út strax.
        arrow1 = wx.Image('right.gif',wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        arrow1Graphic = wx.StaticBitmap(self.toprightpanel,-1,arrow1,pos=(335,354+down+102))
        arrow2 = wx.Image('right.gif',wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        arrow2Graphic = wx.StaticBitmap(self.toprightpanel,-1,arrow1,pos=(335,354+down+165))
        arrow3 = wx.Image('right.gif',wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        arrow4Graphic = wx.StaticBitmap(self.toprightpanel,-1,arrow1,pos=(335,354+down+224))
        
        label81 = wx.StaticText(self.toprightpanel, -1, 'Reikna fjöldi mánaða sem það tekur að safna upp ',pos=(96+right,354+down+210),size=(-1,-1))
        label82 = wx.StaticText(self.toprightpanel, -1, 'pening á reikning með',pos=(96+right,354+down+230),size=(-1,-1))
        label83 = wx.StaticText(self.toprightpanel, -1, 'sparnaði á mánuði.',pos=(280+right,354+down+230),size=(-1,-1)) 
        
        self.inputTxt81 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(360+right,354+down+206),size=(35,20))
        self.inputTxt82 = wx.TextCtrl(self.toprightpanel, -1, '',pos=(225+right,354+down+230),size=(45,20))
        btnmonths = wx.Button(self.toprightpanel,label="Reikna út sparnað",pos=(430+right,354+down+220),size=(-1,-1))
        

        piggy = wx.Image('piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self.toprightpanel,-1,piggy,pos=(345,60))
        
        sedlabanki = wx.Image('sedlabanki.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        logoGraphic = wx.StaticBitmap(self.bottompanel,-1,sedlabanki,pos=(640,20)) 
        


        
    def displaySparnadur(self,event):
        #hreinsa fyrst það sem var í console á undan
        cleanUpBottomPanel(self)
        
        input1 = self.inputTxt1.GetValue()
        input2 = self.inputTxt2.GetValue()
        input3 = self.inputTxt3.GetValue()
        if self.input41.GetValue():
            input4 = True
        else:
            input4 = False
        input5 = self.inputTxt5.GetValue()
        
        extraheight = "\n"
        spar = Savings.Savings(input1,float(input2),float(input3),input4,float(input5))
        someInfo = wx.StaticText(self.bottompanel, -1, str(spar)+extraheight,(15,10))
        font = wx.Font(16, wx.SCRIPT, wx.NORMAL, wx.NORMAL,underline=False)
        someInfo.SetFont(font)
        someInfo.SetForegroundColour("blue")
        #self.bottompanel.SetScrollbars(0,50,0,20)
        self.bottompanel.SetScrollRate(1,1)
        self.bottompanel.SetVirtualSize(someInfo.GetVirtualSize())
    
    def displayProgression(self,event):
        
        #hreinsum panel fyrst
        cleanUpBottomPanel(self)
        
        input1 = self.inputTxt1.GetValue()
        input2 = self.inputTxt2.GetValue()
        input3 = self.inputTxt3.GetValue()
        if self.input41.GetValue():
            input4 = True
        else:
            input4 = False
        input5 = self.inputTxt5.GetValue()
        
        extraheight = "\n"
        spar = Savings.Savings(input1,float(input2),float(input3),input4,float(input5))
        
        
        range = self.inputTxt61.GetValue()
        m = str(range).split('-')
        m1 = int(m[0])
        m2 = int(m[1])
        monthly = float(self.inputTxt62.GetValue())
        prog = spar.progression(monthly, m1,m2)
        text = ''
        for entry in prog:
            text = text + str(entry)+ "\n"
        someInfo = wx.StaticText(self.bottompanel, -1, text+extraheight,(15,10))
        font = wx.Font(16, wx.SCRIPT, wx.NORMAL, wx.NORMAL,underline=False)
        someInfo.SetFont(font)
        someInfo.SetForegroundColour("blue")
        #self.bottompanel.SetScrollbars(0,50,0,20)
        self.bottompanel.SetScrollRate(1,1)
        self.bottompanel.SetVirtualSize(someInfo.GetVirtualSize())
    
    def Quit(self,event):
        self.Close()

def cleanUpBottomPanel(self):
    for child in self.bottompanel.GetChildren():
        if type(child) != wx._controls.StaticBitmap:
            child.Destroy()

app = wx.App(0)
win = MainFrame(None, -1, "Moneys", (50, 50), (800, 700))
win.SetMaxSize((800,700))
win.Show()
app.MainLoop()