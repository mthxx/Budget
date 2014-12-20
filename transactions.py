from gi.repository import Gtk, Gio, Gdk
from calc import Calc
from edit_popover import Edit_Popover

class Transactions():

    def __init__(self, data):
        
        # Content Grid
        self.LAYOUT_GRID_INDEX = 0           # Element

        # Layout Widgets
        self.LAYOUT_WIDGET_INDEX = 1         # Array
        self.CATEGORY_LABEL_INDEX = 0        # Element
        self.DATE_LABEL_INDEX = 1            # Element
        self.CURRENCY_LABEL_INDEX = 2        # Element
        self.COST_LABEL_INDEX = 3            # Element
        self.DESCRIPTION_LABEL_INDEX = 4     # Element
        self.EDIT_BUTTON_INDEX = 5
        
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
        self.menuScrolledWindow.set_property("width-request",277)
        self.menuScrolledWindow.set_property("hscrollbar-policy", Gtk.PolicyType.NEVER)

        self.subMenuScrolledWindow.set_vexpand(True)
        self.subMenuScrolledWindow.set_property("width-request",100)
        
        self.headerGrid.set_column_homogeneous(True)
        self.headerGrid.set_hexpand(True)
        
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        self.contentGrid.set_margin_left(20)
        self.contentGrid.set_margin_right(20)
       
        # Connect Widgets
        self.menuListBox.connect("row-selected",self.menu_clicked)
        self.subMenuListBox.connect("row-selected",self.subMenu_clicked)

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
        
        # Generate Sidebars and Content
        self.generate_sidebars()
        self.display_content()

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
        
        # Income Categories
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
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "income":
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
                
                self.button = self.create_delete_button(self.label.get_text())

                self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                self.labelBox.pack_start(self.label, False, False, 0)
                self.labelBox.pack_end(self.button, False, False, 5)
                self.labelBox.pack_end(self.label2, False, False, 5)

                self.menuListBox.add(self.labelBox)
                
                self.incomeCount += 1
        
        # Expense Categories
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
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][2] == "expense":
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
                
                self.button = self.create_delete_button(self.label.get_text())

                self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                self.labelBox.pack_start(self.label, False, False, 0)
                self.labelBox.pack_end(self.button, False, False, 5)
                self.labelBox.pack_end(self.label2, False, False, 5)

                self.menuListBox.add(self.labelBox)
                #self.menuListBox.add(self.label)
                
                self.expenseCount += 1
           
        self.incomeAllIndex = 1
        self.expenseAllIndex = self.incomeCount + 1

        # Add uncategorized
        # Style Widgets
        self.uncategorizedLabel = Gtk.Label("Uncategorized")
        self.uncategorizedLabel.set_property("height-request", 10)
        self.uncategorizedLabel.set_halign(Gtk.Align.START)
        self.uncategorizedLabel.set_margin_start(10)
                
        self.uncategorizedLabel2 = Gtk.Label()
        self.uncategorizedLabel2.set_markup("<span foreground=\"red\">" + "$" + "</span>")
        self.uncategorizedLabel2.set_halign(Gtk.Align.END)
                
        self.uncategorizedLabelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.uncategorizedLabelBox.pack_start(self.uncategorizedLabel, False, False, 0)
        self.uncategorizedLabelBox.pack_end(self.uncategorizedLabel2, False, False, 5)

        self.menuListBox.add(self.uncategorizedLabelBox)
        
        # Select default option
        self.menuListBox.select_row(self.menuListBox.get_row_at_index(0))
        
        self.label = Gtk.Label()
        self.label.set_markup("<span><b>All Months</b></span>")
        self.label.set_property("height-request", 10)
        self.label.set_halign(Gtk.Align.START)
        self.label.set_margin_bottom(5)
        self.subMenuListBox.add(self.label)
        
        for i in range(1,len(self.data.allMonthMenu)):
            self.label = Gtk.Label(self.data.allMonthMenu[i][1])
            self.label.set_property("height-request", 10)
            self.label.set_halign(Gtk.Align.START)
            self.label.set_margin_start(10)
            self.subMenuListBox.add(self.label)

        self.menuListBox.show_all()
        self.subMenuListBox.select_row(self.subMenuListBox.get_row_at_index(0))
        
    
    def display_content(self):
        #Clear existing data
        while len(self.contentGrid) > 0:
            self.contentGrid.remove_row(0)
            
        while len(self.entryRows) > 0:
                self.entryRows.pop(0)
        
        menu = self.data.transactionsMenu
        data = self.data.transactions
         
        self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
        self.monthRemainingTotalLabel.set_text("$1,500")
        self.percBudgetTotalLabel.set_text("50.00%")
        
        self.whiteSpaceLabel = Gtk.Label()
        
        self.index = 5
        for i in range (0,len(data)):
            
            # Date String
            self.dateString = ""
            self.dateString = self.data.translate_date(data, i)
            
            # Create Widgets
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.entryGrid = Gtk.Grid()
            self.costGrid = Gtk.Grid()
            
            self.categoryLabel = Gtk.Label()
            self.dateLabel = Gtk.Label(self.dateString)
            self.descriptionLabel = Gtk.Label()
            
            self.currencyLabel = Gtk.Label("$")
            self.costLabel = Gtk.Label(str(data[i][self.data.VALUE]))

            # Create Edit Popover
            self.editButton = Gtk.Button()
            self.editPopover = Gtk.Popover.new(self.editButton)
            self.edit_popover = Edit_Popover(self.data)
            self.editPopover.add(self.edit_popover.editGrid)
            self.editButton.connect("clicked", self.edit_popover.on_editDropdown_clicked, self.editPopover, data[i][self.data.UNIQUE_ID], self.entryRows, menu, self.contentGrid)

            # Style Widgets
            self.entryGrid.set_halign(Gtk.Align.CENTER)
            self.entryGrid.set_hexpand(True)
            
            self.categoryLabel.set_markup(data[i][self.data.CATEGORY][self.data.CATEGORY_TEXT])
            self.categoryLabel.set_property("height-request", 50)
            self.categoryLabel.set_property("xalign", 1)
            self.categoryLabel.set_width_chars(15)
            
            self.dateLabel.set_margin_start(30)
            self.dateLabel.set_margin_end(30)
            self.dateLabel.set_width_chars(15)
            
            self.costGrid.set_row_homogeneous(True)
            self.costLabel.set_property("xalign", .05)
            self.costLabel.set_width_chars(14)

            self.descriptionLabel.set_markup("<i>" + data[i][self.data.DESCRIPTION] + "</i>")
            
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
                if self.data.transactionsMenu[j][0] == data[i][self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                    self.transactionType = self.data.transactionsMenu[j][2]
            
            self.entryRows.append([self.layoutGrid, [self.categoryLabel, self.dateLabel, self.currencyLabel, self.costLabel, self.descriptionLabel, self.editButton], self.entryGrid, self.costGrid, data[i][self.data.UNIQUE_ID], self.transactionType])
            self.contentGrid.show_all() 
        

    def create_delete_button(self, label):
        self.button = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="window-close-symbolic")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.MENU)
        self.button.add(self.image)
        self.button.show_all()
        
        self.editPopover = Gtk.Popover.new(self.button)
        
        self.editGrid = Gtk.Grid()
        
        self.editButton = Gtk.Button("Edit")
        self.deleteButton = Gtk.Button("Delete")
        self.selectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        self.confirmLabelLine1 = Gtk.Label("Are you sure?")
        self.confirmLabelLine2 = Gtk.Label()
        self.deleteCancelButton = Gtk.Button("Cancel")
        self.deleteConfirmButton = Gtk.Button("Confirm")
        self.deleteSelectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Style Widgets
        self.editButton.set_size_request(100,32)
        self.deleteButton.set_size_request(100,32)
        self.deleteCancelButton.set_size_request(100,32)
        self.deleteConfirmButton.set_size_request(100,32)
        self.confirmLabelLine2.set_markup("<span foreground=\"red\"><b>This cannot be undone!</b></span>")
        Gtk.StyleContext.add_class(self.selectorBox.get_style_context(), "linked")
        Gtk.StyleContext.add_class(self.deleteSelectorBox.get_style_context(), "linked")
        self.selectorBox.set_margin_start(10)
        self.selectorBox.set_margin_top(10)
        self.selectorBox.set_margin_bottom(10)
        self.selectorBox.set_margin_end(5)
        self.confirmLabelLine1.set_margin_top(10)
        self.deleteSelectorBox.set_margin_start(10)
        self.deleteSelectorBox.set_margin_top(10)
        self.deleteSelectorBox.set_margin_bottom(10)
        self.deleteSelectorBox.set_margin_end(5)

        # Connect Widget Handlers
        self.button.connect("clicked", self.on_categoryModifyButton_clicked, self.editPopover, self.confirmLabelLine1, self.confirmLabelLine2, self.deleteSelectorBox)
        #self.editButton.connect("clicked", self.on_editButton_clicked, self.editPopover, self.confirmLabelLine1, self.confirmLabelLine2, self.deleteSelectorBox)
        self.deleteButton.connect("clicked", self.on_deleteButton_clicked, self.selectorBox, self.confirmLabelLine1, self.confirmLabelLine2, self.deleteSelectorBox)
        #self.deleteCancelButton.connect("clicked", self.on_deleteCancelButton_clicked)
        self.deleteConfirmButton.connect("clicked", self.delete_category_confirm, label)

        # Add Widgets to Grid
        self.selectorBox.add(self.editButton)
        self.selectorBox.add(self.deleteButton)

        self.deleteSelectorBox.add(self.deleteCancelButton)
        self.deleteSelectorBox.add(self.deleteConfirmButton)
        
        self.editGrid.attach(self.selectorBox,0,0,2,1)
        self.editGrid.attach(self.confirmLabelLine1, 0, 1, 2, 1)
        self.editGrid.attach(self.confirmLabelLine2, 0, 2, 2, 1)
        self.editGrid.attach(self.deleteSelectorBox, 0, 3, 2, 1)
        
        self.editPopover.add(self.editGrid)

        return self.button
    
    def on_categoryModifyButton_clicked(self, button, editPopover, confirmLabelLine1, confirmLabelLine2, deleteSelectorBox):
        if editPopover.get_visible():
            editPopover.hide()
        else:
            editPopover.show_all()
            confirmLabelLine1.hide()
            confirmLabelLine2.hide()
            deleteSelectorBox.hide()

    #def on_editButton_clicked(self, button, editPopover, confirmLabelLine1, confirmLabelLine2, deleteSelectorBox):
    #    print(editPopover)
    #    if editPopover.get_visible():
    #        editPopover.hide()
    #    else:
    #        editPopover.show_all()
    #        confirmLabelLine1.hide()
     #       confirmLabelLine2.hide()
     #       deleteSelectorBox.hide()
    
    def on_deleteButton_clicked(self, button, selectorBox, confirmLabelLine1, confirmLabelLine2, deleteSelectorBox):
        selectorBox.hide()
        confirmLabelLine1.show()
        confirmLabelLine2.show()
        deleteSelectorBox.show_all()

    def delete_category_confirm(self, button, label):
        for i in range(len(self.menuListBox) - 1):
            if self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_text() == label:
                self.menuListBox.remove(self.menuListBox.get_row_at_index(i))
        

    def on_selectButton_clicked(self, *args):
        if self.editMode == 0:
            for i in range(len(self.menuListBox) - 1):
                self.editMode = 1
                if (self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.transactionsLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.incomeLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.expenseLabel):
                    self.menuListBox.get_row_at_index(i).get_child().get_children()[1].hide()
                    self.menuListBox.get_row_at_index(i).get_child().get_children()[2].show()
        elif self.editMode == 1:
            self.editMode = 0
            for i in range(len(self.menuListBox)):
                if (self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.transactionsLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.incomeLabel
                    and self.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.expenseLabel):
                    
                    self.menuListBox.get_row_at_index(i).get_child().get_children()[1].show()
                    self.menuListBox.get_row_at_index(i).get_child().get_children()[2].hide()



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
            else:
                for i in range(len(menu)):
                    if menu[i][self.data.CATEGORY_TEXT] == row.get_child().get_children()[0].get_label():
                        self.menu = menu[i][self.data.CATEGORY_TEXT]
                        self.menu_index = menu[i][self.data.CATEGORY_INDEX]
            self.filter_menu(data, menu)
    
    def subMenu_clicked(self, listbox, row):
        # To catch calls before widget exists.
        if row == None:
            return
        else:
            menu = self.data.transactionsMenu
            data = self.data.transactions
            
            for i in range (len(self.data.allMonthMenu)):
                if self.data.allMonthMenu[i][self.data.CATEGORY_INDEX] == row.get_index():
                    self.row = self.data.allMonthMenu[i][self.data.CATEGORY_INDEX]
            self.subMenu = self.data.allMonthMenu[self.row][self.data.CATEGORY_TEXT]
            self.subMenu_index = self.data.allMonthMenu[self.row][self.data.CATEGORY_INDEX]
            self.filter_subMenu(data, menu)
        
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
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
                    self.contentGrid.queue_draw()
                # If selected sub category equals rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data, self.subMenu_index)))
                    self.contentGrid.queue_draw()
                # If selected sub category does not equal rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            
            # If selected menu item is "Income"
            elif self.menu_index == -2 or self.menu_index == -3:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][5]:
                    # If selectded sub menu is "All", show row.
                    if self.subMenu_index == self.data.allMonthMenu[0][self.data.CATEGORY_INDEX]:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))
                        self.contentGrid.queue_draw()
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data, self.menu_index, self.subMenu_index)))
                        self.contentGrid.queue_draw()
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                        #self.entryRows[i][0][1].hide()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))
                    self.contentGrid.queue_draw()
            
            # If selected menu item is not "All"
            elif self.menu_index != -1:
                # If selected category matches rows category
                if self.menu == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    # If selected sub menu is "All", show row.
                    if self.subMenu_index == self.data.allMonthMenu[0][self.data.CATEGORY_INDEX]:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))
                        self.contentGrid.queue_draw()
                    # If selected sub category matches rows sub category, show row
                    elif self.subMenu == self.month:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data, self.menu_index, self.subMenu_index)))
                        self.contentGrid.queue_draw()
                    # If row's category is not the selected category, hide row
                    elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                # If Row's category does not match selected category, hide row 
                elif self.menu != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data, self.menu_index)))
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
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
                    self.contentGrid.queue_draw()
                # If selected sub category matches rows sub category, show row
                elif self.month == self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))
                    self.contentGrid.queue_draw()
                # If selected sub category does not match rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))
                    self.contentGrid.queue_draw()
            
           # If selected category is equal to "Income or Expenses"
            elif self.menu_index == -2 or self.menu_index == -3 :
                # If sub category equals "All"
                if self.subMenu_index == self.data.allMonthMenu[self.data.CATEGORY][self.data.CATEGORY_INDEX]:
                    if self.entryRows[i][5] == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(data)))
                        self.contentGrid.queue_draw()
                # If selected sub category matches rows sub category, show row
                elif self.month == self.subMenu:
                    if self.entryRows[i][5] == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))
                        self.contentGrid.queue_draw()
                # If selected sub category does not match rows sub category, hide row
                elif self.month != self.subMenu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumMonthData(data,self.subMenu_index)))
                    self.contentGrid.queue_draw()
           
            # If selected category is not equal to "All"
            elif self.menu_index != -1:
                # If selected sub category equals "All" and selected category equals rows category, show row
                if self.month == self.subMenu and self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == self.menu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data,self.menu_index, self.subMenu_index)))
                    self.contentGrid.queue_draw()
                # If selected sub category does not equal rows sub category, or selected category doesn't equal rows category, hide row.
                elif self.month != self.subMenu or self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() != self.menu:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryMonthData(data,self.menu_index, self.subMenu_index)))
                    self.contentGrid.queue_draw()
                # If selected sub category equals "All"
                if self.subMenu_index == self.data.allMonthMenu[0][0]:
                    # If selected category equals rows category, show row
                    if self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == self.menu:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.monthTotalLabel.set_text("$" + str(self.calc.sumCategoryData(data,self.menu_index)))
                        self.contentGrid.queue_draw()
