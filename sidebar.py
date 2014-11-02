from gi.repository import Gtk, Gio, Gdk
from data import Data

class Sidebar():

    def __init__(self):
        
        self.data = Data()
        # Initialize Variables
        self.entryRows = []
        self.menu = ""
        self.subMenu = ""
        
        # Set Offsets
        self.entryOffsetTop = 8
        self.categoryOffsetLeft = 1
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5
        
        # Define Layouts
        self.grid = Gtk.Grid()
        self.headerGrid = Gtk.Grid( name = "headerGrid")
        self.contentGrid = Gtk.Grid()
       
        self.menuListBox = Gtk.ListBox(name="menuListBox")
        self.subMenuListBox = Gtk.ListBox(name="subMenuListBox")
        
        self.menuScrolledWindow = Gtk.ScrolledWindow(name="menuScrolledWindow")
        self.subMenuScrolledWindow = Gtk.ScrolledWindow(name="subMenuScrolledWindow")
        self.contentScrolledWindow = Gtk.ScrolledWindow(name="entryScrolledWindow")
        
        self.menuViewport = Gtk.Viewport(name="menuViewport")
        self.subMenuViewport = Gtk.Viewport(name="subMenuViewport")
        self.contentViewport = Gtk.Viewport()

        # Define Widgets
        self.whiteSpaceLabel1 = Gtk.Label()
        self.whiteSpaceLabel2 = Gtk.Label()
        
        self.addEntryButton = Gtk.Button("Add")
        self.editEntryButton = Gtk.Button("Edit")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        self.editEntryPopover = Gtk.Popover.new(self.addEntryButton)
        
        self.topLeftLabel = Gtk.Label()
        self.topMiddleLabel = Gtk.Label()
        self.topRightLabel = Gtk.Label()
        
        self.monthSpentTotalLabel = Gtk.Label("$1,500")
        self.monthRemainingTotalLabel = Gtk.Label("$1,500")
        self.percBudgetTotalLabel = Gtk.Label("50.00%")

        # Set Styling
#        self.grid.override_backgrounddcolor(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.2, 0.2, 0.2, 0.2))
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",150)

        self.subMenuScrolledWindow.set_vexpand(True)
        self.subMenuScrolledWindow.set_property("width-request",100)
        
        self.headerGrid.set_column_homogeneous(True)
        self.headerGrid.set_hexpand(True)
        
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        
        # Add items to Main Grid 
        self.menuViewport.add(self.menuListBox)
        self.subMenuViewport.add(self.subMenuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.subMenuScrolledWindow.add(self.subMenuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,2)
        self.grid.attach(self.subMenuScrolledWindow,1,0,1,2)
        self.grid.attach(self.headerGrid,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,2,1,1,1)

        # Build Content Area - Add items to Content Grid
        self.headerGrid.attach(self.topLeftLabel, 1, 0, 1, 1)
        self.headerGrid.attach(self.topMiddleLabel, 2, 0, 1, 1)
        self.headerGrid.attach(self.topRightLabel, 3, 0, 1, 1)
        
        self.headerGrid.attach(self.monthSpentTotalLabel, 1, 1, 1, 1)
        self.headerGrid.attach(self.monthRemainingTotalLabel, 2, 1, 1, 1)
        self.headerGrid.attach(self.percBudgetTotalLabel, 3, 1, 1, 1)
        
        self.headerGrid.attach(self.whiteSpaceLabel1, 0, 2, 5, 1)
        self.headerGrid.attach(self.addEntryButton, 1, 3, 1, 1)
        self.headerGrid.attach(self.editEntryButton, 3, 3, 1, 1)
        self.headerGrid.attach(self.whiteSpaceLabel2, 1, 4, 1, 1)
        
        self.contentViewport.add(self.contentGrid)

    def generate_sidebars(self, data):
        self.menu = "<b>" +  data[0][1] + "</b>"
        self.subMenu = self.data.currentMonthMenu[0][1]
        for i in range(0,len(data)):
            self.label = Gtk.Label(data[i][1])
            self.label.set_property("height-request", 60)
            self.menuListBox.add(self.label)
            self.menuListBox.select_row(self.menuListBox.get_row_at_index(0))
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.label = Gtk.Label(self.data.currentMonthMenu[i][1])
            self.label.set_property("height-request", 60)
            self.subMenuListBox.add(self.label)
            self.subMenuListBox.select_row(self.subMenuListBox.get_row_at_index(0))

    def generate_content(self, data):
        self.index = 5
        
        for i in range (0,len(data)):
            
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.layoutGrid.set_column_homogeneous(True)
            self.layoutGrid.set_hexpand(True)
            
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,data, i)

            # Set labels
            self.categoryLabel = Gtk.Label()
            self.dateLabel = Gtk.Label(self.dateString)
            self.descriptionLabel = Gtk.Label()
          
            # Style Labels
            self.costLabel = Gtk.Label("$" + data[i][2])
            self.categoryLabel.set_markup("<b>" + data[i][0][1] + "</b>")
            self.descriptionLabel.set_markup("<i>" + data[i][3] + "</i>")
            self.categoryLabel.set_property("height-request", 50)
            
            # Attach Labels
            self.layoutGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.layoutGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.layoutGrid.attach(self.costLabel, 2, 1, 1, 1)
            
            if self.descriptionLabel.get_text() != "":
                self.layoutGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.extraSpaceLabel = Gtk.Label()
                self.layoutGrid.attach(self.extraSpaceLabel,0, 4, 3, 1)
            
            # Add Layout Grid to Content Grid. Increment index and apply whitespaces
            self.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)
            
            self.index = self.index + 2
            self.whiteSpaceLabel = Gtk.Label()
            self.contentGrid.attach(self.whiteSpaceLabel,0, self.index, 5, 1)
            self.index = self.index + 1
            
            self.entryRows.append([[self.layoutGrid, self.whiteSpaceLabel],[self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel]])

    def menu_clicked(self, listbox, row, data, menu):
        for i in range (len(menu)):
            if menu[i][0] == row.get_index():
                self.menu = "<b>" +  menu[i][1] + "</b>"
        self.filter_menu(data, menu)
    
    def subMenu_clicked(self, listbox, row, data, menu):
        for i in range (len(self.data.currentMonthMenu)):
            if self.data.currentMonthMenu[i][0] == row.get_index():
                self.subMenu = self.data.currentMonthMenu[i][1]
        self.filter_subMenu(data, menu)

    def filter_menu(self, data, menu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month =  self.month[0]

            # If selected menu item is "All"
            if self.menu == "<b>" + menu[0][1] + "</b>":
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                elif self.month == self.subMenu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                elif self.month != self.subMenu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()

            # If selected menu item is not "All"
            elif self.menu != "<b>" + menu[0][1] + "</b>":
                # If category matches menu item selected
                if self.entryRows[i][1][0].get_label() == self.menu:
                    if self.subMenu == self.data.currentMonthMenu[0][1]:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
                    if self.subMenu == self.month:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
                    if self.entryRows[i][1][0].get_label() != self.menu:
                        self.entryRows[i][0][0].hide()
                        self.entryRows[i][0][1].hide()
                elif self.entryRows[i][1][0].get_label() != self.menu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()

    def filter_subMenu(self, data, menu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month = self.month[0]
            # If selected month is equal to "All"
            if self.menu == "<b>" + menu[0][1] + "</b>":
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                elif self.month == self.subMenu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                elif self.month != self.subMenu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()

            # If selected category is not equal to "All"
            elif self.menu != "<b>" + menu[0][1] + "</b>":
                if self.month == self.subMenu and self.entryRows[i][1][0].get_label() == self.menu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                elif self.month != self.subMenu or self.entryRows[i][1][0].get_label() != self.menu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    if self.entryRows[i][1][0].get_label() == self.menu:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
