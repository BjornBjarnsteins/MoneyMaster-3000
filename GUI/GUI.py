#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Sun Feb 09 20:47:25 2014
#
#ATHUGID!ATTENTION! YOU NEED TO DOWNLOAD THE BEAUTIFULSOUP LIBRARY BEFORE RUNNING THIS CODE

import wx
import webbrowser
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
#----------------------------------------------------------------------
#icons teki� fr� http://www.gentleface.com/free_icon_set.html

#b�i� var til �etta app me� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/ til hli�sj�nar
import defAccount, defLoan,Lan,Reikningar,calcSparnadur,calcLan,calcSavingsTime,calcDownPay,Heim

#hjalparfall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/
def getNextImageID(count):
    imID = 0
    while True:
        yield imID
        imID += 1
        if imID == count:
            imID = 0
            
class TreeSidebar(wx.Treebook):

    def __init__(self, parent):

        wx.Treebook.__init__(self, parent, wx.ID_ANY, style=wx.BK_DEFAULT)
        il = wx.ImageList(16, 16)
        arrow_icon = wx.Image('icons/arrow_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(arrow_icon)  
        home_icon = wx.Image('icons/home_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(home_icon)
        add_icon = wx.Image('icons/add_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(add_icon)
        accts_icon = wx.Image('icons/skoda_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(accts_icon)
        calc_icon = wx.Image('icons/calc_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(calc_icon)
        dollar_icon = wx.Image('icons/dollar_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(dollar_icon)
        excel_icon = wx.Image('icons/excel_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        il.Add(excel_icon)      
        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())
        imID = 1;
        self.AddPage(Heim.Heim(self),"Fors��a" ,imageId=imID)
                
        imID +=1
        self.AddPage(None, "Skilgreina   ",imageId=imID)
        imID +=1
        
        self.AddSubPage(defAccount.TabPanel(self),"Reikning",imageId=0)
        self.AddSubPage(defLoan.TabPanel(self),"L�n",imageId=0)
        self.AddPage(None, "Sko�a",imageId=imID)
        imID +=1
        self.AddSubPage(Reikningar.TabPanel(self),"Reikninga",imageId=0)
        self.AddSubPage(Lan.TabPanel(self),"L�n",imageId=0)
        self.AddPage(None,"Reikniv�l                       ",imageId = imID)
        self.AddSubPage(calcSparnadur.TabPanel(self),"Sparna�armarkmi� ",imageId=0)
        self.AddSubPage(calcSavingsTime.TabPanel(self),"Sparna�art�mabil",imageId=0)
        self.AddSubPage(calcDownPay.TabPanel(self),"Ni�urgrei�slur l�na",imageId=0)

        
        self.GetTreeCtrl().SetFont(wx.Font(10,family=wx.FONTFAMILY_SCRIPT, style=wx.FONTSTYLE_NORMAL, 
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))

        self.am = wx.BitmapButton(self.GetTreeCtrl(),-1,wx.Image('sedlabanki.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),pos=(31,340),style=wx.NO_BORDER)
        self.am.Bind(wx.EVT_BUTTON,self.openlink) 
        self.am.SetBitmapHover(wx.Image('sedlabankihover.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
		

        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.SetMinSize((600,100))
        
        wx.FutureCall(100, self.AdjustSize)
        
#fall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/
    def openlink(self,event):
        webbrowser.open('http://sedlabanki.is')
    def AdjustSize(self):
        #print self.GetTreeCtrl().GetBestSize()
        self.GetTreeCtrl().InvalidateBestSize()
        self.SendSizeEvent()
    
#fall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        self.GetPage(5).refreshList()
        self.GetPage(6).refreshList()


#fall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/
    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        if new == 8:
            self.GetPage(8).refreshList()
        if new == 9:
            self.GetPage(9).refreshList()
        if new == 10:
            self.GetPage(10).refreshList()
        event.Skip()
        
########################################################################

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        coin = wx.Icon('coins.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(self,coin)


        self.panel = wx.Panel(self)
        self.notebook = TreeSidebar(self.panel)
        
        self.bottomwindow = wx.ScrolledWindow(self, wx.ID_ANY)
        self.bottomwindow.SetScrollRate(5,5)
        
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer2.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.sizer2)
        self.__set_properties()
        self.__do_layout()
        menuBar = wx.MenuBar()
        file = wx.Menu()
        exit = file.Append(wx.ID_EXIT,'Exit','k')
        menuBar.Append(file,'File')
        self.Bind(wx.EVT_MENU,self.Exit,exit)
        self.SetMenuBar(menuBar)
        self.Center()
        # end wxGlade
        
    def Exit(self,event):
        self.Close()
        
    def __set_properties(self):
        # begin wxGlade: Frame.__set_properties
        self.SetTitle(_("MoneyMaster-3000"))
        self.SetSize((800, 700))
        self.bottomwindow.SetMinSize((8000,500))
        self.bottomwindow.SetScrollRate(10, 10)
        self.panel.SetMinSize((8000,500))
        self.panel.SetBackgroundColour(wx.Colour(223, 228, 255))
        self.bottomwindow.SetBackgroundColour("white")

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer.Add(self.panel, 1, wx.ALL | wx.EXPAND, 0)
        grid_sizer.Add(self.bottomwindow, 1, 0, 0)
        sizer.Add(grid_sizer, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade

# end of class Frame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame = Frame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame)
    frame.Show()

    app.MainLoop()
