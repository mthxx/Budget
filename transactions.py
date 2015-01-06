from gi.repository import Gtk, Gio, Gdk
from calc import Calc
from edit_popover import Edit_Popover
from add_category_popover import Add_Category_Popover

class Transactions():

    def __init__(self, data):
        
        # Content Grid
        self.LAYOUT_GRID_INDEX = 0           # Element

        # Layout Widget Indexes
        self.LAYOUT_WIDGET_INDEX = 1         # Array
        self.CATEGORY_LABEL_INDEX = 0        # Element
        self.DATE_LABEL_INDEX = 1            # Element
        self.CURRENCY_LABEL_INDEX = 2        # Element
        self.COST_LABEL_INDEX = 3            # Element
        self.DESCRIPTION_LABEL_INDEX = 4     # Element
        self.EDIT_BUTTON_INDEX = 5
        
        # Menu List Box Indexes
        self.EDIT_CATEGORY_TITLE = 0
        self.EDIT_CATEGORY_ENTRY = 1
        self.EDIT_CATEGORY_BALANCE = 2
        self.EDIT_CATEGORY_BUTTON = 3
        
        # Additional Items
        self.ENTRY_GRID_INDEX = 2            # Element
        self.COST_GRID_INDEX = 3             # Element
        self.UNIQUE_ID_INDEX = 4             # Element
        
        # Initialize Variables
        self.data = data
        self.calc = Calc(self.data)
        self.entryRows = []
        
        self.incomeCount = 0
        self.expenseCount = 0
        self.incomeAllIndex = 0
        self.expenseAllIndex = 0
        self.menu = ""
        self.menu_index = 0
        self.subMenu = ""
        self.subMenu_index = 0
                
        self.incomeMenu = []
        self.expenseMenu = []
        self.dataSum = 0
        
        self.editMode = 0

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
      
        self.menuListBox = Gtk.ListBox(name="menuListBox")
        
        self.menuScrolledWindow = Gtk.ScrolledWindow(name="menuScrolledWindow")
        self.contentScrolledWindow = Gtk.ScrolledWindow(name="entryScrolledWindow")
        
        self.menuViewport = Gtk.Viewport(name="menuViewport")
        self.contentViewport = Gtk.Viewport()

        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",279)
        self.menuScrolledWindow.set_property("hscrollbar-policy", Gtk.PolicyType.NEVER)

        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        self.contentGrid.set_margin_left(20)
        self.contentGrid.set_margin_right(20)
       
        # Create edit and add category buttons
        self.editCategoryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        
        # Connect Widgets
        self.menuListBox.connect("row-selected",self.menu_clicked)
        
        # Generate Sidebar and Content
        self.generate_sidebars()
        self.create_date_grid()
        self.display_content()
        
        # Build and Add items to Main Grid
        self.menuViewport.add(self.menuListBox)
        self.menuScrolledWindow.add(self.menuViewport)
        
        self.contentScrolledWindow.add(self.contentViewport)
        self.contentViewport.add(self.contentGrid)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,2)
        self.grid.attach(self.dateGrid,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,2,1,1,1)
        

    def category_edit_mode(self, index):
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_TITLE].hide()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BALANCE].hide()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].show()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BUTTON].show()
    
    def category_view_mode(self, index):
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_TITLE].show()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BALANCE].show()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].hide()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BUTTON].hide()

    def create_date_grid(self):
        # Date Grid
        self.dateGrid = Gtk.Grid(name="headerGrid")
        self.dateLabelMonth = Gtk.Label("Month:")
        self.dateLabelYear = Gtk.Label("Year:")
        self.dateLabelRange = Gtk.Label("Range:")
        
        self.dateComboMonth = Gtk.ComboBoxText()
        self.dateComboYear = Gtk.ComboBoxText()
        
        self.dateButtonFrom = Gtk.Button()
        self.dateCalendarFrom = Gtk.Calendar()
       
        self.dateLabelTo = Gtk.Label("to")
       
        self.dateButtonTo = Gtk.Button()
        self.dateCalendarTo = Gtk.Calendar()
        
        self.dateGrid.attach(self.dateLabelMonth,0,0,1,1)
        self.dateGrid.attach(self.dateComboMonth,1,0,1,1)
        self.dateGrid.attach(self.dateLabelYear,2,0,1,1)
        self.dateGrid.attach(self.dateComboYear,3,0,1,1)
        self.dateGrid.attach(self.dateLabelRange,4,0,1,1)
        self.dateGrid.attach(self.dateButtonFrom,5,0,1,1) 
        self.dateGrid.attach(self.dateLabelTo,6,0,1,1) 
        self.dateGrid.attach(self.dateButtonTo,7,0,1,1) 
        
        # Generate Months
        for i in range(0,len(self.data.allMonthMenu)):
            self.dateComboMonth.append_text(self.data.allMonthMenu[i][1])
            
        self.dateButtonFrom.set_label("1/1/2013")
        self.dateButtonTo.set_label("1/1/2016")
        
        # Connect to handler    
        self.dateComboMonth.connect("changed",self.subMenu_clicked)
        
        self.dateComboYear.append_text("All")
        self.dateComboYear.append_text("2015")
        self.dateComboYear.append_text("2014")
        self.dateComboYear.append_text("2013")
            
        self.dateComboMonth.set_active(0)
        self.dateComboYear.set_active(0)
        
        self.dateLabelMonth.set_margin_start(20)
        self.dateLabelMonth.set_margin_end(5)
        
        self.dateComboMonth.set_margin_top(10)
        self.dateComboMonth.set_margin_bottom(10)
        self.dateComboMonth.set_margin_end(10)
        
        self.dateLabelYear.set_margin_start(5)
        self.dateLabelYear.set_margin_end(5)
        
        self.dateComboYear.set_margin_top(10) 
        self.dateComboYear.set_margin_bottom(10)
        self.dateComboYear.set_margin_end(100)
        
        self.dateLabelRange.set_margin_end(5)
        
        self.dateButtonFrom.set_margin_top(10)
        self.dateButtonFrom.set_margin_bottom(10)
        self.dateButtonFrom.set_margin_end(5)
        
        self.dateLabelTo.set_margin_end(5)
        
        self.dateButtonTo.set_margin_top(10)
        self.dateButtonTo.set_margin_bottom(10)

    def create_delete_button(self, label):
        self.button = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="window-close-symbolic")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.MENU)
        self.button.add(self.image)
        self.button.show_all()
        
        self.editPopover = Gtk.Popover.new(self.button)
        
        self.editGrid = Gtk.Grid()
        
        self.confirmLabelLine1 = Gtk.Label("Are you sure?")
        self.confirmLabelLine2 = Gtk.Label()
        self.deleteCancelButton = Gtk.Button("Cancel")
        self.deleteConfirmButton = Gtk.Button("Confirm")
        self.deleteSelectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Style Widgets
        self.deleteCancelButton.set_size_request(100,32)
        self.deleteConfirmButton.set_size_request(100,32)
        self.confirmLabelLine2.set_markup("<span foreground=\"red\"><b>This cannot be undone!</b></span>")
        Gtk.StyleContext.add_class(self.deleteSelectorBox.get_style_context(), "linked")
        self.confirmLabelLine1.set_margin_top(10)
        self.deleteSelectorBox.set_margin_start(10)
        self.deleteSelectorBox.set_margin_top(10)
        self.deleteSelectorBox.set_margin_bottom(10)
        self.deleteSelectorBox.set_margin_end(5)

        # Connect Widget Handlers
        self.button.connect("clicked", self.on_deleteButton_clicked, self.editPopover)
        self.deleteCancelButton.connect("clicked", self.on_deleteButton_clicked, self.editPopover)
        self.deleteConfirmButton.connect("clicked", self.delete_category_confirm, label)

        self.deleteSelectorBox.add(self.deleteCancelButton)
        self.deleteSelectorBox.add(self.deleteConfirmButton)
        
        self.editGrid.attach(self.confirmLabelLine1, 0, 0, 2, 1)
        self.editGrid.attach(self.confirmLabelLine2, 0, 1, 2, 1)
        self.editGrid.attach(self.deleteSelectorBox, 0, 2, 2, 1)
        
        self.editPopover.add(self.editGrid)

        return self.button
    
    def delete_category_confirm(self, button, label):
        for i in range(len(self.menuListBox)):
            if self.menuListBox.get_row_at_index(i) == None:
                return
            elif self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_text() == label:
                for j in range(0, len(self.data.transactionsMenu)):
                    # Find matching menu item and uniqueID in database
                    if self.data.transactionsMenu[j][1] == self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_label():
                        self.data.delete_category(self.data.transactionsMenu[j][0])
                        # If row is found, break out of loop.
                        return
    
    def display_content(self):
        #Clear existing data
        while len(self.contentGrid) > 0:
            self.contentGrid.remove_row(0)
            
        while len(self.entryRows) > 0:
                self.entryRows.pop(0)
        
        self.whiteSpaceLabel = Gtk.Label()
        
        self.index = 5
        for i in range (0,len(self.data.transactions)):
            
            # Date String
            self.dateString = ""
            self.dateString = self.data.translate_date(self.data.transactions, i)
            
            # Create Widgets
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.entryGrid = Gtk.Grid()
            self.costGrid = Gtk.Grid()
            
            self.categoryLabel = Gtk.Label()
            self.dateLabel = Gtk.Label(self.dateString)
            self.descriptionLabel = Gtk.Label()
            
            self.currencyLabel = Gtk.Label("$")
            self.costLabel = Gtk.Label()
            
            for j in range(0, len(self.data.transactionsMenu)):
                if int(self.data.transactions[i][0][0]) == int(self.data.transactionsMenu[j][0]) and self.data.transactionsMenu[j][2] == "income":
                    self.costLabel.set_markup("<span foreground=\"green\">" + str(self.data.transactions[i][self.data.VALUE]) + "</span>")
           
            for j in range(0, len(self.data.transactionsMenu)):
                if int(self.data.transactions[i][0][0]) == int(self.data.transactionsMenu[j][0]) and self.data.transactionsMenu[j][2] == "expense":
                    self.costLabel.set_markup("<span foreground=\"red\">" + str(self.data.transactions[i][self.data.VALUE]) + "</span>")

            # Create Edit Popover
            self.editButton = Gtk.Button()
            self.editPopover = Gtk.Popover.new(self.editButton)
            self.edit_popover = Edit_Popover(self.data)
            self.editPopover.add(self.edit_popover.editGrid)
            self.editButton.connect("clicked", self.edit_popover.on_editDropdown_clicked, self.editPopover, self.data.transactions[i][self.data.UNIQUE_ID], self.entryRows, self.data.transactionsMenu, self.contentGrid)

            # Style Widgets
            self.entryGrid.set_halign(Gtk.Align.CENTER)
            self.entryGrid.set_hexpand(True)
            
            self.categoryLabel.set_markup(self.data.transactions[i][self.data.CATEGORY][self.data.CATEGORY_TEXT])
            self.categoryLabel.set_property("height-request", 50)
            self.categoryLabel.set_property("xalign", 1)
            self.categoryLabel.set_width_chars(15)
            
            self.dateLabel.set_margin_start(30)
            self.dateLabel.set_margin_end(30)
            self.dateLabel.set_width_chars(15)
            
            self.costGrid.set_row_homogeneous(True)
            self.costLabel.set_property("xalign", .05)
            self.costLabel.set_width_chars(14)

            self.descriptionLabel.set_markup("<i>" + self.data.transactions[i][self.data.DESCRIPTION] + "</i>")
            
            # Style Edit Button
            self.editIcon = Gio.ThemedIcon(name="go-down-symbolic")
            self.editImage = Gtk.Image.new_from_gicon(self.editIcon, Gtk.IconSize.MENU)
            self.editButton.add(self.editImage)
            self.editButton.set_relief(Gtk.ReliefStyle.NONE)
            self.editButton.set_valign(Gtk.Align.START)
            self.editButton.set_opacity(.5)

            # Attach Labels
            self.costGrid.attach(self.currencyLabel, 0,1,1,1)
            self.costGrid.attach(self.costLabel, 1,1,1,1)
            self.entryGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.entryGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.entryGrid.attach(self.costGrid, 2, 0, 1, 2)
           
            if self.descriptionLabel.get_text() != "":
                self.entryGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.extraSpaceLabel = Gtk.Label()
                self.entryGrid.attach(self.extraSpaceLabel,0, 4, 1, 1)
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 5)
            
            # Add Layout Grid to Content Grid. Increment index and apply whitespaces
            else:
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 2)
            
            self.layoutGrid.attach(self.editButton, 1, 0, 1, 1)
            self.layoutGrid.set_margin_bottom(25)


            self.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)

            self.index = self.index + 2

            self.transactionType = ""
            for j in range(0, len(self.data.transactionsMenu)):
                if self.data.transactionsMenu[j][0] == self.data.transactions[i][self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                    self.transactionType = self.data.transactionsMenu[j][2]
            
            self.entryRows.append([self.layoutGrid, [self.categoryLabel, self.dateLabel, self.currencyLabel, self.costLabel, self.descriptionLabel, self.editButton], self.entryGrid, self.costGrid, self.data.transactions[i][self.data.UNIQUE_ID], self.transactionType])
            self.contentGrid.show_all() 
        
    def editable_category(self, i):
        if i != 0:
            if self.menuListBox.get_row_at_index(i).get_child() != self.editCategoryBox:
                if (self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_TITLE] != self.transactionsLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_TITLE] != self.incomeLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_TITLE] != self.expenseLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_TITLE].get_label() != "Uncategorized"
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[2].get_label() != "Month"):
                    return True
                else:
                    return False
            else: 
                return False
    
    def filter_menu(self, data, menu):
        count = 0
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1][1].get_label().split()
            self.month =  self.month[0]

            # If selected menu item is "All"
            if self.menu_index == -1:
                # If selected sub category equals "All", show row
                if self.subMenu == self.data.allMonthMenu[self.data.CATEGORY][self.data.CATEGORY_TEXT]:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                # If selected sub category equals rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                # If selected sub category does not equal rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            
            # If selected menu item is "Income" or "Expenses"
            elif self.menu_index == -2 or self.menu_index == -3:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][5]:
                    # If selected sub menu is "All", show row.
                    if self.subMenu_index == self.data.allMonthMenu[0][self.data.CATEGORY_INDEX]:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                        #self.entryRows[i][0][1].hide()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            
            # If selected menu item is "Uncategorized" Income
            elif self.menu_index == -4 or self.menu_index == -5:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][5] and self.entryRows[i][1][0].get_label() == "Uncategorized":
                    # If selected sub menu is "All", show row.
                    if self.subMenu_index == self.data.allMonthMenu[0][self.data.CATEGORY_INDEX]:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                        #self.entryRows[i][0][1].hide()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            
            # If selected menu item is not "All"
            elif self.menu_index != -1:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    # If selected sub menu is "All", show row.
                    if self.subMenu_index == self.data.allMonthMenu[0][self.data.CATEGORY_INDEX]:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()

    def filter_subMenu(self, data, menu):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DATE_LABEL_INDEX].get_label().split()
            self.month = self.month[0]
           # If selected category is equal to "All"
            if self.menu_index == -1 :
                # If sub category equals "All"
                if self.subMenu_index == self.data.allMonthMenu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                # If selected sub category matches rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                # If selected sub category does not match rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            
           # If selected category is equal to "Income or Expenses"
            elif self.menu_index == -2 or self.menu_index == -3 :
                # If sub category equals "All"
                if self.subMenu_index == self.data.allMonthMenu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                    if self.entryRows[i][5] == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                # If selected sub category matches rows sub category, show row
                elif self.month == self.subMenu:
                    if self.entryRows[i][5] == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                # If selected sub category does not match rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
           
            # If selected category is not equal to "All"
            elif self.menu_index != -1:
                # If selected sub category equals "All" and selected category equals rows category, show row
                if self.month == self.subMenu and self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == self.menu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                # If selected sub category does not equal rows sub category, or selected category doesn't equal rows category, hide row.
                elif self.month != self.subMenu or self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() != self.menu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
                # If selected sub category equals "All"
                if self.subMenu_index == self.data.allMonthMenu[0][0]:
                    # If selected category equals rows category, show row
                    if self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
    
    def generate_sidebars(self):
        #Clear existing data
        while len(self.menuListBox) > 0:
            self.menuListBox.remove(self.menuListBox.get_row_at_index(0))
        self.subMenu = self.data.allMonthMenu[0][1]
        
        # Reset Income/Expense Menu's
        self.incomeMenu = []
        self.expenseMenu = []
        self.dataSum = 0
       
        for i in range(0, len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "income":
                self.incomeMenu.append(self.data.transactionsMenu[i][0])
            if self.data.transactionsMenu[i][2] == "expense":
                self.expenseMenu.append(self.data.transactionsMenu[i][0])
        
        self.dataSum = 0
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.incomeMenu)):
                if self.data.transactions[i][0][0] == self.incomeMenu[j]:
                    self.dataSum += self.data.transactions[i][2]
       
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.expenseMenu)):
                if self.data.transactions[i][0][0] == self.expenseMenu[j]:
                    self.dataSum -= self.data.transactions[i][2]

        # Generate from database
        self.transactionsLabel = Gtk.Label()
        self.transactionsLabel.set_markup("<span><b>All Transactions</b></span>")
        self.transactionsLabel.set_halign(Gtk.Align.START)
        
        self.label2 = Gtk.Label()
        if self.dataSum >= 0:
            self.label2.set_markup("<span foreground=\"green\">" + "$" + str(self.dataSum) + "</span>")
        elif self.dataSum < 0:
            self.label2.set_markup("<span foreground=\"red\">" + "$" + str(self.dataSum) + "</span>")
        self.label2.set_halign(Gtk.Align.END)

        self.transactionsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.transactionsBox.pack_start(self.transactionsLabel, False, False, 0)
        self.transactionsBox.pack_end(self.label2, False, False, 5)

        self.menuListBox.add(self.transactionsBox)
        
        # Income Label 
        self.incomeLabel = Gtk.Label()
        self.incomeLabel.set_markup("<span><b>Income</b></span>")
        self.incomeLabel.set_halign(Gtk.Align.START)
        
        self.dataSum = 0
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.incomeMenu)):
                if self.data.transactions[i][0][0] == self.incomeMenu[j]:
                    self.dataSum += self.data.transactions[i][2]
        
        self.label2 = Gtk.Label()
        self.label2.set_markup("<span foreground=\"green\">" + "$" + str(self.dataSum) + "</span>")
        self.label2.set_halign(Gtk.Align.END)

        self.incomeBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.incomeBox.pack_start(self.incomeLabel, False, False, 0)
        self.incomeBox.pack_end(self.label2, False, False, 5)

        self.menuListBox.add(self.incomeBox)
       
        # Income Categories 
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "income":
                if self.data.transactionsMenu[i][1] != "Uncategorized":
                    uniqueID = self.data.transactionsMenu[i][0]
                    self.label = Gtk.Label(self.data.transactionsMenu[i][1])
                    self.label.set_halign(Gtk.Align.START)
                    self.label.set_margin_start(10)
                    
                    self.entry = Gtk.Entry()
                    self.entry.set_text(self.label.get_label())
    
                    self.entry.connect("activate", self.on_selectButton_clicked)

                    self.dataSum = 0
                    for j in range(0, len(self.data.transactions)):
                        if self.data.transactions[j][0][0] == uniqueID:
                            self.dataSum += self.data.transactions[j][2]
                    
                    self.label2 = Gtk.Label()
                    self.label2.set_markup("<span foreground=\"green\">" + "$" + str(self.dataSum) + "</span>")
                    self.label2.set_halign(Gtk.Align.END)
                    
                    self.button = self.create_delete_button(self.label.get_text())

                    self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.labelBox.pack_start(self.label, False, False, 0)
                    self.labelBox.pack_start(self.entry, False, False, 0)
                    self.labelBox.pack_end(self.button, False, False, 5)
                    self.labelBox.pack_end(self.label2, False, False, 5)

                    self.menuListBox.add(self.labelBox)
                    
                    self.incomeCount += 1
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "income":
                if self.data.transactionsMenu[i][1] == "Uncategorized":
                    uniqueID = self.data.transactionsMenu[i][0]
                    self.label = Gtk.Label(self.data.transactionsMenu[i][1])
                    self.label.set_halign(Gtk.Align.START)
                    self.label.set_margin_start(10)
                   
                    self.dataSum = 0
                    for j in range(0, len(self.data.transactions)):
                        if self.data.transactions[j][0][0] == uniqueID:
                            self.dataSum += self.data.transactions[j][2]
                    
                    self.label2 = Gtk.Label()
                    self.label2.set_markup("<span foreground=\"green\">" + "$" + str(self.dataSum) + "</span>")
                    self.label2.set_halign(Gtk.Align.END)
                    
                    self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.labelBox.pack_start(self.label, False, False, 0)
                    self.labelBox.pack_end(self.label2, False, False, 5)

                    self.menuListBox.add(self.labelBox)
                    
                    self.incomeCount += 1
        
        # Expense Label
        self.expenseLabel = Gtk.Label()
        self.expenseLabel.set_markup("<span><b>Expenses</b></span>")
        self.expenseLabel.set_halign(Gtk.Align.START)
        
        self.dataSum = 0
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.expenseMenu)):
                if self.data.transactions[i][0][0] == self.expenseMenu[j]:
                    self.dataSum += self.data.transactions[i][2]
        
        self.label2 = Gtk.Label()
        self.label2.set_markup("<span foreground=\"red\">" + "$" + str(self.dataSum) + "</span>")
        self.label2.set_halign(Gtk.Align.END)

        self.expenseBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.expenseBox.pack_start(self.expenseLabel, False, False, 0)
        self.expenseBox.pack_end(self.label2, False, False, 5)
        
        self.menuListBox.add(self.expenseBox)
        
        # Expense Categories
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "expense":
                if self.data.transactionsMenu[i][1] != "Uncategorized":
                    uniqueID = self.data.transactionsMenu[i][0]
                    self.label = Gtk.Label(self.data.transactionsMenu[i][1])
                    self.label.set_halign(Gtk.Align.START)
                    self.label.set_margin_start(10)
                    
                    self.entry = Gtk.Entry()
                    self.entry.set_text(self.label.get_label())
                    
                    self.dataSum = 0
                    for j in range(0, len(self.data.transactions)):
                        if self.data.transactions[j][0][0] == uniqueID:
                            self.dataSum += self.data.transactions[j][2]
                    
                    self.label2 = Gtk.Label()
                    self.label2.set_markup("<span foreground=\"red\">" + "$" + str(self.dataSum) + "</span>")
                    self.label2.set_halign(Gtk.Align.END)
                    self.button = self.create_delete_button(self.label.get_text())

                    self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.labelBox.pack_start(self.label, False, False, 0)
                    self.labelBox.pack_start(self.entry, False, False, 0)
                    self.labelBox.pack_end(self.button, False, False, 5)
                    self.labelBox.pack_end(self.label2, False, False, 5)
                    

                    self.menuListBox.add(self.labelBox)
                    #self.menuListBox.add(self.label)
                    
                    self.expenseCount += 1
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "expense":
                if self.data.transactionsMenu[i][1] == "Uncategorized":
                    uniqueID = self.data.transactionsMenu[i][0]
                    self.label = Gtk.Label(self.data.transactionsMenu[i][1])
                    self.label.set_halign(Gtk.Align.START)
                    self.label.set_margin_start(10)
                    
                    self.dataSum = 0
                    for j in range(0, len(self.data.transactions)):
                        if self.data.transactions[j][0][0] == uniqueID:
                            self.dataSum += self.data.transactions[j][2]
                    
                    self.label2 = Gtk.Label()
                    self.label2.set_markup("<span foreground=\"red\">" + "$" + str(self.dataSum) + "</span>")
                    self.label2.set_halign(Gtk.Align.END)

                    self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                    self.labelBox.pack_start(self.label, False, False, 0)
                    self.labelBox.pack_end(self.label2, False, False, 5)
                    

                    self.menuListBox.add(self.labelBox)
                    #self.menuListBox.add(self.label)
                    
                    self.expenseCount += 1
           
        self.incomeAllIndex = 1
        self.expenseAllIndex = self.incomeCount + 1

        self.menuListBox.show_all()
        for i in range(len(self.menuListBox)):
            if self.editable_category(i):
                self.category_view_mode(i)
        
        # Create Add and Edit Category Buttons
        self.editCategoryButton = Gtk.Button()
        self.addCategoryButton = Gtk.Button()
        
        self.addCategoryPopover = Gtk.Popover.new(self.addCategoryButton)
        self.add_category_popover = Add_Category_Popover(self.data)
        self.addCategoryPopover.add(self.add_category_popover.addGrid)
        
        # Style Widgets
        self.editCategoryIcon = Gio.ThemedIcon(name="list-remove-symbolic")
        self.editCategoryImage = Gtk.Image.new_from_gicon(self.editCategoryIcon, Gtk.IconSize.MENU)
        self.editCategoryButton.add(self.editCategoryImage)
        self.editCategoryButton.set_relief(Gtk.ReliefStyle.NONE)
        
        self.addCategoryIcon = Gio.ThemedIcon(name="list-add-symbolic")
        self.addCategoryImage = Gtk.Image.new_from_gicon(self.addCategoryIcon, Gtk.IconSize.MENU)
        self.addCategoryButton.add(self.addCategoryImage)
        self.addCategoryButton.set_relief(Gtk.ReliefStyle.NONE)
        
        self.editCategoryBox.add(self.editCategoryButton)
        self.editCategoryBox.add(self.addCategoryButton)
        self.menuListBox.add(self.editCategoryBox)
        self.editCategoryBox.show_all()
       
        # Connect Widgets
        self.editCategoryButton.connect("clicked", self.on_selectButton_clicked)
        self.addCategoryButton.connect("clicked", self.add_category_popover.on_addCategoryButton_clicked, self.addCategoryPopover)
        

        # Select default option
        self.menuListBox.select_row(self.menuListBox.get_row_at_index(0))
    
    def menu_clicked(self, listbox, row):
        # To catch calls before widget exists.
        if row == None:
            return
        else:
            menu = self.data.transactionsMenu
            data = self.data.transactions

            if row.get_child().get_children()[0].get_label() == "<span><b>All Transactions</b></span>":
                self.menu = "all transactions"
                self.menu_index = -1
            elif row.get_child().get_children()[0].get_label() == "<span><b>Income</b></span>":
                self.menu = "income"
                self.menu_index = -2
            elif row.get_child().get_children()[0].get_label() == "<span><b>Expenses</b></span>":
                self.menu = "expense"
                self.menu_index = -3
            elif row.get_child().get_children()[0].get_label() == "Uncategorized" and row.get_index() < (len(self.menuListBox) - 1):
                self.menu = "income"
                self.menu_index = -4
            elif row.get_child().get_children()[0].get_label() == "Uncategorized" and row.get_index() == (len(self.menuListBox) - 1):
                self.menu = "expense"
                self.menu_index = -5
            else:
                for i in range(len(menu)):
                    if menu[i][self.data.CATEGORY_TEXT] == row.get_child().get_children()[0].get_label():
                        self.menu = menu[i][self.data.CATEGORY_TEXT]
                        self.menu_index = menu[i][self.data.CATEGORY_INDEX]
            self.filter_menu(data, menu)
    
    def on_deleteButton_clicked(self, button, editPopover):
        if editPopover.get_visible():
            editPopover.hide()
        else:
            editPopover.show_all()

    def on_selectButton_clicked(self, *args):
        if self.editMode == 0:
            for i in range(len(self.menuListBox)):
                self.editMode = 1
                if self.editable_category(i):
                    self.category_edit_mode(i)
        elif self.editMode == 1:
            self.editMode = 0
            for i in range(len(self.menuListBox)):
                if self.editable_category(i):
                    if self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_TITLE].get_label() != self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].get_text():
                        for j in range(0, len(self.data.transactionsMenu)):
                            # Find matching menu item and uniqueID in database
                            if self.data.transactionsMenu[j][1] == self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_label():
                                self.data.edit_category(self.data.transactionsMenu[j][0],self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].get_text())
                    self.category_view_mode(i)
                    
    def subMenu_clicked(self, listbox, *args):
        # To catch calls before widget exists.
        if listbox == None:
            return
        else:
            menu = self.data.transactionsMenu
            data = self.data.transactions
            
            for i in range (len(self.data.allMonthMenu)):
                if self.data.allMonthMenu[i][self.data.CATEGORY_INDEX] == listbox.get_active():
                    self.row = self.data.allMonthMenu[i][self.data.CATEGORY_INDEX]
            self.subMenu = self.data.allMonthMenu[self.row][self.data.CATEGORY_TEXT]
            self.subMenu_index = self.data.allMonthMenu[self.row][self.data.CATEGORY_INDEX]
            self.filter_subMenu(data, menu)
