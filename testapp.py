import wx
 
application = wx.App()
 
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム')
 
icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
frame.SetIcon(icon)
 
frame.Show()
 
application.MainLoop()
