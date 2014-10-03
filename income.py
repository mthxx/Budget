from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.values = ['All','Income 1','Income 2','Income 3','Income 4','Income 5']
        self.monthOffsetLeft = 1
        self.monthOffsetTop = 7
        # Define Widgets
        self.contentGrid = Gtk.Grid()
        self.incomeLabel = Gtk.Label("Income 1")
        
        self.currentMonthLabel = Gtk.Label("Current Month")
        self.yearToDateLabel = Gtk.Label("Year to date")
        
        self.dummyLabel1 = Gtk.Label()
        self.dummyLabel2 = Gtk.Label()
        self.currentMonthTotalLabel = Gtk.Label("$1,500")
        self.yearToDateTotalLabel = Gtk.Label("$28,500")
        
        self.paymentLabel1 = Gtk.Label("$1,500")
        self.paymentLabel2 = Gtk.Label("$1,500")
        self.paymentLabel3 = Gtk.Label("$1,500")
        self.paymentLabel4 = Gtk.Label("$1,500")
        self.paymentLabel5 = Gtk.Label("$1,500")
        self.paymentLabel6 = Gtk.Label("$1,500")
        self.paymentLabel7 = Gtk.Label("$1,500")
        self.paymentLabel8 = Gtk.Label("$1,500")
        self.paymentLabel9 = Gtk.Label("$1,500")
        self.paymentLabel10 = Gtk.Label("$1,500")
        self.paymentLabel11 = Gtk.Label("$1,500")
        self.paymentLabel12 = Gtk.Label("$1,500")
        self.paymentLabel13 = Gtk.Label("$1,500")
        self.paymentLabel14 = Gtk.Label("$1,500")
        self.paymentLabel15 = Gtk.Label("$1,500")
        self.paymentLabel16 = Gtk.Label("$1,500")
        self.paymentLabel17 = Gtk.Label("$1,500")
        self.paymentLabel18 = Gtk.Label("$1,500")
        self.paymentLabel19 = Gtk.Label("$1,500")
        
        self.addEntryButton = Gtk.Button("Add")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        
        self.januaryLabel = Gtk.Label("January:")
        self.februaryLabel = Gtk.Label("February:")
        self.marchLabel = Gtk.Label("March:")
        self.aprilLabel = Gtk.Label("April:")
        self.mayLabel = Gtk.Label("May:")
        self.juneLabel = Gtk.Label("June:")
        self.julyLabel = Gtk.Label("July:")
        self.augustLabel = Gtk.Label("August:")
        self.septemberLabel = Gtk.Label("September:")
        self.octoberLabel = Gtk.Label("October:")
        self.novemberLabel = Gtk.Label("November:")
        self.decemberLabel = Gtk.Label("December:")
        
        #Widget Styling
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.incomeLabel.set_justify(Gtk.Justification.RIGHT)
        
        self.januaryLabel.set_halign(Gtk.Align.END)
        self.februaryLabel.set_halign(Gtk.Align.END)
        self.marchLabel.set_halign(Gtk.Align.END)
        self.aprilLabel.set_halign(Gtk.Align.END)
        self.mayLabel.set_halign(Gtk.Align.END)
        self.juneLabel.set_halign(Gtk.Align.END)
        self.julyLabel.set_halign(Gtk.Align.END)
        self.augustLabel.set_halign(Gtk.Align.END)
        self.septemberLabel.set_halign(Gtk.Align.END)
        self.octoberLabel.set_halign(Gtk.Align.END)
        self.novemberLabel.set_halign(Gtk.Align.END)
        self.decemberLabel.set_halign(Gtk.Align.END)

        # Build Content Area
        self.contentGrid.attach(self.incomeLabel, 0,0,10,1)
        
        self.contentGrid.attach(self.currentMonthLabel, 3, 2, 1, 1)
        self.contentGrid.attach(self.yearToDateLabel, 6, 2, 1, 1)
        
        self.contentGrid.attach(self.currentMonthTotalLabel, 3, 3, 1, 1)
        self.contentGrid.attach(self.yearToDateTotalLabel, 6, 3, 1, 1)
        
        self.contentGrid.attach(self.dummyLabel1, 5, 4, 2, 1)
        
        self.contentGrid.attach(self.addEntryButton, 4, 5, 2, 1)

        self.contentGrid.attach(self.dummyLabel2, 5, 6, 2, 1)

        self.contentGrid.attach(self.januaryLabel, self.monthOffsetLeft, self.monthOffsetTop, 1, 1)
        self.contentGrid.attach(self.februaryLabel, self.monthOffsetLeft, self.monthOffsetTop + 1, 1, 1)
        self.contentGrid.attach(self.marchLabel, self.monthOffsetLeft, self.monthOffsetTop + 2, 1, 1)
        self.contentGrid.attach(self.aprilLabel, self.monthOffsetLeft, self.monthOffsetTop + 3, 1, 1)
        self.contentGrid.attach(self.mayLabel, self.monthOffsetLeft, self.monthOffsetTop + 4, 1, 1)
        self.contentGrid.attach(self.juneLabel, self.monthOffsetLeft, self.monthOffsetTop + 5, 1, 1)
        self.contentGrid.attach(self.julyLabel, self.monthOffsetLeft, self.monthOffsetTop + 6, 1, 1)
        self.contentGrid.attach(self.augustLabel, self.monthOffsetLeft, self.monthOffsetTop + 7, 1, 1)
        self.contentGrid.attach(self.septemberLabel, self.monthOffsetLeft, self.monthOffsetTop + 8, 1, 1)
        self.contentGrid.attach(self.octoberLabel, self.monthOffsetLeft, self.monthOffsetTop + 9, 1, 1)
        self.contentGrid.attach(self.novemberLabel, self.monthOffsetLeft, self.monthOffsetTop + 10, 1, 1)
        self.contentGrid.attach(self.decemberLabel, self.monthOffsetLeft, self.monthOffsetTop + 11, 1, 1)
        
        self.contentGrid.attach(self.paymentLabel1, self.monthOffsetLeft + 2, self.monthOffsetTop, 1, 1)
        self.contentGrid.attach(self.paymentLabel2, self.monthOffsetLeft + 5, self.monthOffsetTop, 1, 1)
        self.contentGrid.attach(self.paymentLabel3, self.monthOffsetLeft + 2, self.monthOffsetTop + 1, 1, 1)
        self.contentGrid.attach(self.paymentLabel4, self.monthOffsetLeft + 5, self.monthOffsetTop + 1, 1, 1)
        self.contentGrid.attach(self.paymentLabel5, self.monthOffsetLeft + 2, self.monthOffsetTop + 2, 1, 1)
        self.contentGrid.attach(self.paymentLabel6, self.monthOffsetLeft + 5, self.monthOffsetTop + 2, 1, 1)
        self.contentGrid.attach(self.paymentLabel7, self.monthOffsetLeft + 2, self.monthOffsetTop + 3, 1, 1)
        self.contentGrid.attach(self.paymentLabel8, self.monthOffsetLeft + 5, self.monthOffsetTop + 3, 1, 1)
        self.contentGrid.attach(self.paymentLabel9, self.monthOffsetLeft + 2, self.monthOffsetTop + 4, 1, 1)
        self.contentGrid.attach(self.paymentLabel10, self.monthOffsetLeft + 5, self.monthOffsetTop + 4, 1, 1)
        self.contentGrid.attach(self.paymentLabel11, self.monthOffsetLeft + 2, self.monthOffsetTop + 5, 1, 1)
        self.contentGrid.attach(self.paymentLabel12, self.monthOffsetLeft + 5, self.monthOffsetTop + 5, 1, 1)
        self.contentGrid.attach(self.paymentLabel13, self.monthOffsetLeft + 2, self.monthOffsetTop + 6, 1, 1)
        self.contentGrid.attach(self.paymentLabel14, self.monthOffsetLeft + 5, self.monthOffsetTop + 6, 1, 1)
        self.contentGrid.attach(self.paymentLabel15, self.monthOffsetLeft + 2, self.monthOffsetTop + 7, 1, 1)
        self.contentGrid.attach(self.paymentLabel16, self.monthOffsetLeft + 5, self.monthOffsetTop + 7, 1, 1)
        self.contentGrid.attach(self.paymentLabel17, self.monthOffsetLeft + 2, self.monthOffsetTop + 8, 1, 1)
        self.contentGrid.attach(self.paymentLabel18, self.monthOffsetLeft + 5, self.monthOffsetTop + 8, 1, 1)
        self.contentGrid.attach(self.paymentLabel19, self.monthOffsetLeft + 2, self.monthOffsetTop + 9, 1, 1)
        
        self.view = Sidebar(self.values) 
        
        # Attach Content
        self.view.grid.attach(self.contentGrid, 1, 0, 1, 1)
        


    def open_view(window, sidebar):
        window.add(sidebar.grid)
