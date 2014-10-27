from gi.repository import Gtk, Gio

class Reports():
        
    def __init__(self):
        self.grid = Gtk.Grid()

        self.contentGrid = Gtk.Grid()
        self.scrolledWindow = Gtk.ScrolledWindow()
        self.viewport = Gtk.Viewport()
        
        self.viewport.add(self.contentGrid)
        self.scrolledWindow.add(self.viewport)
        self.grid.attach(self.scrolledWindow,0,0,1,1)


        
