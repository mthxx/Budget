from gi.repository import Gtk, Gio

class Sidebar():

    def __init__(self):

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
        
        self.categoryNotebook = Gtk.Notebook()
        
        self.menuButtons = []
        self.subMenuButtons = []
            
        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",200)
        
        self.subMenuScrolledWindow.set_vexpand(True)
        self.subMenuScrolledWindow.set_property("width-request",100)
        
        # Add items to Grid 
        self.menuViewport.add(self.menuListBox)
        self.subMenuViewport.add(self.subMenuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.subMenuScrolledWindow.add(self.subMenuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,1)
        self.grid.attach(self.subMenuScrolledWindow,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)


    def menu_clicked(self,button):
        (button.get_label())
