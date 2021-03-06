#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wx
import  wx.lib.mixins.listctrl  as  listmix
import Loan
import Savings
import storage
import gettext
#�essi k��i er a� hluta til copy pastea�ur fra http://www.blog.pythonlibrary.org/2011/01/04/wxpython-wx-listctrl-tips-and-tricks/
#eg var me� �ennan tutorial til hli�sj�nar allan t�mann
a = storage.loadLoans()
dictLoans = {}
index = 1
for i in a:
    vtr = ''
    if i.dex:
        vtr = 'J�'
    else:
        vtr = 'Nei'
    dictLoans[index]=(str(i.name),str(i.amount),str(i.interest),str(i.m),vtr)
    index += 1
        
class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        
class TabPanel(wx.Panel, listmix.ColumnSorterMixin):

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.SetFont(wx.Font(10,family=wx.FONTFAMILY_SWISS, style=wx.FONTSTYLE_NORMAL,faceName= "PT Sans",
                                           weight=wx.NORMAL,encoding=wx.FONTENCODING_SYSTEM))
        self.SetBackgroundColour("white")
        self.createAndLayout()
        
    def createAndLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.list = TestListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT
                                 | wx.BORDER_NONE
                                 | wx.LC_EDIT_LABELS
                                 | wx.LC_SORT_ASCENDING)
        sizer.Add(self.list, 1, wx.EXPAND)
        self.populateList()
        
        self.itemDataMap = dictLoans
        listmix.ColumnSorterMixin.__init__(self, 5)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        
    def populateList(self):
        self.list.InsertColumn(0, "L�n")
        self.list.InsertColumn(1, "H�fu�st�ll")
        self.list.InsertColumn(2, "�rsvextir")
        self.list.InsertColumn(3, "Lengd (m�nu�ir)")
        self.list.InsertColumn(4, "Ver�tryggt")
        items = dictLoans.items()
        
        for key, data in items:
            index = self.list.InsertStringItem(sys.maxint, data[0])
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            self.list.SetStringItem(index, 3, data[3])
            self.list.SetStringItem(index, 4, data[4])
            self.list.SetItemData(index, long(key))
    
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1,80)
        self.list.SetColumnWidth(2, 70)
        self.list.SetColumnWidth(3, 120)
        self.list.SetColumnWidth(4, 80)
        
        # show how to select an item
        self.list.SetItemState(5, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        self.currentItem = 0
        
    def refreshList(self):
        self.list.DeleteAllItems()
        a = storage.loadLoans()
        dictLoans = {}
        index = 1
        for i in a:
            vtr = ''
            if i.dex:
                vtr = 'J�'
            else:
                vtr = 'Nei'
            dictLoans[index]=(str(i.name),str(i.amount),str(i.interest),str(i.m),vtr)
            index += 1
        items = dictLoans.items()
        for key, data in items:
            index = self.list.InsertStringItem(sys.maxint, data[0])
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            self.list.SetStringItem(index, 3, data[3])
            self.list.SetStringItem(index, 4, data[4])
            self.list.SetItemData(index, long(key))
        
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.list
         
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Lan")
        panel = TabPanel(self)
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp()
    frame = Frame()
    app.MainLoop()

