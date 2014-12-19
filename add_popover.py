from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Add_Popover(Gtk.Window):

    def __init__(self, data):
        #Initialize Data
        self.data = data
        # Create Widgets
        self.addGrid = Gtk.Grid()
        self.addIncomeRadio = Gtk.RadioButton(None, "Income")
        self.addExpenseRadio = Gtk.RadioButton(self.addIncomeRadio, "Expense")
        self.addStack = Gtk.Stack()
        self.addStackSwitcher = Gtk.StackSwitcher()
        self.addStack.add_titled(self.addIncomeRadio, "Income", "Income")
        self.addStack.add_titled(self.addExpenseRadio, "Expense", "Expense")
        self.addStackSwitcher.set_stack(self.addStack)
        self.addCategoryLabel = Gtk.Label("Category")
        self.addCategoryComboBoxText = Gtk.ComboBoxText()
        self.addEntryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.addEntryLabel = Gtk.Label("Entry")
        self.addDescriptionLabel = Gtk.Label("Description")
        self.addCurrencyLabel = Gtk.Label("$ ")
        self.addEntry = Gtk.Entry()
        self.addEntry.set_input_purpose(Gtk.InputPurpose.NUMBER)
        self.addDescription = Gtk.Entry()
        self.addDate = Gtk.Calendar()
        self.addSubmitButton = Gtk.Button("Submit")
        
        self.addEntryBox.add(self.addCurrencyLabel)
        self.addEntryBox.add(self.addEntry)
        
        # Style Widgets
        self.addStackSwitcher.set_homogeneous(True)
        self.addStack.set_hexpand(True)        
        self.add_popover_margin(self.addStackSwitcher, 10)
        
        self.add_popover_margin(self.addCategoryComboBoxText, 10)
        self.add_popover_margin(self.addEntryBox, 10)
        self.add_popover_margin(self.addDescription, 10)
        self.addCategoryComboBoxText.set_margin_top(0)
        self.addEntryBox.set_margin_top(0)
        self.addEntryBox.set_margin_end(4)
        self.addDescription.set_margin_top(0)
        self.addDescription.set_margin_start(4)
        self.add_popover_margin(self.addDate, 10)
        self.add_popover_margin(self.addSubmitButton, 10)

        self.addCategoryComboBoxText.set_property("height-request", 34)

        self.radioStatus = "income"
        
        # Connect Widget Handlers
        self.addStackSwitcher.connect("set-focus-child", self.on_addRadio_toggled)
        
        # Add Widgets to Grid
        self.addGrid.attach(self.addStackSwitcher,0,0,2,1)
        
        self.addGrid.attach(self.addCategoryLabel,0,1,2,1)
        self.addGrid.attach(self.addCategoryComboBoxText,0,2,2,1)
        self.addGrid.attach(self.addEntryLabel,0,3,1,1)
        self.addGrid.attach(self.addDescriptionLabel,1,3,1,1)
        self.addGrid.attach(self.addEntryBox,0,4,1,1)
        self.addGrid.attach(self.addDescription,1,4,1,1)
        self.addGrid.attach(self.addDate,0,5,2,1)
        self.addGrid.attach(self.addSubmitButton,0,6,2,1)
        self.addEntry.connect("activate", self.on_addSubmitButton_clicked)
        self.addDescription.connect("activate", self.on_addSubmitButton_clicked)
        self.addSubmitButton.connect("clicked", self.on_addSubmitButton_clicked)
    
    def add_popover_margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_end(margin)
        widget.set_margin_bottom(margin)
    
    def on_addButton_clicked(self, button, addPopover):
        if addPopover.get_visible():
            addPopover.hide()
        else:
            for i in range(0,len(self.data.transactionsMenu)):
                if self.data.transactionsMenu[i][2] == "income":
                    self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][1])
            addPopover.show_all()

    def on_addRadio_toggled(self, *args):
        if args[1] != None:
            for i in range(0, len(self.data.transactionsMenu)):
                self.addCategoryComboBoxText.remove(0)
            if args[1].get_group()[0].get_active():
                self.radioStatus = "income"
                for i in range(0,len(self.data.transactionsMenu)):
                    if self.data.transactionsMenu[i][2] == "income":
                        self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][1])
            if args[1].get_group()[1].get_active():
                self.radioStatus = "expense"
                for i in range(0,len(self.data.transactionsMenu)):
                    if self.data.transactionsMenu[i][2] == "expense":
                        self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][1])
    
    def on_addSubmitButton_clicked(self, *args):
        self.entryString = ""
        
        if self.addCategoryComboBoxText.get_active() < 0:
            self.addCategoryLabel.set_markup("<span foreground=\"red\"><b>* Category</b></span>")
        else:
            self.addCategoryLabel.set_text("Category")
        
        if self.addEntry.get_text() == "":
            self.addEntryLabel.set_markup("<span foreground=\"red\"><b>* Entry</b></span>")
        else:
            self.addEntryLabel.set_text("Entry")
        
        if self.addCategoryComboBoxText.get_active() >= 0 and self.addEntry.get_text() != "":
            self.dateArr = self.addDate.get_date()
            self.year = str(self.dateArr[0])
            self.month = str(self.dateArr[1] + 1)
            self.day = str(self.dateArr[2])
            self.data.LATEST_ID += 1
           
            self.entryString = self.data.create_data_string(self.addCategoryComboBoxText.get_active_text(),
                                            self.year, self.month, self.day, self.addEntry.get_text(), self.addDescription.get_text(),
                                            self.data.LATEST_ID)
            
            self.addEntry.set_text("")
            self.addDescription.set_text("")
                        
            self.data.add_data(self.entryString)
