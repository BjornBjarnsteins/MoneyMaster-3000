#!/usr/bin/env python
# -*- coding: cp1252 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Sun Feb 09 20:47:25 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
#----------------------------------------------------------------------
#icons teki� fr� http://www.gentleface.com/free_icon_set.html

#b�i� var til �etta app me� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/ til hli�sj�nar
import defAccount, defLoan,Lan,Reikningar,calcSparnadur,calcLan

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
    
        plot_icon = wx.Image('icons/plot2_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(plot_icon)
        excel_icon = wx.Image('icons/excel_icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        il.Add(excel_icon)      
        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())
        
        imID = 1;
        self.AddPage(defAccount.TabPanel(self), "Home                   " ,imageId=imID)
        imID +=1
        self.AddPage(defAccount.TabPanel(self), "Skilgreina",imageId=imID)
        imID +=1
        self.AddSubPage(defAccount.TabPanel(self),"Reikning",imageId=0)
        self.AddSubPage(defLoan.TabPanel(self),"L�n",imageId=0)
        self.AddPage(Reikningar.TabPanel(self), "Sko�a               ",imageId=imID)
        imID +=1
        self.AddSubPage(Reikningar.TabPanel(self),"Reikninga",imageId=0)
        self.AddSubPage(Lan.TabPanel(self),"L�n",imageId=0)
        self.AddPage(calcSparnadur.TabPanel(self),"Reikniv�l",imageId = imID)
        self.AddSubPage(calcSparnadur.TabPanel(self),"Sparna�ur",imageId=0)
        self.AddSubPage(calcLan.TabPanel(self),"L�n",imageId=0)
        imID +=1
        self.AddPage(defAccount.TabPanel(self),"Peningast�ff",imageId=imID)
        imID +=1
        self.AddPage(defAccount.TabPanel(self),"Plot",imageId=imID)
        self.AddSubPage(defAccount.TabPanel(self),"44")
        imID +=1
        self.AddPage(defAccount.TabPanel(self),"Faux Excel",imageId=imID)
        imID +=1
        self.AddPage(defAccount.TabPanel(self),"Anna�",imageId=imID)
        
        
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.SetMinSize((600,100))
        
        wx.FutureCall(100, self.AdjustSize)
        
#fall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/

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
        event.Skip()

#fall copy-pastea� fr� http://www.blog.pythonlibrary.org/2009/12/03/the-book-controls-of-wxpython-part-1-of-2/
    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()
        
########################################################################

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        coin = wx.Icon('coins.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(self,coin)
        self.bottomwindow = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)                
        self.panel = wx.Panel(self)
        self.notebook = TreeSidebar(self.panel)
        self.panel.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "PT Sans"))
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
        self.bottomwindow.SetMinSize((800,200))
        self.bottomwindow.SetScrollRate(10, 10)
        self.panel.SetMinSize((800,500))
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