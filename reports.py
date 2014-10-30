from gi.repository import Gtk, Gio, Gdk
from data import Data

class Reports():
        
    def __init__(self):
        self.css = Gtk.CssProvider()
        self.css.load_from_path("style.css")
        self.data = Data()

        self.grid = Gtk.Grid()
        
        self.contentGrid = Gtk.Grid()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        self.contentViewport = Gtk.Viewport()
        
        self.contentViewport.add(self.contentGrid)
        self.contentScrolledWindow.add(self.contentViewport)
        self.grid.attach(self.contentScrolledWindow,0,0,1,1)
        
        self.emptyLabel = Gtk.Label()

        self.grid.attach(self.emptyLabel,0,0,5,1)
        #self.grid.set_column_homogeneous(True)
        #self.grid.set_hexpand(True)

        self.contentScrolledWindow.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.grid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.2, 0.2, 0.2, 0.2))

        self.index = 0
        for i in range (0,len(self.data.income)):
            
            self.layoutGrid = Gtk.Grid()
            self.layoutGrid.set_column_homogeneous(True)
            self.layoutGrid.set_hexpand(True)
            
            self.emptyLabel = Gtk.Label()
            self.index = self.index + 2
            self.contentGrid.attach(self.emptyLabel,0, self.index, 5, 1)

            self.index = self.index + 3
            
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.expenses, i)

            self.categoryLabel = Gtk.Label(self.data.expenses[i][0][1])
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.expenses[i][2])
            self.descriptionLabel = Gtk.Label(self.data.expenses[i][3])
            
            self.costLabel.set_property("height-request", 35)
            
            self.layoutGrid.attach(self.categoryLabel, 0, 0, 1, 1)
            self.layoutGrid.attach(self.dateLabel, 1, 0, 1, 1)
            self.layoutGrid.attach(self.costLabel, 0, 1, 1, 1)
            self.layoutGrid.attach(self.descriptionLabel, 1, 1, 1, 1)
            
            self.layoutGrid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
            self.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)
            

