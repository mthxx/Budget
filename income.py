from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.menu = ['All','Income 1','Income 2','Income 3','Income 4','Income 5']
        self.subMenu = ['All','December','November','October','September','August','July','June','May','April','March','February','January']
        
        self.entryOffsetTop = 7
        
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5

        # Define Widgets
        self.contentGrid = Gtk.Grid()
        
        self.monthSpentLabel = Gtk.Label("Income")
        self.monthRemainingLabel = Gtk.Label("Remaining Income")
        self.percBudgetLabel = Gtk.Label("% Remaining")
        
        self.dummyLabel1 = Gtk.Label()
        self.dummyLabel2 = Gtk.Label()
        self.dummyLabel3 = Gtk.Label()
        
        self.monthSpentTotalLabel = Gtk.Label("$1,500")
        self.monthRemainingTotalLabel = Gtk.Label("$1,500")
        self.percBudgetTotalLabel = Gtk.Label("50.00%")
       
        self.dateLabel1 = Gtk.Label("January 1st")
        self.dateLabel2 = Gtk.Label("January 15th")
        self.dateLabel3 = Gtk.Label("February 1st")
        self.dateLabel4 = Gtk.Label("February 15th")
        self.dateLabel5 = Gtk.Label("March 1st")
        self.dateLabel6 = Gtk.Label("March 15th")
        self.dateLabel7 = Gtk.Label("April 1st")
        self.dateLabel8 = Gtk.Label("April 15th")
        self.dateLabel9 = Gtk.Label("May 1st")
        self.dateLabel10 = Gtk.Label("May 15th")

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
        
        self.descriptionLabel1 = Gtk.Label("Income 1")
        self.descriptionLabel2 = Gtk.Label("Income 2")
        self.descriptionLabel3 = Gtk.Label("Income 1")
        self.descriptionLabel4 = Gtk.Label("Tax Return")
        self.descriptionLabel5 = Gtk.Label("Income 1")
        self.descriptionLabel6 = Gtk.Label("Bonus")
        self.descriptionLabel7 = Gtk.Label("Income 1")
        self.descriptionLabel8 = Gtk.Label("Income 2")
        self.descriptionLabel9 = Gtk.Label("Income 1")
        self.descriptionLabel10 = Gtk.Label("Income 2")
        
        self.addEntryButton = Gtk.Button("Add")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        self.editEntryButton = Gtk.Button("Edit")
        self.editEntryPopover = Gtk.Popover.new(self.addEntryButton)
        
        # Widget Styling
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        # Build Content Area
        self.contentGrid.attach(self.monthSpentLabel, self.dateOffsetLeft, 2, 1, 1)
        self.contentGrid.attach(self.monthRemainingLabel, self.costOffsetLeft, 2, 1, 1)
        self.contentGrid.attach(self.percBudgetLabel, self.descriptionOffsetLeft, 2, 1, 1)
        
        self.contentGrid.attach(self.monthSpentTotalLabel, self.dateOffsetLeft, 3, 1, 1)
        self.contentGrid.attach(self.monthRemainingTotalLabel, self.costOffsetLeft, 3, 1, 1)
        self.contentGrid.attach(self.percBudgetTotalLabel, self.descriptionOffsetLeft, 3, 1, 1)
        
        self.contentGrid.attach(self.dummyLabel1, 1, 4, 5, 1)
        self.contentGrid.attach(self.addEntryButton, 2, 5, 1, 1)
        self.contentGrid.attach(self.editEntryButton, 4, 5, 1, 1)
        self.contentGrid.attach(self.dummyLabel2, 1, 6, 1, 1)
        
        self.contentGrid.attach(self.dateLabel10, self.dateOffsetLeft, self.entryOffsetTop, 1, 1)
        self.contentGrid.attach(self.paymentLabel10, self.costOffsetLeft, self.entryOffsetTop, 1, 1)
        self.contentGrid.attach(self.descriptionLabel10, self.descriptionOffsetLeft, self.entryOffsetTop, 1, 1)
        
        self.contentGrid.attach(self.dateLabel9, self.dateOffsetLeft, self.entryOffsetTop + 1, 1, 1)
        self.contentGrid.attach(self.paymentLabel9, self.costOffsetLeft, self.entryOffsetTop + 1, 1, 1)
        self.contentGrid.attach(self.descriptionLabel9, self.descriptionOffsetLeft, self.entryOffsetTop + 1, 1, 1)
        
        self.contentGrid.attach(self.dateLabel8, self.dateOffsetLeft, self.entryOffsetTop + 2, 1, 1)
        self.contentGrid.attach(self.paymentLabel8, self.costOffsetLeft, self.entryOffsetTop + 2, 1, 1)
        self.contentGrid.attach(self.descriptionLabel8, self.descriptionOffsetLeft, self.entryOffsetTop + 2, 1, 1)
        
        self.contentGrid.attach(self.dateLabel7, self.dateOffsetLeft, self.entryOffsetTop + 3, 1, 1)
        self.contentGrid.attach(self.paymentLabel7, self.costOffsetLeft, self.entryOffsetTop + 3, 1, 1)
        self.contentGrid.attach(self.descriptionLabel7, self.descriptionOffsetLeft, self.entryOffsetTop + 3, 1, 1)
        
        self.contentGrid.attach(self.dateLabel6, self.dateOffsetLeft, self.entryOffsetTop + 4, 1, 1)
        self.contentGrid.attach(self.paymentLabel6, self.costOffsetLeft, self.entryOffsetTop + 4, 1, 1)
        self.contentGrid.attach(self.descriptionLabel6, self.descriptionOffsetLeft, self.entryOffsetTop + 4, 1, 1)
        
        self.contentGrid.attach(self.dateLabel5, self.dateOffsetLeft, self.entryOffsetTop + 5, 1, 1)
        self.contentGrid.attach(self.paymentLabel5, self.costOffsetLeft, self.entryOffsetTop + 5, 1, 1)
        self.contentGrid.attach(self.descriptionLabel5, self.descriptionOffsetLeft, self.entryOffsetTop + 5, 1, 1)
        
        self.contentGrid.attach(self.dateLabel4, self.dateOffsetLeft, self.entryOffsetTop + 6, 1, 1)
        self.contentGrid.attach(self.paymentLabel4, self.costOffsetLeft, self.entryOffsetTop + 6, 1, 1)
        self.contentGrid.attach(self.descriptionLabel4, self.descriptionOffsetLeft, self.entryOffsetTop + 6, 1, 1)
        
        self.contentGrid.attach(self.dateLabel3, self.dateOffsetLeft, self.entryOffsetTop + 7, 1, 1)
        self.contentGrid.attach(self.paymentLabel3, self.costOffsetLeft, self.entryOffsetTop + 7, 1, 1)
        self.contentGrid.attach(self.descriptionLabel3, self.descriptionOffsetLeft, self.entryOffsetTop + 7, 1, 1)
        
        self.contentGrid.attach(self.dateLabel2, self.dateOffsetLeft, self.entryOffsetTop + 8, 1, 1)
        self.contentGrid.attach(self.paymentLabel2, self.costOffsetLeft, self.entryOffsetTop + 8, 1, 1)
        self.contentGrid.attach(self.descriptionLabel2, self.descriptionOffsetLeft, self.entryOffsetTop + 8, 1, 1)
        
        self.contentGrid.attach(self.dateLabel1, self.dateOffsetLeft, self.entryOffsetTop + 9, 1, 1)
        self.contentGrid.attach(self.paymentLabel1, self.costOffsetLeft, self.entryOffsetTop + 9, 1, 1)
        self.contentGrid.attach(self.descriptionLabel1, self.descriptionOffsetLeft, self.entryOffsetTop + 9, 1, 1)
        
        self.contentGrid.attach(self.dummyLabel3, 5, self.entryOffsetTop + 10, 2, 1)
        
        self.view = Sidebar(self.menu, self.subMenu) 
        
        # Attach Content
        self.view.contentViewport.add(self.contentGrid)
