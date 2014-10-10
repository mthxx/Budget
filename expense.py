from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data

class Expense():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data()

        self.entryOffsetTop = 8
        
        self.categoryOffsetLeft = 1
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5

        # Define Widgets
        self.contentGrid = Gtk.Grid()
        
        self.monthSpentLabel = Gtk.Label()
        self.monthRemainingLabel = Gtk.Label()
        self.percBudgetLabel = Gtk.Label()
        
        self.categoryTitleLabel = Gtk.Label("Category")
        self.dateTitleLabel = Gtk.Label("Date")
        self.costTitleLabel = Gtk.Label("Cost")
        self.descriptionTitleLabel = Gtk.Label("Description")
        
        self.dummyLabel1 = Gtk.Label()
        self.dummyLabel2 = Gtk.Label()
        self.dummyLabel3 = Gtk.Label()
        
        self.monthSpentTotalLabel = Gtk.Label("$145.40")
        self.monthRemainingTotalLabel = Gtk.Label("$154.60")
        self.percBudgetTotalLabel = Gtk.Label("51.53%")
       
        self.addEntryButton = Gtk.Button("Add")
        self.editEntryButton = Gtk.Button("Edit")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        self.editEntryPopover = Gtk.Popover.new(self.editEntryButton)
        
        # Widget Styling
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.monthSpentLabel.set_markup("<b>Total Spend</b>")
        self.monthRemainingLabel.set_markup("<b>Total Remaining</b>")
        self.percBudgetLabel.set_markup("<b>% of Budget</b>")
        
        self.categoryTitleLabel.set_markup("<b>Category</b>")
        self.dateTitleLabel.set_markup("<b>Date</b>")
        self.costTitleLabel.set_markup("<b>Cost</b>")
        self.descriptionTitleLabel.set_markup("<b>Description</b>")
        
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
        
        self.contentGrid.attach(self.categoryTitleLabel, self.categoryOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.dateTitleLabel, self.dateOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.costTitleLabel, self.costOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.descriptionTitleLabel, self.descriptionOffsetLeft, 7, 1, 1)
        
        for i in range (0,len(self.data.expenses)):
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.expenses, i)

            self.categoryLabel = Gtk.Label(self.data.expenses[i][0])
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.expenses[i][3])
            self.descriptionLabel = Gtk.Label(self.data.expenses[i][4])
            self.contentGrid.attach(self.categoryLabel, self.categoryOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.dateLabel, self.dateOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.costLabel, self.costOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.descriptionLabel, self.descriptionOffsetLeft, self.entryOffsetTop + i, 1, 1)
       

        self.contentGrid.attach(self.dummyLabel3, 1, self.entryOffsetTop + 10, 2, 1)
        
        self.view = Sidebar(self.data.expenseMenu, self.data.currentMonthMenu) 
        
        # Attach Content
        self.view.contentViewport.add(self.contentGrid)
