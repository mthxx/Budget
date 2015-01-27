from gi.repository import Gtk, Gio

class Projections():
        
    def __init__(self):
        self.grid = Gtk.Grid(name="projectionsGrid")
        
        self.sideGrid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        
        # Side Grid Styling 
        self.sideGrid.set_vexpand(True)
        self.sideGrid.set_property("width-request",200)
        
        # Content Grid Styling 
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
    
        self.contentGrid.set_margin_end(50)
        self.contentGrid.set_margin_bottom(50)

        self.generate_sidebar()
        self.generate_day_view()

        self.grid.attach(self.sideGrid, 0, 0, 1, 1)
        self.grid.attach(self.contentGrid, 1, 0, 1, 1)

    def generate_day_view(self):
        
        self.label = Gtk.Label("Janaury 1st, 2015")        

        self.contentGrid.attach(self.label, 0,0,7,1)
        
        for i in range(0, 42):
            self.button = Gtk.Button(i)
            self.button.set_relief(Gtk.ReliefStyle.NONE)
            if i <= 6:
                self.contentGrid.attach(self.button,i,1,1,1)
            elif i > 6 and i <= 13:
                self.contentGrid.attach(self.button,(i-7),2,1,1)
            elif i > 13 and i <= 20:
                self.contentGrid.attach(self.button,(i-14),3,1,1)
            elif i > 20 and i <= 27:
                self.contentGrid.attach(self.button,(i-21),4,1,1)
            elif i > 27 and i <= 34:
                self.contentGrid.attach(self.button,(i-28),5,1,1)
            elif i > 34:
                self.contentGrid.attach(self.button,(i-35),6,1,1)
 
    def generate_sidebar(self):
        self.dayButton = Gtk.Button("Day")
        self.weekButton = Gtk.Button("Week")
        self.monthButton = Gtk.Button("Month")
        self.incomeButton = Gtk.Button("Projected Income")
        self.expenseButton = Gtk.Button("Projected Expenses")
        
        self.dayButton.set_property("width-request",60)
        self.dayButton.set_margin_start(20)
        self.dayButton.set_margin_top(80)
        
        self.weekButton.set_property("width-request",50)
        self.weekButton.set_margin_start(20)
        self.weekButton.set_margin_top(20)
        
        self.monthButton.set_property("width-request",50)
        self.monthButton.set_margin_start(20)
        self.monthButton.set_margin_top(20)
        
        self.incomeButton.set_property("width-request",50)
        self.incomeButton.set_margin_start(20)
        self.incomeButton.set_margin_top(50)
        
        self.expenseButton.set_property("width-request",50)
        self.expenseButton.set_margin_start(20)
        self.expenseButton.set_margin_top(20)

        self.sideGrid.attach(self.dayButton, 0,0,1,1)
        self.sideGrid.attach(self.weekButton, 0,1,1,1)
        self.sideGrid.attach(self.monthButton, 0,2,1,1)
        self.sideGrid.attach(self.incomeButton, 0,3,1,1)
        self.sideGrid.attach(self.expenseButton, 0,4,1,1)

