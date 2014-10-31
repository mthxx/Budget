from gi.repository import Gtk, Gio, Gdk
from data import Data

class Sidebar():

    def __init__(self):
        
        self.data = Data()
        # Initialize Variables
        self.entryRows = []
        self.menu = self.data.incomeMenu[0][1]
        self.subMenu = self.data.currentMonthMenu[0][1]
        
        # Set Offsets
        self.entryOffsetTop = 8
        self.categoryOffsetLeft = 1
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5
        
        # Define Layouts
        self.grid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
       
        self.menuListBox = Gtk.ListBox()
        self.subMenuListBox = Gtk.ListBox()
        
        self.menuScrolledWindow = Gtk.ScrolledWindow()
        self.subMenuScrolledWindow = Gtk.ScrolledWindow()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        
        self.menuViewport = Gtk.Viewport()
        self.subMenuViewport = Gtk.Viewport()
        self.contentViewport = Gtk.Viewport()

        # Define Widgets
        self.dummyLabel1 = Gtk.Label()
        self.dummyLabel2 = Gtk.Label()
        
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
        
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        # Add items to Main Grid 
        self.menuViewport.add(self.menuListBox)
        self.subMenuViewport.add(self.subMenuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.subMenuScrolledWindow.add(self.subMenuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,1)
        self.grid.attach(self.subMenuScrolledWindow,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)

        # Build Content Area - Add items to Content Grid
        self.contentGrid.attach(self.topLeftLabel, 1, 2, 1, 1)
        self.contentGrid.attach(self.topMiddleLabel, 2, 2, 1, 1)
        self.contentGrid.attach(self.topRightLabel, 3, 2, 1, 1)
        
        self.contentGrid.attach(self.monthSpentTotalLabel, 1, 3, 1, 1)
        self.contentGrid.attach(self.monthRemainingTotalLabel, 2, 3, 1, 1)
        self.contentGrid.attach(self.percBudgetTotalLabel, 3, 3, 1, 1)
        
        self.contentGrid.attach(self.dummyLabel1, 0, 4, 3, 1)
        self.contentGrid.attach(self.addEntryButton, 1, 5, 1, 1)
        self.contentGrid.attach(self.editEntryButton, 3, 5, 1, 1)
        self.contentGrid.attach(self.dummyLabel2, 1, 6, 1, 1)
        
        self.contentViewport.add(self.contentGrid)

    def generate_sidebars(self, data):
        for i in range(0,len(data)):
            self.label = Gtk.Label(data[i][1])
            self.label.set_property("height-request", 60)
            self.menuListBox.add(self.label)
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.label = Gtk.Label(self.data.currentMonthMenu[i][1])
            self.label.set_property("height-request", 60)
            self.subMenuListBox.add(self.label)

    def generate_content(self, data):
        self.index = 3
        for i in range (0,len(data)):
            
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.layoutGrid.set_column_homogeneous(True)
            self.layoutGrid.set_hexpand(True)
            
            self.whiteSpaceLabel = Gtk.Label()
            self.index = self.index + 2
            self.contentGrid.attach(self.whiteSpaceLabel,0, self.index, 5, 1)
            self.index = self.index + 3
            
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,data, i)

            self.categoryLabel = Gtk.Label()
            self.categoryLabel.set_markup("<b>" + data[i][0][1] + "</b>")
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + data[i][2])
            self.descriptionLabel = Gtk.Label(data[i][3])
            #self.whiteSpaceLabel = Gtk.Label()
            
            self.costLabel.set_property("height-request", 35)
            
            #self.layoutGrid.attach(self.whiteSpaceLabel,0, 1, 3, 1)
            self.layoutGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.layoutGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.layoutGrid.attach(self.costLabel, 2, 1, 1, 1)
            
            if self.descriptionLabel.get_text() != "":
                self.layoutGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.whiteSpaceLabel = Gtk.Label()
                self.layoutGrid.attach(self.whiteSpaceLabel,0, 4, 3, 1)

            self.layoutGrid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
            self.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)
            self.entryRows.append([self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel])

    def menu_clicked(self, listbox, row, data, dataMenu):
        for i in range (len(dataMenu)):
            if dataMenu[i][0] == row.get_index():
                self.menu = dataMenu[i][1]
        self.filter_menu(data, dataMenu)
    
    def subMenu_clicked(self, listbox, row, data, dataMenu):
        for i in range (len(self.data.currentMonthMenu)):
            if self.data.currentMonthMenu[i][0] == row.get_index():
                self.subMenu = self.data.currentMonthMenu[i][1]
        self.filter_subMenu(data, dataMenu)

    def filter_menu(self, data, dataMenu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1].get_label().split()
            self.month =  self.month[0]
            if self.menu == dataMenu[0][1]:
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    #self.categoryTitleLabel.show()
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month == self.subMenu:
                    #self.categoryTitleLabel.show()
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month != self.subMenu:
                    #self.categoryTitleLabel.show()
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != dataMenu[0][1]:
                if self.entryRows[i][0].get_label() == self.menu:
                    if self.subMenu == self.data.currentMonthMenu[0][1]:
                        #self.categoryTitleLabel.hide()
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.subMenu == self.month:
                        self.categoryTitleLabel.hide()
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.entryRows[i][0].get_label() != self.menu:
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].hide()
                        self.entryRows[i][2].hide()
                        self.entryRows[i][3].hide()
                elif self.entryRows[i][0].get_label() != self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()

    def filter_subMenu(self, data, dataMenu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1].get_label().split()
            self.month = self.month[0]
            if self.menu == dataMenu[0][1]:
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month == self.subMenu:
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month != self.subMenu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != dataMenu[0][1]:
                if self.month == self.subMenu and self.entryRows[i][0].get_label() == self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month != self.subMenu or self.entryRows[i][0].get_label() != self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
                if self.subMenu == self.data.currentMonthMenu[0][1]:
                    if self.entryRows[i][0].get_label() == self.menu:
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
