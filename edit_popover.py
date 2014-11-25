from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Edit_Popover(Gtk.Window):

    def __init__(self, data):
        #Initialize Data
        #self.data = data
        
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
        
        # Add Widgets to Grid
        self.selectorBox.add(self.editButton)
        self.selectorBox.add(self.deleteButton)
        
        self.editGrid.attach(self.selectorBox,0,0,1,1)

    def margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_bottom(margin)
    
    def on_editButton_clicked(self, button, editPopover):
        if editPopover.get_visible():
            editPopover.hide()
        else:
            editPopover.show_all()
