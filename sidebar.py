from gi.repository import Gtk, Gio, Gdk
from data import Data
from calc import Calc

class Sidebar():

    def __init__(self):
        
        # Initialize Variables
        self.data = Data()
        self.calc = Calc()
        self.entryRows = []
        self.menu = ""
        self.menu_index = 0
        self.subMenu = ""
        self.subMenu_index = 0

        # Set Offsets
        self.entryOffsetTop = 8
        self.categoryOffsetLeft = 1
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5
        
        # Define Layouts
        self.grid = Gtk.Grid()
        self.headerGrid = Gtk.Grid(name="headerGrid")
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
        
        self.topLeftLabel.set_markup("<b>Total</b>")
        self.topMiddleLabel.set_markup("<b>Remaining</b>")
        self.topRightLabel.set_markup("<b>% Remaining</b>")
        
        self.monthTotalLabel = Gtk.Label()
        self.monthRemainingTotalLabel = Gtk.Label("$1,500")
        self.percBudgetTotalLabel = Gtk.Label("50.00%")

        # Set Styling
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
        
        self.headerGrid.attach(self.monthTotalLabel, 1, 1, 1, 1)
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
            self.costLabel = Gtk.Label("$" + data[i][self.data.value])
            self.categoryLabel.set_markup("<b>" + data[i][self.data.category][self.data.category_text] + "</b>")
            self.descriptionLabel.set_markup("<i>" + data[i][self.data.description] + "</i>")
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
        
    def add_entry(self, button):
        if self.addEntryPopover.get_visible():
            self.addEntryPopover.hide()
        else:
            self.addEntryPopover.show_all()

    def generate_add_popover(self, data):
        # Add Items to Add Popover
        self.addGrid = Gtk.Grid()
        self.addCategoryComboBoxText = Gtk.ComboBoxText()
        self.addEntryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.addEntryLabel = Gtk.Label("Entry")
        self.addDescriptionLabel = Gtk.Label("Description")
        self.addCurrencyLabel = Gtk.Label("$ ")
        self.addEntry = Gtk.Entry()
        self.addDescription = Gtk.Entry()
        self.addDate = Gtk.Calendar()
        self.addSubmitButton = Gtk.Button("Submit")
        
        self.addEntryBox.add(self.addCurrencyLabel)
        self.addEntryBox.add(self.addEntry)
        
        # Style Add Popover Items
        self.add_popover_margin(self.addCategoryComboBoxText, 10)
        self.add_popover_margin(self.addEntryBox, 10)
        self.add_popover_margin(self.addDescription, 10)
        self.addEntryBox.set_margin_top(0)
        self.addEntryBox.set_margin_end(4)
        self.addDescription.set_margin_top(0)
        self.addDescription.set_margin_start(4)
        self.add_popover_margin(self.addDate, 10)
        self.add_popover_margin(self.addSubmitButton, 10)

        self.addCategoryComboBoxText.set_property("height-request", 34)

        for i in range(1,len(data)):
            self.addCategoryComboBoxText.append_text(data[i][1])
        
        # Add Widgets to Grid
        self.addGrid.attach(self.addCategoryComboBoxText,0,0,2,1)
        self.addGrid.attach(self.addEntryLabel,0,1,1,1)
        self.addGrid.attach(self.addDescriptionLabel,1,1,1,1)
        self.addGrid.attach(self.addEntryBox,0,2,1,1)
        self.addGrid.attach(self.addDescription,1,2,1,1)
        self.addGrid.attach(self.addDate,0,3,2,1)
        self.addGrid.attach(self.addSubmitButton,0,4,2,1)
    
        self.addEntryPopover.add(self.addGrid)
   
    def add_popover_margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_end(margin)
        widget.set_margin_bottom(margin)
    
    def menu_clicked(self, listbox, row, data, menu):
        for i in range(len(menu)):
            if menu[i][self.data.category_index] == row.get_index():
                self.menu = "<b>" +  menu[i][self.data.category_text] + "</b>"
                self.menu_index = menu[i][self.data.category_index]
        self.filter_menu(data, menu)
    
    def subMenu_clicked(self, listbox, row, data, menu):
        for i in range (len(self.data.currentMonthMenu)):
            if self.data.currentMonthMenu[i][self.data.category_index] == row.get_index():
                self.row = self.data.currentMonthMenu[i][self.data.category_index]
        self.subMenu = self.data.currentMonthMenu[self.row][self.data.category_text]
        self.subMenu_index = self.data.currentMonthMenu[self.row][self.data.category_index]
        self.filter_subMenu(data, menu)
        
    def filter_menu(self, data, menu):
        count = 0
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month =  self.month[0]

            # If selected menu item is "All"
            if self.menu_index == menu[0][self.data.category_index]:
                # If selected sub category equals "All", show row
                if self.subMenu == self.data.currentMonthMenu[self.data.category][self.data.category_text]:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
                # If selected sub category equals rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data, self.subMenu_index)))
                # If selected sub category does not equal rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()

            # If selected menu item is not "All"
            elif self.menu_index != menu[0][1]:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][1][0].get_label():
                    # If selected sub menu is "All", show row.
                    if self.subMenu_index == self.data.currentMonthMenu[0][self.data.category_index]:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data, self.menu_index, self.subMenu_index)))
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][1][0].get_label():
                        self.entryRows[i][0][0].hide()
                        self.entryRows[i][0][1].hide()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][1][0].get_label():
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))

    def filter_subMenu(self, data, menu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month = self.month[0]
           # If selected category is equal to "All"
            if self.menu_index == menu[self.data.category][self.data.category_index]:
                # If sub category equals "All"
                if self.subMenu_index == self.data.currentMonthMenu[self.data.category][self.data.category_index]:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
                # If selected sub category matches rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))
                # If selected sub category does not match rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))

            # If selected category is not equal to "All"
            elif self.menu_index != menu[self.data.category][self.data.category_index]:
                # If selected sub category equals "All" and selected category equals rows category, show row
                if self.month == self.subMenu and self.entryRows[i][1][0].get_label() == self.menu:
                    self.entryRows[i][0][0].show()
                    self.entryRows[i][0][1].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data,self.menu_index, self.subMenu_index)))
                # If selected sub category does not equal rows sub category, or selected category doesn't equal rows category, hide row.
                elif self.month != self.subMenu or self.entryRows[i][1][0].get_label() != self.menu:
                    self.entryRows[i][0][0].hide()
                    self.entryRows[i][0][1].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data,self.menu_index, self.subMenu_index)))
                # If selected sub category equals "All"
                if self.subMenu_index == self.data.currentMonthMenu[0][0]:
                    # If selected category equals rows category, show row
                    if self.entryRows[i][1][0].get_label() == self.menu:
                        self.entryRows[i][0][0].show()
                        self.entryRows[i][0][1].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data,self.menu_index)))
