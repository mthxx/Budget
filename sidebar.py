from gi.repository import Gtk, Gio

class Sidebar():

    def __init__(self):

        # Create Grid, Sidebar, List, and Buttons
        self.grid = Gtk.Grid()
        self.menuListBox = Gtk.ListBox()
        self.menuScrolledWindow = Gtk.ScrolledWindow()
        self.menuViewport = Gtk.Viewport()
        self.buttons = []
        for i in range(0,10):
            self.buttons.append(Gtk.Button("Testing"))
            
        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",235)
        for i in range(0,10):
            self.buttons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.buttons[i].set_property("height-request", 60)
            self.buttons[i].set_property("width-request", 215)
            
        # Add buttons to menu 
        for i in range(0,10):
            self.menuListBox.add(self.buttons[i])
            
        # Add items to Grid 
        self.menuViewport.add(self.menuListBox)
        self.menuScrolledWindow.add(self.menuViewport)
        self.grid.add(self.menuScrolledWindow)
