from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data() 
        
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
        
        for i in range (0,len(self.data.income)):
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.income, i)

            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.income[i][2])
            self.descriptionLabel = Gtk.Label(self.data.income[i][3])
            self.contentGrid.attach(self.dateLabel, self.dateOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.costLabel, self.costOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.descriptionLabel, self.descriptionOffsetLeft, self.entryOffsetTop + i, 1, 1)
        
        
        self.contentGrid.attach(self.dummyLabel3, 1, len(self.data.income) + 7, 2, 1)
        
        self.view = Sidebar(self.data.incomeSources, self.data.monthMenu) 
        
        # Attach Content
        self.view.contentViewport.add(self.contentGrid)
