# First things, first. Import the wxPython package.
import wx,os

class GUIManager(wx.Frame):
    def __init__(self, parent, title):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.dirname=''

        path=os.getcwd()
                
        wx.Frame.__init__(self, parent, title=title, size=(240, 250), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        selfsize=(300, 200)
        top_panel = wx.Panel(self,-1)
        box = wx.BoxSizer(wx.VERTICAL)
        
        # Setting up the menu.
        filemenu= wx.Menu()
        helpmenu= wx.Menu()
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        helpmenuhelp=helpmenu.Append(wx.ID_OPEN, "&Help"," Open Help File")
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"&Help")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.on_help, helpmenuhelp)
        
        bottom_panel=wx.Panel(self, -1)
        
        box.Add(top_panel, 1,wx.EXPAND | wx.ALL,1)
        box.Add(bottom_panel, 1,wx.EXPAND | wx.ALL, 1)

        #Top Panel
        self.dirtitle = wx.StaticText(top_panel, label="Factor 1:",pos=(5, 3))
        self.editname = wx.TextCtrl(top_panel, size=(260, 24),pos=(0, 24))

        self.dirtitle = wx.StaticText(top_panel, label="Factor 2:",pos=(5, 49))
        self.editname = wx.TextCtrl(top_panel, size=(260, 24),pos=(0, 70))

        #Bottom Panel
        
        wx.Button(bottom_panel, 2, 'Generate', (0,0))

        #Layout sizers
        self.SetSize(selfsize)
        self.SetSizer(box)

        self.Show()

    def OnExit(self,e):
        self.Destroy()
        try:
            l2.server_sock.close()
            self.update_status(e,'Service Stopped',0)
        except:
            print "Attempted to Cleanup BT when not active"


    def on_help(self,e):
        print 'help'

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, "Version 1.37, Limited release 11-2-16 for testing purposes only.", "LIAM"+u"\u2122"+" Windows GUI Version 1.3", wx.OK)
        self.update_status(e,'About',0)
        dlg.ShowModal()
        dlg.Destroy()
        self.update_status(e,'',1)
        


# Next, create an application object.
app = wx.App()

# Then a frame.
frm = GUIManager(None, 'GUIManager')

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
