# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 488,317 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,300 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"結束程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem4 )

		self.m_menubar2.Append( self.m_menu2, u"檔案" )

		self.m_menu3 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem5 )

		self.m_menubar2.Append( self.m_menu3, u"關於" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.newfile, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.opennew, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.save, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.exit, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.author, id = self.m_menuItem5.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def newfile( self, event ):
		event.Skip()

	def opennew( self, event ):
		event.Skip()

	def save( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()

	def author( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"作者介紹", pos = wx.DefaultPosition, size = wx.Size( 407,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"作者:許君源", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"信箱:fgr59123456@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"網站:https://www.youtube.com/channel/UCnTTMZxqmN49JYjVI9M4u8Q", wx.DefaultPosition, wx.Size( 400,200 ), 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.stranger )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def stranger( self, event ):
		event.Skip()


