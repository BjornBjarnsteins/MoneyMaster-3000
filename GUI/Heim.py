#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import xlrd
import xlsgrid as XG
 
import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
class Heim(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
                             wx.BK_DEFAULT)
        
        self.panel1 = wx.Panel(self, wx.ID_ANY)
        self.panel2 = wx.Panel(self, wx.ID_ANY, size=(1, 1))
        self.panel2.SetMinSize((900,1000))
        self.panel1.SetBackgroundColour('white')
        self.panel3 = wx.Panel(self,wx.ID_ANY)
        self.panel3.SetBackgroundColour('white')

        filename = "infl2.xls"
        book = xlrd.open_workbook(filename, formatting_info=1)
        sheetname = "Sheet1"
        sheet = book.sheet_by_index(0)
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)

        self.xlsGrid = XG.XLSGrid(self.panel2)
        self.xlsGrid.PopulateGrid(book, sheet, texts, comments)
        self.xlsGrid.SetMinSize((900,500))
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(self.xlsGrid, 1, )
        self.panel2.SetSizer(sizer1)

        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(self.xlsGrid, 1, )
        self.panel2.SetSizer(sizer2)
        graph = wx.Image('inflationgraph.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        graph1 = wx.StaticBitmap(self.panel1,-1,graph,pos=(56,43))

        piggy = wx.Image('images/piggy.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap()
        piggyGraphic = wx.StaticBitmap(self.panel3,-1,piggy,pos=(214,152))

        self.AddPage(self.panel3,"Forsíða")
        self.AddPage(self.panel2,  "Verðlagsþróun (tafla)")
        self.AddPage(self.panel1, "Verðlagsþróun (graf)")
        
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
        
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

        
########################################################################
class Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Heim",size=(600,400))
        panel = wx.Panel(self)
        self.book = Heim(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(book, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()
