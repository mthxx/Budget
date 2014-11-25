from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Edit_Popover(Gtk.Window):

    def __init__(self, data):
        #Initialize Data
        self.unique_id = 0
        self.entryRows = 0
        self.menu = 0
        # Create Widgets
        self.editGrid = Gtk.Grid()
        
        self.editButton = Gtk.Button("Edit")
        self.deleteButton = Gtk.Button("Delete")
        self.selectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Style Widgets
        self.editButton.set_size_request(100,32)
        self.deleteButton.set_size_request(100,32)
        Gtk.StyleContext.add_class(self.selectorBox.get_style_context(), "linked")
        self.selectorBox.set_margin_start(5)
        self.selectorBox.set_margin_top(5)
        self.selectorBox.set_margin_bottom(5)

        # Connect Widget Handlers
        self.editButton.connect("clicked", self.on_editButton_clicked)

        # Add Widgets to Grid
        self.selectorBox.add(self.editButton)
        self.selectorBox.add(self.deleteButton)
        
        self.editGrid.attach(self.selectorBox,0,0,1,1)

    def margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_bottom(margin)
    
    def on_editDropdown_clicked(self, button, editPopover, unique_id, entryRows, menu):
        if editPopover.get_visible():
            editPopover.hide()
        else:
            editPopover.show_all()
        self.unique_id = unique_id
        self.entryRows = entryRows
        self.menu = menu

    def on_editButton_clicked(self, *args):
        # Create editing widgets
        self.categoryComboBoxText = Gtk.ComboBoxText()
        
        #Style Editing Widgets
        self.categoryComboBoxText.set_margin_start(5)
        self.categoryComboBoxText.set_margin_top(8)
        self.categoryComboBoxText.set_margin_bottom(8)
        
        # Populate Category Combo Box
        #for i in range(1,len(self.menu)):
        #    self.categoryComboBoxText.append_text(self.menu[i][1])
        
        # Replace label widgets with editing widgets
        for i in range(0, len(self.entryRows)):
            if self.entryRows[i][3] == self.unique_id:
                for j in range(1,len(self.menu)):
                    self.categoryComboBoxText.append_text(self.menu[j][1])
                    #print(self.entryRows[i][1][0].get_text())
                    if self.menu[j][1] == self.entryRows[i][1][0].get_text():
                        print("Got Here")
                        self.categoryComboBoxText.set_active(j-1)
                # Category
                self.entryRows[i][1][0].hide()
                self.entryRows[i][2].attach(self.categoryComboBoxText,0,1,1,1)
                self.categoryComboBoxText.show()
                
                # Date
                # Cost
                # Description

