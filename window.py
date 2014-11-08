from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu
from data import Data
from income import Income
from expense import Expense
from sidebar import Sidebar

class Window(Gtk.Window):

    def __init__(self):
        
        self.provider = Gtk.CssProvider()
        self.provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.data = Data()

        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(1000, 700)
        
        # --- Header Bar ---
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.set_titlebar(self.hb)

        # --- Date Range Buttons (Left Side of Header Bar) ---
            
            # Create Buttons
        self.dayButton = Gtk.Button("Day")
        self.weekButton = Gtk.Button("Week")
        self.monthButton = Gtk.Button("Month")
            # Set Size
        self.dayButton.set_size_request(65,32)
        self.weekButton.set_size_request(65,32)
        self.monthButton.set_size_request(65,32)
            # Connect to handler
        self.dayButton.connect("clicked", self.on_dayButton_clicked)
        self.weekButton.connect("clicked", self.on_weekButton_clicked)
        self.monthButton.connect("clicked", self.on_monthButton_clicked)
            # Pack into Box 
        self.rangeBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.rangeBox.get_style_context(), "linked")
        self.rangeBox.add(self.dayButton)
        self.rangeBox.add(self.weekButton)
        self.rangeBox.add(self.monthButton)
        
        # --- Navigation Buttons (Center of Header Bar) ---
            
            # Create Buttons
        self.overviewButton = Gtk.Button("Overview")
        self.incomeButton = Gtk.Button("Income")
        self.expensesButton = Gtk.Button("Expenses")
            # Set Size
        self.overviewButton.set_size_request(100,32)
        self.incomeButton.set_size_request(100,32)
        self.expensesButton.set_size_request(100,32)
        # Connect to handler
        self.overviewButton.connect("clicked", self.on_overviewButton_clicked)
        self.incomeButton.connect("clicked", self.on_incomeButton_clicked)
        self.expensesButton.connect("clicked", self.on_expensesButton_clicked)
            # Pack into Box 
        self.navBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.navBox.get_style_context(), "linked")
        self.navBox.add(self.overviewButton)
        self.navBox.add(self.incomeButton)
        self.navBox.add(self.expensesButton)
        
        # --- Action Buttons (Right of Header Bar) ---
        
            # Create Buttons
        self.addButton = Gtk.Button()
        self.menuButton = Gtk.MenuButton();
            # Add Image
        self.addIcon = Gio.ThemedIcon(name="list-add-symbolic")
        self.menuIcon = Gio.ThemedIcon(name="emblem-system-symbolic")
        self.addImage = Gtk.Image.new_from_gicon(self.addIcon, Gtk.IconSize.MENU)
        self.menuImage = Gtk.Image.new_from_gicon(self.menuIcon, Gtk.IconSize.MENU)
        self.addButton.add(self.addImage)
        self.menuButton.add(self.menuImage)
            # Set Size
        self.addButton.set_size_request(32,32)
        self.menuButton.set_size_request(32,32)
            
            # Create Popovers
        self.create_add_popover()
           # Connect to handler
        self.addButton.connect("clicked", self.on_addButton_clicked)
        self.menuButton.connect("clicked", self.on_menuButton_clicked)
        
        # --- Header Bar Packing ---
        self.hb.set_custom_title(self.navBox)
        #self.hb.pack_start(self.rangeBox)
        self.hb.pack_end(self.menuButton)
        self.hb.pack_end(self.addButton)

        # --- Notebook Views ---
        self.overviewMenu = Overview_Menu()
        self.income = Income()
        self.expense = Expense()

        self.notebook = Gtk.Notebook()
        self.notebook.insert_page(self.overviewMenu.notebook, None, 0)
        self.notebook.append_page(self.income.view.grid, None)
        self.notebook.append_page(self.expense.view.grid, None)
        self.notebook.set_show_tabs(False)
        self.add(self.notebook)

    def create_add_popover(self):
        # Create Widgets
        self.addPopover = Gtk.Popover.new(self.addButton)
        self.addGrid = Gtk.Grid()
        #self.addIncomeRadio = Gtk.RadioButton.new_with_label_from_widget(None, "Income")
        self.addIncomeRadio = Gtk.RadioButton(None, "Income")
        self.addExpenseRadio = Gtk.RadioButton(self.addIncomeRadio, "Expense")
        #self.addExpenseRadio = Gtk.RadioButton.new_from_widget(self.addIncomeRadio)
        self.addStack = Gtk.Stack()
        self.addStackSwitcher = Gtk.StackSwitcher()
        self.addStack.add_titled(self.addIncomeRadio, "Income", "Income")
        self.addStack.add_titled(self.addExpenseRadio, "Expense", "Expense")
        self.addStackSwitcher.set_stack(self.addStack)
        self.addCategoryComboBoxText = Gtk.ComboBoxText()
        self.addEntryLabel = Gtk.Label("Entry")
        self.addDescriptionLabel = Gtk.Label("Description")
        self.addEntry = Gtk.Entry()
        self.addDescription = Gtk.Entry()
        self.addEntry.set_text("$")
        self.addDate = Gtk.Calendar()
        self.addSubmitButton = Gtk.Button("Submit")
        
        # Style Widgets
        self.addStackSwitcher.set_homogeneous(True)
        self.addStack.set_hexpand(True)
        
        self.add_popover_margin(self.addStackSwitcher, 10)
        self.add_popover_margin(self.addCategoryComboBoxText, 10)
        #self.add_popover_margin(self.addEntryLabel, 10)
        #self.add_popover_margin(self.addDescriptionLabel, 10)
        self.add_popover_margin(self.addEntry, 10)
        self.add_popover_margin(self.addDescription, 10)
        self.add_popover_margin(self.addDate, 10)
        self.add_popover_margin(self.addSubmitButton, 10)

        self.addCategoryComboBoxText.set_property("height-request", 34)

        for i in range(1,len(self.data.incomeMenu)):
            self.addCategoryComboBoxText.append_text(self.data.incomeMenu[i][1])
        
        # Connect Widget Handlers
        self.addStackSwitcher.connect("set-focus-child", self.on_addRadio_toggled)
        
        # Add Widgets to Grid
        self.addGrid.attach(self.addStackSwitcher,0,0,2,1)
        self.addGrid.attach(self.addCategoryComboBoxText,0,1,2,1)
        self.addGrid.attach(self.addEntryLabel,0,2,1,1)
        self.addGrid.attach(self.addDescriptionLabel,1,2,1,1)
        self.addGrid.attach(self.addEntry,0,3,1,1)
        self.addGrid.attach(self.addDescription,1,3,1,1)
        self.addGrid.attach(self.addDate,0,4,2,1)
        self.addGrid.attach(self.addSubmitButton,0,5,2,1)
        self.addPopover.add(self.addGrid)

    def add_popover_margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_end(margin)
        widget.set_margin_bottom(margin)

    def on_addRadio_toggled(self, *args):
        if args[1] != None:
            for i in range(0, len(self.data.incomeMenu) + len(self.data.expenseMenu)):
                self.addCategoryComboBoxText.remove(0)
            if args[1].get_group()[0].get_active():
                for i in range(1,len(self.data.incomeMenu)):
                    self.addCategoryComboBoxText.append_text(self.data.incomeMenu[i][1])
            if args[1].get_group()[1].get_active():
                for i in range(1,len(self.data.expenseMenu)):
                    self.addCategoryComboBoxText.append_text(self.data.expenseMenu[i][1])

    def on_dayButton_clicked(self, *args):
        print("Day Button Working!")
    
    def on_weekButton_clicked(self, *args):
        print("Week Button Working!")

    def on_monthButton_clicked(self, *args):
        print("Month Button Working!")

    def on_overviewButton_clicked(self, *args):
        self.notebook.set_current_page(0)

    def on_incomeButton_clicked(self, *args):
        self.notebook.set_current_page(1)

    def on_expensesButton_clicked(self, *args):
        self.notebook.set_current_page(2)

    def on_addButton_clicked(self, *args):
        if self.addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.addPopover.show_all()

    def on_menuButton_clicked(self, *args):
        print("Menu Button Working!")

