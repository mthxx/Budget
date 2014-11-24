from gi.repository import Gtk, Gio, Gdk
from calc import Calc

class Sidebar():

    def __init__(self, data):
        
        # Initialize Variables
        self.data = data
        self.calc = Calc(self.data)
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

    def display_content(self, data):
        #Clear existing data
        while len(self.contentGrid) > 0:
            self.contentGrid.remove_row(0)
            
        while len(self.entryRows) > 0:
                self.entryRows.pop(0)
        
        self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
        self.monthRemainingTotalLabel.set_text("$1,500")
        self.percBudgetTotalLabel.set_text("50.00%")
        
        self.index = 5
        for i in range (0,len(data)):
            
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.entryGrid = Gtk.Grid()
            self.entryGrid.set_column_homogeneous(True)
            self.entryGrid.set_hexpand(True)
            
            self.dateString = ""
            self.dateString = self.data.translate_date(data, i)

            # Set labels
            self.categoryLabel = Gtk.Label()
            self.dateLabel = Gtk.Label(self.dateString)
            self.descriptionLabel = Gtk.Label()
            self.editButton = Gtk.Button()

            # Style Labels
            self.costLabel = Gtk.Label("$" + str(data[i][self.data.VALUE]))
            self.categoryLabel.set_markup("<b>" + data[i][self.data.CATEGORY][self.data.CATEGORY_TEXT] + "</b>")
            self.descriptionLabel.set_markup("<i>" + data[i][self.data.DESCRIPTION] + "</i>")
            self.categoryLabel.set_property("height-request", 50)
            
            #Style Edit Button
            self.editIcon = Gio.ThemedIcon(name="go-down-symbolic")
            self.editImage = Gtk.Image.new_from_gicon(self.editIcon, Gtk.IconSize.MENU)
            self.editButton.add(self.editImage)
            self.editButton.set_relief(Gtk.ReliefStyle.NONE)
            self.editButton.set_size_request(32,32)
            
            # Attach Labels
            self.entryGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.entryGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.entryGrid.attach(self.costLabel, 2, 1, 1, 1)
           
            if self.descriptionLabel.get_text() != "":
                self.entryGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.extraSpaceLabel = Gtk.Label()
                self.entryGrid.attach(self.extraSpaceLabel,0, 4, 3, 1)
                
                self.editEmptyLabel = Gtk.Label()
                self.layoutGrid.attach(self.editEmptyLabel, 0, 1, 1, 1)
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 2)
            
            # Add Layout Grid to Content Grid. Increment index and apply whitespaces
            else:
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 1)
            self.layoutGrid.attach(self.editButton, 1, 0, 1, 1)

            self.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)
            
            self.index = self.index + 2
            self.whiteSpaceLabel = Gtk.Label()
            self.contentGrid.attach(self.whiteSpaceLabel,0, self.index, 5, 1)
            self.index = self.index + 1
            
            self.entryRows.append([[self.layoutGrid, self.whiteSpaceLabel],[self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel]]) # data[self.data.UNIQUE_ID]])
            self.contentGrid.show_all() 
        
    def menu_clicked(self, listbox, row, data, menu):
        for i in range(len(menu)):
            if menu[i][self.data.CATEGORY_INDEX] == row.get_index():
                self.menu = "<b>" +  menu[i][self.data.CATEGORY_TEXT] + "</b>"
                self.menu_index = menu[i][self.data.CATEGORY_INDEX]
        self.filter_menu(data, menu)
    
    def subMenu_clicked(self, listbox, row, data, menu):
        for i in range (len(self.data.currentMonthMenu)):
            if self.data.currentMonthMenu[i][self.data.CATEGORY_INDEX] == row.get_index():
                self.row = self.data.currentMonthMenu[i][self.data.CATEGORY_INDEX]
        self.subMenu = self.data.currentMonthMenu[self.row][self.data.CATEGORY_TEXT]
        self.subMenu_index = self.data.currentMonthMenu[self.row][self.data.CATEGORY_INDEX]
        self.filter_subMenu(data, menu)
        
    def filter_menu(self, data, menu):
        count = 0
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month =  self.month[0]

            # If selected menu item is "All"
            if self.menu_index == menu[0][self.data.CATEGORY_INDEX]:
                # If selected sub category equals "All", show row
                if self.subMenu == self.data.currentMonthMenu[self.data.CATEGORY][self.data.CATEGORY_TEXT]:
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
                    if self.subMenu_index == self.data.currentMonthMenu[0][self.data.CATEGORY_INDEX]:
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
            if self.menu_index == menu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                # If sub category equals "All"
                if self.subMenu_index == self.data.currentMonthMenu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
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
            elif self.menu_index != menu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
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
