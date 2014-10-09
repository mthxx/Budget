from gi.repository import Gtk, Gio

class Sidebar():

    def __init__(self,menu,subMenu):

        # Create Grid, Sidebar, List, and Buttons
        self.grid = Gtk.Grid()
       
        self.menuListBox = Gtk.ListBox()
        self.subMenuListBox = Gtk.ListBox()

        self.menuScrolledWindow = Gtk.ScrolledWindow()
        self.subMenuScrolledWindow = Gtk.ScrolledWindow()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        
        self.menuViewport = Gtk.Viewport()
        self.subMenuViewport = Gtk.Viewport()
        self.contentViewport = Gtk.Viewport()
        
        self.menuButtons = []
        self.subMenuButtons = []
        
        for i in range(0,len(menu)):
            self.menuButtons.append(Gtk.Button(menu[i]))
        
        for i in range(0,len(subMenu)):
            self.subMenuButtons.append(Gtk.Button(subMenu[i]))
            
        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",200)
        
        self.subMenuScrolledWindow.set_vexpand(True)
        self.subMenuScrolledWindow.set_property("width-request",100)
        
        for i in range(0,len(menu)):
            self.menuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.menuButtons[i].set_property("height-request", 60)
        
        for i in range(0,len(subMenu)):
            self.subMenuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.subMenuButtons[i].set_property("height-request", 60)
            
        # Add buttons to menu 
        for i in range(0,len(menu)):
            self.menuListBox.add(self.menuButtons[i])
        
        for i in range(0,len(subMenu)):
            self.subMenuListBox.add(self.subMenuButtons[i])
            
        # Add items to Grid 
        self.menuViewport.add(self.menuListBox)
        self.subMenuViewport.add(self.subMenuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.subMenuScrolledWindow.add(self.subMenuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,1)
        self.grid.attach(self.subMenuScrolledWindow,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)
