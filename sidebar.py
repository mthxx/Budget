from gi.repository import Gtk, Gio

class Sidebar():

    def __init__(self,values):

        # Create Grid, Sidebar, List, and Buttons
        self.grid = Gtk.Grid()
       
        self.menuListBox = Gtk.ListBox()

        self.menuScrolledWindow = Gtk.ScrolledWindow()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        
        self.menuViewport = Gtk.Viewport()
        self.contentViewport = Gtk.Viewport()
        
        self.buttons = []
        
        for i in range(0,len(values)):
            self.buttons.append(Gtk.Button(values[i]))
            
        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",235)
        for i in range(0,len(values)):
            self.buttons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.buttons[i].set_property("height-request", 60)
            self.buttons[i].set_property("width-request", 215)
            
        # Add buttons to menu 
        for i in range(0,len(values)):
            self.menuListBox.add(self.buttons[i])
            
        # Add items to Grid 
        self.menuViewport.add(self.menuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,1)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)
