from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data() 
        self.view = Sidebar() 
        
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
        
        self.monthSpentTotalLabel = Gtk.Label("$1,500")
        self.monthRemainingTotalLabel = Gtk.Label("$1,500")
        self.percBudgetTotalLabel = Gtk.Label("50.00%")
       
        self.addEntryButton = Gtk.Button("Add")
        self.editEntryButton = Gtk.Button("Edit")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        self.editEntryPopover = Gtk.Popover.new(self.addEntryButton)
        
        self.menuButtons = []
        self.subMenuButtons = []
        
        self.entryRows = []

        self.menu = "All"
        self.subMenu = "All"

        # Widget Styling
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.monthSpentLabel.set_markup("<b>All Income</b>")
        self.monthRemainingLabel.set_markup("<b>All Remaining</b>")
        self.percBudgetLabel.set_markup("<b>% Remaining</b>")
        
        self.categoryTitleLabel.set_markup("<b>Category</b>")
        self.dateTitleLabel.set_markup("<b>Date</b>")
        self.costTitleLabel.set_markup("<b>Cost</b>")
        self.descriptionTitleLabel.set_markup("<b>Description</b>")
        
        # Build Sidebars
        self.data.incomeMenu, self.data.currentMonthMenu
        for i in range(0,len(self.data.incomeMenu)):
            self.button = Gtk.Button(self.data.incomeMenu[i])
            self.menuButtons.append(self.button)
            self.button.connect("clicked",self.menu_clicked)

        for i in range(0,len(self.data.currentMonthMenu)):
            self.button = Gtk.Button(self.data.currentMonthMenu[i])
            self.subMenuButtons.append(self.button)
            self.button.connect("clicked",self.subMenu_clicked)
        
        # Style Sidebars
        for i in range(0,len(self.data.incomeMenu)):
            self.menuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.menuButtons[i].set_property("height-request", 60)
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.subMenuButtons[i].set_relief(Gtk.ReliefStyle.NONE)
            self.subMenuButtons[i].set_property("height-request", 60)
            
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
        
        for i in range (0,len(self.data.income)):
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.income, i)

            self.categoryLabel = Gtk.Label(self.data.income[i][0])
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.income[i][3])
            self.descriptionLabel = Gtk.Label(self.data.income[i][4])
            self.contentGrid.attach(self.categoryLabel, self.categoryOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.dateLabel, self.dateOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.costLabel, self.costOffsetLeft, self.entryOffsetTop + i, 1, 1)
            self.contentGrid.attach(self.descriptionLabel, self.descriptionOffsetLeft, self.entryOffsetTop + i, 1, 1)
            
            self.entryRows.append([self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel])

        
        self.contentGrid.attach(self.dummyLabel3, 1, len(self.data.income) + 10, 2, 1)
        
        
        # Attach Buttons and Content
        for i in range(0,len(self.data.incomeMenu)):
            self.view.menuListBox.add(self.menuButtons[i])
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.view.subMenuListBox.add(self.subMenuButtons[i])
            
        self.view.contentViewport.add(self.contentGrid)

    def menu_clicked(self,button):
        self.menu = button.get_label()
        self.filter_menu(button.get_label())
    
    def subMenu_clicked(self,button):
        self.subMenu = button.get_label()
        self.filter_subMenu(button.get_label())
    
    def filter_menu(self,menu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1].get_label().split()
            if self.menu == "All":
                if self.subMenu == "All":
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] == self.subMenu:
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != "All":
                if self.entryRows[i][0].get_label() == self.menu:
                    if self.subMenu == "All":
                        self.entryRows[i][0].show()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.subMenu == self.month[0]:
                        self.entryRows[i][0].show()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.entryRows[i][0].get_label() != menu:
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].hide()
                        self.entryRows[i][2].hide()
                        self.entryRows[i][3].hide()
                elif self.entryRows[i][0].get_label() != self.menu:    
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            
    def filter_subMenu(self,subMenu):
        for i in range (0,len(self.data.income)):
            self.month = self.entryRows[i][1].get_label().split()
            if self.menu == "All":
                if self.subMenu == "All":
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] == self.subMenu:    
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != "All":
                if self.month[0] == self.subMenu and self.entryRows[i][0].get_label() == self.menu:
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu or self.entryRows[i][0].get_label() != self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
                if subMenu == "All":
                    if self.entryRows[i][0].get_label() == self.menu:
                        self.entryRows[i][0].show()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
