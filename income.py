from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Income():

    def __init__(self):
        # Define Sidebar Menu
        values = ['Income 1','Income 2','Income 3','Income 4','Income 5']
        
        # Define Widgets
        self.contentGrid = Gtk.Grid()
        self.incomeLabel = Gtk.Label("Income 1")
        self.buttons = []
        
        #Widget Styling
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)

        # Define Buttons
        for i in range(0,10):
            self.buttons.append(Gtk.Button("Button"))
            
        # Build Content Area
        self.contentGrid.attach(self.incomeLabel, 0,0,10,1)
        for i in range(0,10):
            self.contentGrid.attach(self.buttons[i],i,1,1,1)
        
        self.view = Sidebar(values) 
        
        # Attach Content
        self.view.grid.attach(self.contentGrid, 1, 0, 1, 1)
        


    def open_view(window, sidebar):
        window.add(sidebar.grid)
