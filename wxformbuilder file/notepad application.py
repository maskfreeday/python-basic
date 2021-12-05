
import wx
from wx.core import FD_OPEN, FD_SAVE
from notepad import MyFrame1#作業檔名(notebook) 引用的面板(MyFrame1一般的視窗)
from notepad import MyDialog1
import codecs
import os 

class notepad1 ( MyFrame1 ):

#1. 建立新檔	
	def newfile(self , event):
		w1.SetTitle("記事本")
		self.m_textCtrl1.SetValue("")

# 2. 開啟舊檔
	def opennew(self , event):
		oldfile = wx.FileSelector(
			"開啟檔案",
			wildcard = "文字檔|*.txt",
			flags=wx.FD_OPEN
		)
		with codecs.open(oldfile, "r", "utf-8") as file:
			self.m_textCtrl1.SetValue(file.read())
		oldfile = os.path.basename(str(oldfile))
		w1.SetTitle(f"記事本-{oldfile}")
# 3. 儲存檔案
	def save(self , event):
		filename = str(self.GetTitle()).split("記事本-")
		oldtitle = str(self.GetTitle()).split("-")
		if len(oldtitle) == 1:
			oldfile = wx.FileSelector(
				"儲存檔案",
				wildcard = "文字檔|*.txt",
				flags=wx.FD_SAVE
			)
			with codecs.open(oldfile, "w", "utf-8") as file:
				file.write(self.m_textCtrl1.GetValue())#
			oldfile = os.path.basename(str(oldfile))
			self.SetTitle(f"記事本-{oldfile}")
		else:
			with codecs.open(filename[1], "w","utf-8") as file:
				file.write(self.m_textCtrl1.GetValue())
# 4. 結束程式
	def exit( self, event ):
		wx.Exit()
# 5. 作者介紹
	def author( self, event ):
		w2.Show()

class notepad2 ( MyDialog1 ):
	def stranger( self, event ):
		w2.SetTitle("作者介紹")
		



w=wx.App()
w1=notepad1(None)
w2=notepad2(None)
w1.Show()
w.MainLoop()