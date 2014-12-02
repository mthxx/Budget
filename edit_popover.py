from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Edit_Popover(Gtk.Window):

    def __init__(self, data):
        self.data = data

        # Content Grid
        self.CONTENT_GRID_INDEX = 0          # Array
        self.LAYOUT_GRID_INDEX = 0           # Element
        self.WHITESPACE_LABEL = 1            # Element

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
        
        #Initialize Data
        self.unique_id = 0
        self.entryRows = 0
        self.menu = 0
        self.editPopover = ""
        
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

        self.editPopover = editPopover
        self.unique_id = unique_id
        self.entryRows = entryRows
        self.menu = menu

    def on_editButton_clicked(self, *args):
        self.editPopover.hide()
        
        # Create editing widgets
        self.categoryLabel = Gtk.Label("Category:")
        self.calendarLabel = Gtk.Label("Date:")
        self.costLabel = Gtk.Label("Cost:")
        self.descriptionLabel = Gtk.Label("Description:")
        
        self.categoryComboBoxText = Gtk.ComboBoxText()
        self.costEntry = Gtk.Entry()
        self.descriptionEntry = Gtk.Entry()
        self.submitButton = Gtk.Button("Submit")
        self.cancelButton = Gtk.Button("Cancel")

        self.calendar = Gtk.Calendar()
        self.calendarButton = Gtk.Button()
        self.calendarPopover = Gtk.Popover.new(self.calendarButton)
        self.calendarPopover.add(self.calendar)
        
        # Connect Widgets
        self.calendarButton.connect("clicked", self.on_calendarDropdown_clicked, self.calendarPopover)
        self.calendarPopover.connect("closed", self.on_calendarDropdown_closed)

        # Style Editing Widgets
        self.categoryLabel.set_halign(Gtk.Align.END)
        self.categoryLabel.set_margin_top(20)
        
        self.categoryComboBoxText.set_margin_start(32)
        self.categoryComboBoxText.set_margin_top(20)
        
        self.calendarLabel.set_halign(Gtk.Align.END)
        self.calendarLabel.set_margin_top(8)

        self.calendarButton.set_margin_start(32)
        self.calendarButton.set_margin_top(8)
        
        self.costLabel.set_halign(Gtk.Align.END)
        self.costLabel.set_margin_top(8)

        self.costEntry.set_alignment(1)
        self.costEntry.set_margin_start(32)
        self.costEntry.set_margin_top(8)
        
        self.descriptionLabel.set_halign(Gtk.Align.END)
        self.descriptionLabel.set_margin_top(8)

        self.descriptionEntry.set_margin_start(32)
        self.descriptionEntry.set_margin_top(8)
        
        self.cancelButton.set_alignment(1, 1)
        self.cancelButton.set_margin_top(32)
        self.cancelButton.set_margin_bottom(32)

        self.submitButton.set_margin_start(32)
        self.submitButton.set_margin_top(32)
        self.submitButton.set_margin_bottom(20)

        self.cancelButton.set_margin_top(32)
        self.cancelButton.set_margin_bottom(20)
       
        # Set Calendar to currently set date
        if self.menu[0][1] == self.data.incomeMenu[0][1]:
            self.set_calendar(self.data.income)
        elif self.menu[0][1] == self.data.expenseMenu[0][1]:
            self.set_calendar(self.data.expenses)
        
        # Replace label widgets with editing widgets
        for i in range(0, len(self.entryRows)):
            if self.entryRows[i][self.UNIQUE_ID_INDEX] == self.unique_id:
                for j in range(1,len(self.menu)):
                    self.categoryComboBoxText.append_text(self.menu[j][1])
                    if self.menu[j][1] == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_text():
                        self.categoryComboBoxText.set_active(j-1)
                
                # Style Grid
                self.entryRows[i][self.ENTRY_GRID_INDEX].set_column_homogeneous(False)
                self.entryRows[i][self.ENTRY_GRID_INDEX].set_halign(Gtk.Align.CENTER)
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.EDIT_BUTTON_INDEX].hide()
                self.entryRows[i][self.COST_GRID_INDEX].hide()
                
                # Category
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].hide()
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.categoryLabel, 1,0,1,1)
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.categoryComboBoxText,2,0,1,1)
                self.categoryLabel.show()
                self.categoryComboBoxText.show()
                
                # Date
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DATE_LABEL_INDEX].hide()
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.calendarLabel,1,1,1,1)
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.calendarButton,2,1,1,1)
                self.calendarButton.set_label(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DATE_LABEL_INDEX].get_text())
                self.calendarLabel.show()
                self.calendarButton.show()
                
                # Cost
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.COST_LABEL_INDEX].hide()
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CURRENCY_LABEL_INDEX].hide()
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.costLabel,1,3,1,1)
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.costEntry,2,3,1,1)
                self.costEntry.set_text(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.COST_LABEL_INDEX].get_text())
                self.costLabel.show()
                self.costEntry.show()
                
                # Description
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DESCRIPTION_LABEL_INDEX].hide()
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.descriptionLabel,1,4,1,1)
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.descriptionEntry,2,4,1,1)
                self.descriptionEntry.set_text(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DESCRIPTION_LABEL_INDEX].get_text())
                self.descriptionLabel.show()
                self.descriptionEntry.show()

                # Add Submit/Cancel Button to popover
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.cancelButton,1,5,1,1)
                self.entryRows[i][self.ENTRY_GRID_INDEX].attach(self.submitButton,2,5,1,1)
                self.cancelButton.show()
                self.submitButton.show()


  

    def on_calendarDropdown_clicked(self, button, calendarPopover):
        if calendarPopover.get_visible():
            calendarPopover.hide()
        else:
            calendarPopover.show_all()


    def on_calendarDropdown_closed(self, calendarPopover):
#        self.calendarButton.set_label(self.calendar.get_date())
        dateString = self.data.translate_date(self.calendar.get_date(),"edit")
        self.calendarButton.set_label(dateString)
    
    def set_calendar(self,data):
        for i in range(0, len(data)):
            if data[i][self.data.UNIQUE_ID] == self.unique_id:
                self.calendar.select_month(data[i][self.data.DATE][self.data.DATE_MONTH] - 1,
                                            data[i][self.data.DATE][self.data.DATE_YEAR])
                self.calendar.select_day(data[i][self.data.DATE][self.data.DATE_DAY])
