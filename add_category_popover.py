from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Add_Category_Popover(Gtk.Window):

    def __init__(self, data):
        #Initialize Data
        self.data = data
        # Create Widgets
        self.addGrid = Gtk.Grid()
        self.addIncomeRadio = Gtk.RadioButton.new_with_label(None, "Income")
        self.addExpenseRadio = Gtk.RadioButton.new_with_label(None, "Expense")
        self.addExpenseRadio.join_group(self.addIncomeRadio)
        self.radioBox = Gtk.Box(Gtk.Orientation.HORIZONTAL,1)
        self.radioBox.pack_start(self.addIncomeRadio, True, True, 0)
        self.radioBox.pack_start(self.addExpenseRadio, True, True, 0)
        self.addEntryLabel = Gtk.Label("Category")
        self.addEntry = Gtk.Entry()
        self.addCancelButton = Gtk.Button("Cancel")
        self.addSubmitButton = Gtk.Button("Submit")
        
        # Style Widgets
        self.radioBox.set_homogeneous(True)
        self.radioBox.set_hexpand(True)        
        self.radioBox.set_vexpand(True)        
        self.radioBox.set_property("height-request", 34)
        self.add_popover_margin(self.radioBox, 10)
        self.addIncomeRadio.set_property("draw-indicator",False)
        self.addExpenseRadio.set_property("draw-indicator",False)
        Gtk.StyleContext.add_class(self.radioBox.get_style_context(), "linked")
        self.add_popover_margin(self.addEntryLabel, 1)
        self.add_popover_margin(self.addEntry, 10)
        self.addEntry.set_margin_top(0)
        self.add_popover_margin(self.addCancelButton, 10)
        self.add_popover_margin(self.addSubmitButton, 10)

        self.radio = "income"
        
        # Connect Widget Handlers
        self.addIncomeRadio.connect("toggled", self.on_addRadio_toggled)
        
        # Add Widgets to Grid
        self.addGrid.attach(self.radioBox,0,0,2,1)
        
        self.addGrid.attach(self.addEntryLabel,0,1,2,1)
        self.addGrid.attach(self.addEntry,0,2,2,1)
        self.addGrid.attach(self.addCancelButton,0,3,1,1)
        self.addGrid.attach(self.addSubmitButton,1,3,1,1)
        self.addCancelButton.connect("clicked", self.on_addCancelButton_clicked)
        self.addSubmitButton.connect("clicked", self.on_addSubmitButton_clicked)
        self.addEntry.connect("activate", self.on_addSubmitButton_clicked)
    
    def add_popover_margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_end(margin)
        widget.set_margin_bottom(margin)
    
    def on_addCancelButton_clicked(self, button):
        self.addPopover.hide()
    
    def on_addCategoryButton_clicked(self, button, addPopover):
        self.addPopover = addPopover
        if addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.addPopover.show_all()
            self.addEntry.set_text("")
            self.addEntry.grab_focus()
    
    def on_addRadio_toggled(self, *args):
        if self.addIncomeRadio.get_active() == True:
            self.radio = "income"
        elif self.addExpenseRadio.get_active() == True:
            self.radio = "expense"
        print(self.radio)

    def on_addSubmitButton_clicked(self, button):
        self.entryString = ""
        
        if self.addEntry.get_text() == "":
            self.addEntry.set_placeholder_text("Enter A Category")
        else:
            # Create string and add to database
            self.entryString = self.data.create_category_string(self.radio, self.addEntry) 
            self.data.add_data(self.entryString)

            # Refresh the menu
            self.data.transaction_view.generate_sidebars()
            
            self.addPopover.hide()
