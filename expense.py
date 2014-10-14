from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data

class Expense():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data()
        self.view = Sidebar() 
        
        self.view.topLeftLabel.set_markup("<b>Total Spent</b>")
        self.view.topMiddleLabel.set_markup("<b>Total Remaining</b>")
        self.view.topRightLabel.set_markup("<b>% of Budget</b>")

        # Build Content Area
        for i in range (0,len(self.data.expenses)):
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.expenses, i)

            self.categoryLabel = Gtk.Label(self.data.expenses[i][0])
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.expenses[i][3])
            self.descriptionLabel = Gtk.Label(self.data.expenses[i][4])
            
            self.costLabel.set_property("height-request", 35)
            
            self.view.contentGrid.attach(self.categoryLabel, self.view.categoryOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
            self.view.contentGrid.attach(self.dateLabel, self.view.dateOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
            self.view.contentGrid.attach(self.costLabel, self.view.costOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
            self.view.contentGrid.attach(self.descriptionLabel, self.view.descriptionOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
       
            self.view.entryRows.append([self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel])

        # Build Sidebars
        for i in range(0,len(self.data.expenseMenu)):
            self.button = Gtk.Button(self.data.expenseMenu[i])
            self.view.menuButtons.append(self.button)
            self.button.connect("clicked",self.view.menu_clicked)
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.button = Gtk.Button(self.data.currentMonthMenu[i])
            self.view.subMenuButtons.append(self.button)
            self.button.connect("clicked",self.view.subMenu_clicked)
        
        # Style Sidebars
        for i in range(0,len(self.data.expenseMenu)):
            self.view.menuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.view.menuButtons[i].set_property("height-request", 60)
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.view.subMenuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.view.subMenuButtons[i].set_property("height-request", 60)
        
        # Attach Buttons and Content
        for i in range(0,len(self.data.expenseMenu)):
            self.view.menuListBox.add(self.view.menuButtons[i])
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.view.subMenuListBox.add(self.view.subMenuButtons[i])
