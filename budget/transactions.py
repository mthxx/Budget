from gi.repository import Gtk, Gio, Gdk
from edit_mode import Edit_Entry
from add_popover import Add_Category_Popover
import datetime

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
        self.entryRows = []
        
        self.selected_category = ""
        self.selected_category_index = 0
        self.selected_month = ""
        self.selected_month_index = 0
        self.selected_year = 0
        self.selected_year_index = 0

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
        self.menuListBox.connect("row-selected",self.category_selected)
        
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
    
    def add_menu_item(self, i):
        uniqueID = self.data.transactionsMenu[i][self.data.MENU_ID_INDEX]
        self.label = Gtk.Label(self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX])
        self.label.set_halign(Gtk.Align.START)
        self.label.set_margin_start(10)
        
        self.entry = Gtk.Entry()
        self.entry.set_text(self.label.get_label())

        self.entry.connect("activate", self.on_selectButton_clicked)

        self.dataSum = 0
        for j in range(0, len(self.data.transactions)):
            if self.data.transactions[j][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == uniqueID:
                self.dataSum += self.data.transactions[j][self.data.TRANSACTION_VALUE_INDEX]
        
        self.label2 = Gtk.Label()
        if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "income":
            self.label2.set_markup("<span foreground=\"green\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        elif self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "expense":
            self.label2.set_markup("<span foreground=\"red\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        self.label2.set_halign(Gtk.Align.END)
        
        self.button = self.create_delete_button(self.label.get_text())

        self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.labelBox.pack_start(self.label, False, False, 0)
        self.labelBox.pack_start(self.entry, False, False, 0)
        self.labelBox.pack_end(self.button, False, False, 5)
        self.labelBox.pack_end(self.label2, False, False, 5)

        self.menuListBox.add(self.labelBox)
   
    def add_menu_item_uncategorized(self, i):
        uniqueID = self.data.transactionsMenu[i][self.data.MENU_ID_INDEX]
        self.label = Gtk.Label(self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX])
        self.label.set_halign(Gtk.Align.START)
        self.label.set_margin_start(10)
       
        self.dataSum = 0
        for j in range(0, len(self.data.transactions)):
            if self.data.transactions[j][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == uniqueID:
                self.dataSum += self.data.transactions[j][self.data.TRANSACTION_VALUE_INDEX]
        
        self.label2 = Gtk.Label()
        if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "income":
            self.label2.set_markup("<span foreground=\"green\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        elif self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "expense":
            self.label2.set_markup("<span foreground=\"red\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        self.label2.set_halign(Gtk.Align.END)
        
        self.labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.labelBox.pack_start(self.label, False, False, 0)
        self.labelBox.pack_end(self.label2, False, False, 5)

        self.menuListBox.add(self.labelBox)

    def category_edit_mode(self, index):
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_TITLE].hide()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BALANCE].hide()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].show()
            self.menuListBox.get_row_at_index(index).get_child().get_children()[self.EDIT_CATEGORY_BUTTON].show()
    
    def category_selected(self, listbox, row):
        # To catch calls before widget exists.
        if row == None:
            return
        else:
            if row.get_child().get_children()[0].get_label() == "<span><b>All Transactions</b></span>":
                self.selected_category = "all transactions"
                self.selected_category_index = -1
            elif row.get_child().get_children()[0].get_label() == "<span><b>Income</b></span>":
                self.selected_category = "income"
                self.selected_category_index = -2
            elif row.get_child().get_children()[0].get_label() == "<span><b>Expenses</b></span>":
                self.selected_category = "expense"
                self.selected_category_index = -3
            elif row.get_child().get_children()[0].get_label() == "Uncategorized" and row.get_index() < (len(self.menuListBox) - 2):
                self.selected_category = "income"
                self.selected_category_index = -4
            elif row.get_child().get_children()[0].get_label() == "Uncategorized" and row.get_index() >= (len(self.menuListBox) - 2):
                self.selected_category = "expense"
                self.selected_category_index = -5
            else:
                for i in range(len(self.data.transactionsMenu)):
                    if self.data.transactionsMenu[i][self.data.TRANSACTION_MENU_NAME_INDEX] == row.get_child().get_children()[0].get_label():
                        self.selected_category = self.data.transactionsMenu[i][self.data.TRANSACTION_MENU_NAME_INDEX]
                        self.selected_category_index = self.data.transactionsMenu[i][self.data.TRANSACTION_MENU_ID_INDEX]
            self.filter_entries()
    
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
        
        self.dateComboMonth = Gtk.ComboBoxText()
        self.dateComboYear = Gtk.ComboBoxText()
        
        self.currentDate = datetime.datetime.now()
        
        self.dateButtonFrom = Gtk.Button()
        self.dateCalendarFrom = Gtk.Calendar()
        self.datePopoverFrom = Gtk.Popover.new(self.dateButtonFrom)
        self.datePopoverFrom.add(self.dateCalendarFrom)

        self.dateCalendarFrom.select_day(self.currentDate.day)
        self.dateCalendarFrom.select_month(self.currentDate.month - 1, self.currentDate.year)
        self.dateButtonFrom.set_label(self.data.translate_date(self.dateCalendarFrom.get_date(),"edit"))

        self.dateLabelTo = Gtk.Label("to")
       
        self.dateButtonTo = Gtk.Button()
        self.dateCalendarTo = Gtk.Calendar()
        self.datePopoverTo = Gtk.Popover.new(self.dateButtonTo)
        self.datePopoverTo.add(self.dateCalendarTo)
        
        self.dateCalendarTo.select_day(self.currentDate.day)
        self.dateCalendarTo.select_month(self.currentDate.month - 1, self.currentDate.year)
        self.dateButtonTo.set_label(self.data.translate_date(self.dateCalendarFrom.get_date(),"edit"))
        
        self.monthYearRadio = Gtk.RadioButton.new_with_label(None, "Month/Year")
        self.rangeRadio = Gtk.RadioButton.new_with_label(None, "Range")
        self.rangeRadio.join_group(self.monthYearRadio)

        self.dateGrid.attach(self.monthYearRadio,0,0,1,1)
        self.dateGrid.attach(self.rangeRadio,1,0,1,1)
        self.dateGrid.attach(self.dateLabelMonth,2,0,1,1)
        self.dateGrid.attach(self.dateComboMonth,3,0,1,1)
        self.dateGrid.attach(self.dateLabelYear,4,0,1,1)
        self.dateGrid.attach(self.dateComboYear,5,0,1,1)
        self.dateGrid.attach(self.dateButtonFrom,6,0,1,1) 
        self.dateGrid.attach(self.dateLabelTo,7,0,1,1) 
        self.dateGrid.attach(self.dateButtonTo,8,0,1,1) 
        
        # Generate Months
        for i in range(0,len(self.data.allMonthMenu)):
            self.dateComboMonth.append_text(self.data.allMonthMenu[i][1])

        self.dateButtonFrom.set_property("width-request",100)
        self.dateButtonTo.set_property("width-request",100)
        
        # Connect to handler    
        self.dateComboMonth.connect("changed",self.month_selected)
        self.dateComboYear.connect("changed",self.year_selected)
        self.monthYearRadio.connect("toggled", self.on_dateRadio_toggled)
        self.dateButtonFrom.connect("clicked", self.on_datePopover_clicked, self.datePopoverFrom)
        self.dateButtonTo.connect("clicked", self.on_datePopover_clicked, self.datePopoverTo)
        self.datePopoverFrom.connect("closed", self.on_datePopover_closed, self.dateCalendarFrom, self.dateButtonFrom)
        self.datePopoverTo.connect("closed", self.on_datePopover_closed, self.dateCalendarTo, self.dateButtonTo)

        for i in range(0,len(self.data.yearMenu)):
            self.dateComboYear.append_text(self.data.yearMenu[i])

        self.dateComboMonth.set_active(0)
        self.dateComboYear.set_active(0)
       
        self.monthYearRadio.set_margin_start(20)
        self.monthYearRadio.set_margin_top(2)
        self.monthYearRadio.set_margin_end(5)
        
        self.dateLabelMonth.set_margin_start(30)
        self.dateLabelMonth.set_margin_end(5)

        self.dateComboMonth.set_margin_top(10)
        self.dateComboMonth.set_margin_bottom(10)
        self.dateComboMonth.set_margin_end(10)
        
        self.dateLabelYear.set_margin_start(5)
        self.dateLabelYear.set_margin_end(5)
        
        self.dateComboYear.set_margin_top(10) 
        self.dateComboYear.set_margin_bottom(10)
        self.dateComboYear.set_margin_end(50)
        
        self.rangeRadio.set_margin_top(2)
        self.rangeRadio.set_margin_end(5)
        
        self.dateButtonFrom.set_margin_start(30)
        self.dateButtonFrom.set_margin_top(10)
        self.dateButtonFrom.set_margin_bottom(10)
        self.dateButtonFrom.set_margin_end(5)
        
        self.dateLabelTo.set_margin_end(5)
        
        self.dateButtonTo.set_margin_top(10)
        self.dateButtonTo.set_margin_bottom(10)
        
        self.month_year_visible(True)
        self.range_visible(False)
    
    def on_datePopover_clicked(self, button, datePopover):
        if datePopover.get_visible():
            datePopover.hide()
        else:
            datePopover.show_all()
    
    def on_datePopover_closed(self, datePopover, dateCalendar, dateButton):
        dateString = self.data.translate_date(dateCalendar.get_date(),"edit")
        dateButton.set_label(dateString)
        if self.dateButtonFrom.get_label() != None and self.dateButtonTo.get_label() != None:
            self.filter_entries()

    def create_delete_button(self, label):
        self.button = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="window-close-symbolic")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.MENU)
        self.button.add(self.image)
        self.button.show_all()
        
        self.editView = Gtk.Popover.new(self.button)
        
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
        self.button.connect("clicked", self.on_deleteButton_clicked, self.editView)
        self.deleteCancelButton.connect("clicked", self.on_deleteButton_clicked, self.editView)
        self.deleteConfirmButton.connect("clicked", self.delete_category_confirm, label)

        self.deleteSelectorBox.add(self.deleteCancelButton)
        self.deleteSelectorBox.add(self.deleteConfirmButton)
        
        self.editGrid.attach(self.confirmLabelLine1, 0, 0, 2, 1)
        self.editGrid.attach(self.confirmLabelLine2, 0, 1, 2, 1)
        self.editGrid.attach(self.deleteSelectorBox, 0, 2, 2, 1)
        
        self.editView.add(self.editGrid)

        return self.button
    
    def on_dateRadio_toggled(self, *args):
        if self.monthYearRadio.get_active() == True:
            self.month_year_visible(True)
            self.range_visible(False)
            self.filter_entries()
        if self.rangeRadio.get_active() == True:
            self.month_year_visible(False)
            self.range_visible(True)
            self.filter_entries()

    def delete_category_confirm(self, button, label):
        #print("Hello")
        for i in range(len(self.menuListBox)):
            if self.menuListBox.get_row_at_index(i) == None:
                return
            elif self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_text() == label:
                for j in range(0, len(self.data.transactionsMenu)):
                    # Find matching menu item and uniqueID in database
                    if self.data.transactionsMenu[j][self.data.MENU_NAME_INDEX] == self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_label():
                        self.data.delete_category(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX])
                        self.editMode = 0
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
                if int(self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]) == int(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX]) and self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX] == "income":
                    self.costLabel.set_markup("<span foreground=\"green\">" + str("%0.2f" % (self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX],)) + "</span>")
           
            for j in range(0, len(self.data.transactionsMenu)):
                if int(self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]) == int(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX]) and self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX] == "expense":
                    self.costLabel.set_markup("<span foreground=\"red\">" + str("%0.2f" % (self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX],)) + "</span>")

            self.descriptionLabel.set_markup("<i>" + self.data.transactions[i][self.data.TRANSACTION_DESCRIPTION_INDEX] + "</i>")
            
            # Create Edit Popover
            self.editButton = Gtk.Button()
            self.editView = Gtk.Popover.new(self.editButton)
            self.edit_view = Edit_Entry(self.data, "transaction")
            self.editView.add(self.edit_view.editGrid)

            # Style Widgets
            self.entryGrid.set_halign(Gtk.Align.CENTER)
            self.entryGrid.set_hexpand(True)
            self.categoryLabel.set_markup(self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_NAME_INDEX])
            self.categoryLabel.set_property("height-request", 50)
            self.categoryLabel.set_property("xalign", 1)
            self.categoryLabel.set_width_chars(15)
            
            self.dateLabel.set_margin_start(30)
            self.dateLabel.set_margin_end(30)
            self.dateLabel.set_width_chars(15)
            
            self.costGrid.set_row_homogeneous(True)
            self.costLabel.set_property("xalign", .05)
            self.costLabel.set_width_chars(14)
            
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
                if self.data.transactionsMenu[j][self.data.MENU_ID_INDEX] == self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]:
                    self.transactionType = self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX]
            
            self.entryRows.append([self.layoutGrid, [self.categoryLabel, self.dateLabel, self.currencyLabel, self.costLabel, self.descriptionLabel, self.editButton], self.entryGrid, self.costGrid, self.data.transactions[i][self.data.TRANSACTION_ID_INDEX], self.transactionType])
            self.editButton.connect("clicked", self.edit_view.on_editDropdown_clicked, self.editView, self.data.transactions[i][self.data.TRANSACTION_ID_INDEX], self.entryRows[i],  self.contentGrid, self.data.transactions[i])
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
   
    def filter_entries(self):
        if hasattr(self, "monthYearRadio"):
            for i in range (0,len(self.entryRows)):
                self.date = self.entryRows[i][1][1].get_label().split()
                self.entry_month =  self.date[0]
                self.entry_day = self.date[1]
                self.entry_year = self.date[2]
                
                self.entry_day = self.entry_day.rstrip(",") 
                self.entry_day = self.entry_day.rstrip("st") 
                self.entry_day = self.entry_day.rstrip("th") 
                self.entry_day = self.entry_day.rstrip("nd") 
                self.entry_day = self.entry_day.rstrip("rd") 
                    
                if self.monthYearRadio.get_active() == True:
                    
                    # If selected category item is "All"
                    if self.selected_category_index == -1:
                        self.filter_month(i)
                     # If selected category item is "Income" or "Expenses"
                    elif self.selected_category_index == -2 or self.selected_category_index == -3:
                        if self.selected_category == self.entryRows[i][5]:
                            self.filter_month(i)
                        elif self.selected_category != self.entryRows[i][5]:
                            self.hide_entry(i)
                    
                    # If selected category item is "Uncategorized"
                    elif (self.selected_category_index == -4 or self.selected_category_index == -5):
                        if (self.selected_category == self.entryRows[i][5] and self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == "Uncategorized"):
                            self.filter_month(i)
                        elif (self.selected_category != self.entryRows[i][5] or self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() != "Uncategorized"):
                            self.hide_entry(i)
                    
                    # If selected menu item is not "All"
                    elif self.selected_category_index != -1:
                        if self.selected_category == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                            self.filter_month(i)
                        if self.selected_category != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                            self.hide_entry(i)
            
                elif self.rangeRadio.get_active() == True:
                    
                    self.fromArr = self.dateCalendarFrom.get_date()
                    self.toArr = self.dateCalendarTo.get_date()
                    
                    self.fromYear = self.fromArr[0]
                    self.fromMonth = self.fromArr[1]
                    self.fromMonth += 1
                    self.fromDay= self.fromArr[2]
                    
                    self.entry_month = self.data.translate_date(self.entry_month, "month")
                    
                    self.toYear = self.toArr[0]
                    self.toMonth = self.toArr[1]
                    self.toMonth += 1
                    self.toDay= self.toArr[2]
    
                    # If selected category item is "All"
                    if self.selected_category_index == -1:
                        self.filter_range(i)
                    # If selected category item is "Income" or "Expenses"
                    elif self.selected_category_index == -2 or self.selected_category_index == -3:
                        if self.selected_category == self.entryRows[i][5]:
                            self.filter_range(i)
                        elif self.selected_category != self.entryRows[i][5]:
                            self.hide_entry(i)
                    
                    # If selected category item is "Uncategorized"
                    elif (self.selected_category_index == -4 or self.selected_category_index == -5):
                        if (self.selected_category == self.entryRows[i][5] and self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() == "Uncategorized"):
                            self.filter_range(i)
                        elif (self.selected_category != self.entryRows[i][5] or self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label() != "Uncategorized"):
                            self.hide_entry(i)
                            
                    # If selected menu item is not "All"
                    elif self.selected_category_index != -1:
                        if self.selected_category == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                            self.filter_range(i)
                        if self.selected_category != self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_label():
                            self.hide_entry(i)
    
    def filter_month(self, i):
        # If selected month equals "All"
        if self.selected_month == self.data.allMonthMenu[self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_NAME_INDEX]:
            # Check Year Filter
            self.filter_year(i)
        # If selected month does not equal "All"
        elif self.selected_month != self.data.allMonthMenu[self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_NAME_INDEX]:
            # If selected month equals entry's month
            if self.selected_month == self.entry_month:
                # Check Year Filter
                self.filter_year(i)
            # If selected month does not equal entry's month
            else:
                self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                self.contentGrid.queue_draw()
    
    def filter_range(self,i):
        # Same from and to year
        if int(self.entry_year) == int(self.fromYear) and int(self.entry_year) == int(self.toYear):
            # Same from and to month
            if int(self.entry_month) == int(self.fromMonth) and int(self.entry_month) == int(self.toMonth):
                if int(self.entry_day) >= int(self.fromDay) and int(self.entry_day) <= int(self.toDay):
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                    self.contentGrid.queue_draw()
                else:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            # Different from and to month
            elif int(self.entry_month) >= int(self.fromMonth) and int(self.entry_month) <= int(self.toMonth):
                if int(self.entry_month) == int(self.fromMonth):# and int(self.entry_month) != int(self.toMonth):
                    if int(self.entry_day) >= int(self.fromDay):
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    else:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                elif int(self.entry_month) == int(self.toMonth):
                    if int(self.entry_day) <= int(self.toDay):
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    else:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
            else:
                self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                self.contentGrid.queue_draw()
        elif (int(self.entry_year) != int(self.fromYear) or int(self.entry_year) != int(self.toYear)) and (int(self.entry_year) >= int(self.fromYear) and int(self.entry_year) <= int(self.toYear)):
            if int(self.entry_year) == int(self.fromYear):
                if int(self.entry_month >= self.fromMonth):
                    if int(self.entry_day) >= int(self.fromDay):
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    else:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                else:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            elif int(self.entry_year) == int(self.toYear):
                if int(self.entry_month <= self.toMonth):
                    if int(self.entry_day) <= int(self.toDay):
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                        self.contentGrid.queue_draw()
                    else:
                        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                        self.contentGrid.queue_draw()
                else:
                    self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                    self.contentGrid.queue_draw()
            elif int(self.entry_year) != int(self.fromYear) and int(self.entry_year) != int(self.toYear):
                self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                self.contentGrid.queue_draw()
            else:
                self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                self.contentGrid.queue_draw()






        else:
            self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
            self.contentGrid.queue_draw()

    def filter_year(self, i):
        # if selected year equals "All", show row
        if self.selected_year == self.data.yearMenu[0]:
            self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
            self.contentGrid.queue_draw()
        # if selected year does not equal "All"
        elif self.selected_year != self.data.yearMenu[0]:
            if self.selected_year == self.entry_year:
                self.entryRows[i][self.LAYOUT_GRID_INDEX].show()
                self.contentGrid.queue_draw()
            else:
                self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
                self.contentGrid.queue_draw()

    def generate_sidebars(self):
        #Clear existing data
        while len(self.menuListBox) > 0:
            self.menuListBox.remove(self.menuListBox.get_row_at_index(0))
        self.subMenu = self.data.allMonthMenu[0][1]
       
        # Get Current Balance
        self.dataSum = 0
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.data.incomeMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.incomeMenu[j]:
                    self.dataSum += self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]
       
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.data.expenseMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.expenseMenu[j]:
                    self.dataSum -= self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]

        # Generate from database
        self.transactionsLabel = Gtk.Label()
        self.transactionsLabel.set_markup("<span><b>All Transactions</b></span>")
        self.transactionsLabel.set_halign(Gtk.Align.START)
        
        self.label2 = Gtk.Label()
        if self.dataSum >= 0:
            self.label2.set_markup("<span foreground=\"green\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        elif self.dataSum < 0:
            self.label2.set_markup("<span foreground=\"red\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
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
            for j in range(0, len(self.data.incomeMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.incomeMenu[j]:
                    self.dataSum += self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]
        
        self.label2 = Gtk.Label()
        self.label2.set_markup("<span foreground=\"green\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        self.label2.set_halign(Gtk.Align.END)

        self.incomeBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.incomeBox.pack_start(self.incomeLabel, False, False, 0)
        self.incomeBox.pack_end(self.label2, False, False, 5)

        self.menuListBox.add(self.incomeBox)
       
        # Income Categories 
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "income":
                if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] != "Uncategorized":
                    self.add_menu_item(i)
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "income":
                if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] == "Uncategorized":
                    self.add_menu_item_uncategorized(i)
        
        # Expense Label
        self.expenseLabel = Gtk.Label()
        self.expenseLabel.set_markup("<span><b>Expenses</b></span>")
        self.expenseLabel.set_halign(Gtk.Align.START)
        
        self.dataSum = 0
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.data.expenseMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.expenseMenu[j]:
                    self.dataSum += self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]
        
        self.label2 = Gtk.Label()
        self.label2.set_markup("<span foreground=\"red\">" + "$" + str("%0.2f" % (self.dataSum,)) + "</span>")
        self.label2.set_halign(Gtk.Align.END)

        self.expenseBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.expenseBox.pack_start(self.expenseLabel, False, False, 0)
        self.expenseBox.pack_end(self.label2, False, False, 5)
        
        self.menuListBox.add(self.expenseBox)
        
        # Expense Categories
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "expense":
                if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] != "Uncategorized":
                    self.add_menu_item(i)
        
        for i in range(0,len(self.data.transactionsMenu)):
            if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "expense":
                if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] == "Uncategorized":
                    self.add_menu_item_uncategorized(i)

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
        self.menuListBox.get_row_at_index(len(self.menuListBox)-1).set_selectable(False)
        self.editCategoryBox.show_all()
       
        # Connect Widgets
        self.editCategoryButton.connect("clicked", self.on_selectButton_clicked)
        self.addCategoryButton.connect("clicked", self.add_category_popover.on_addCategoryButton_clicked, self.addCategoryPopover)

        # Select default option
        self.menuListBox.select_row(self.menuListBox.get_row_at_index(0))
    
    def hide_entry(self, i):
        self.entryRows[i][self.LAYOUT_GRID_INDEX].hide()
        self.contentGrid.queue_draw()
    
    def month_selected(self, listbox, *args):
        # To catch calls before widget exists.
        if listbox == None:
            return
        else:
            for i in range (len(self.data.allMonthMenu)):
                if self.data.allMonthMenu[i][self.data.TRANSACTION_MENU_ID_INDEX] == listbox.get_active():
                    self.row = self.data.allMonthMenu[i][self.data.TRANSACTION_MENU_ID_INDEX]
            self.selected_month = self.data.allMonthMenu[self.row][self.data.TRANSACTION_MENU_NAME_INDEX]
            self.selected_month_index = self.data.allMonthMenu[self.row][self.data.TRANSACTION_MENU_ID_INDEX]
            self.filter_entries()
    
    def month_year_visible(self, boolean):
        self.dateLabelMonth.set_visible(boolean)
        self.dateComboMonth.set_visible(boolean)
        self.dateComboYear.set_visible(boolean)
        self.dateLabelYear.set_visible(boolean)
        # self.dateComboMonth.set_sensitive(boolean)
        # self.dateComboYear.set_sensitive(boolean)
    
    def on_deleteButton_clicked(self, button, editView):
        if editView.get_visible():
            editView.hide()
        else:
            editView.show_all()

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
                            if self.data.transactionsMenu[j][self.data.MENU_NAME_INDEX] == self.menuListBox.get_row_at_index(i).get_child().get_children()[0].get_label():
                                self.data.edit_category(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX],self.menuListBox.get_row_at_index(i).get_child().get_children()[self.EDIT_CATEGORY_ENTRY].get_text())
                    self.category_view_mode(i)
    
    def range_visible(self, boolean):
        self.dateButtonFrom.set_visible(boolean)
        self.dateButtonTo.set_visible(boolean)
        self.dateLabelTo.set_visible(boolean)

    def year_selected(self, listbox, *args):
        # To catch calls before widget exists.
        if listbox == None:
            return
        else:
            self.row = listbox.get_active()
            self.selected_year = self.data.yearMenu[self.row]
            self.selected_year_index = self.row
            self.filter_entries()
